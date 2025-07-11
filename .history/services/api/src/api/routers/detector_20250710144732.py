# PYTHON IMPORTS
import logging
from typing import Annotated, List, Optional
from beanie import PydanticObjectId
import base64

# LIBRARY IMPORTS
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, Request, status
from pydantic import BaseModel

# LOCAL IMPORTS
from api.routers.auth import CurrentUser
from api.routers import GetSession
from common.clients.detector import DetectorClient
from common.models.detector import DetectObject, DetectText, Detector as DetectorDocument, DetectorLabel, DetectorSuggestion
from common.models.detector import DetectorImage,DetectorImageLabel,DetectorImageMode
from api.routers.recorder import Recorder


# INITIALIZATION
router = APIRouter()
log = logging.getLogger(__name__)


async def get_detector(request: Request) -> DetectorClient:
    if not hasattr(request.app.state, "detector"):
        config = request.app.state.config.detector
        request.app.state.detector = DetectorClient(config)
        await request.app.state.detector.startup()
    return request.app.state.detector


Detector = Annotated[DetectorClient, Depends(get_detector)]

class DetectorListResponse(BaseModel):
    detectors: List[DetectorDocument] 
    total: int
                

@router.get(
    "/list/{projectId}",
    operation_id="detectorList",
    response_model=DetectorListResponse,
)
async def list(
    user: CurrentUser,
    detector: Detector,
    projectId: PydanticObjectId,
    skip: int = 0,
    limit: int = 10,
    search: str = None,
):
    try:
        total, detectors = await detector.listDetector(user,projectId,skip,limit,search)
        return DetectorListResponse(total=total,detectors=detectors)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



@router.get(
    "/label/{detectorId}",  
    operation_id="detectorLabel",
    response_model=DetectorLabel
)
async def label(user: CurrentUser, detector: Detector, detectorId: PydanticObjectId,name:str):
    try:
        return await detector.findDetectorLabel(user,detectorId,name)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



@router.get(
    "/count/{projectId}",  
    operation_id="detectorCount",
    response_model=int
)
async def count(user: CurrentUser, detector: Detector, projectId: PydanticObjectId):
    try:
        return await detector.countDetector(user,projectId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


@router.post(
    "/update",  
    operation_id="detectorUpdate",
    response_model=DetectorDocument
)
async def update(
    user: CurrentUser, detector: Detector, detectorId: PydanticObjectId, name: str, description: str
):
    try:
        return await detector.updateDetector(user,detectorId,name,description)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))




@router.get(
    "/load/{detectorId}",
    operation_id="detectorLoad",
    description="Performs the loading of a Detector",
    response_model=DetectorDocument,
)
async def load(user: CurrentUser, detector: Detector, detectorId: PydanticObjectId):
    try:
        return await detector.loadDetector(user,detectorId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))

class DetectorObjectsPayload(BaseModel):
    data: str
    confidence: float = 0.7

@router.post(
    "/objects/{detectorId}",
    description="Performs the detection of objects from base64 image",
    operation_id="detectorObjects",
    response_model=List[DetectObject]
)
async def objects(user:CurrentUser,detector: Detector,detectorId: PydanticObjectId, payload:DetectorObjectsPayload):
    try:
        return await detector.detectObjects(user,detectorId,payload.data,payload.confidence)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


@router.post(
    "/frame/objects/{recordId}",
    description="Performs the detection of objects from recording frame image",
    operation_id="detectorObjectsFromFrame",
    response_model=List[DetectObject]
)
async def objects_from_frame(user:CurrentUser,detector: Detector,recorder:Recorder,detectorId:PydanticObjectId,recordId: PydanticObjectId,frame:int, confidence:float):
    try:
        data = await recorder.loadRecordFrameBase64(user,recordId,frame)
        return await detector.detectObjects(user,detectorId,data,confidence)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))

class DetectorTextsPayload(BaseModel):
    data: str
    confidence: float = 0.7

@router.post(
    "/texts",
    description="Performs the detection of texts from base64 image",
    operation_id="detectorTexts",
    response_model=List[DetectText]
)
async def texts(user:CurrentUser,detector: Detector,payload:DetectorTextsPayload):
    try:
        return await detector.detectTexts(user,payload.data,payload.confidence)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))





@router.post(
    "/frame/suggestions",
    description="Performs the detection of suggestions from recording frame image",
    operation_id="detectorFrameSuggestions",
    response_model=List[DetectorSuggestion]
)
async def frame_suggestions(user:CurrentUser,detector: Detector,recorder:Recorder,detectorId:PydanticObjectId,eventId:PydanticObjectId, confidence:float):
    try:
        event = await recorder.loadEvent(user,eventId)
        log.debug(str(event))
        data = await recorder.loadRecordFrameBase64(user,event.record,event.frame)
        return  await detector.suggestStep(user,data,detectorId,eventId,confidence)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



@router.post(
    "/frame/texts",
    description="Performs the detection of texts from recording frame image",
    operation_id="detectorFrameTexts",
    response_model=List[DetectText]
)
async def frame_texts(user:CurrentUser,detector: Detector,recorder:Recorder,recordId: PydanticObjectId,frame:int, confidence:float):
    try:
        data = await recorder.loadRecordFrameBase64(user,recordId,frame)
        return await detector.detectTexts(user,data,confidence)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


@router.post(
    "/create/{projectId}",
    operation_id="detectorCreate",
    description="Creates a new detector",
    response_model=DetectorDocument,
)
async def create(
    user: CurrentUser,
    detector: Detector,
    projectId: PydanticObjectId,
    name: str,
    origin: Optional[str] = None,
    description: Optional[str] = "",
):
    try:
        return await detector.createDetector(user,projectId,name,description,origin)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



@router.post(
    "/train/{detectorId}",
    operation_id="detectorTrain",
    description="Trains a detector",
    response_model=bool,
)
async def train(
    user: CurrentUser,
    detector: Detector,
    backgroundTasks: BackgroundTasks,
    detectorId: PydanticObjectId,
    session: GetSession,
    epochs: Optional[int] = 100,
    size: Optional[int] = 640
    
):
    try:
        return await detector.trainDetector(user,detectorId,session,epochs=epochs,image_size=size)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



class DetectorImageListResponse(BaseModel):
    images: List[DetectorImage]
    total: int
                          

@router.get(
    "/image/list/{detectorId}",
    operation_id="detectorImageList",
    response_model=DetectorImageListResponse,
)
async def image_list(
    user: CurrentUser, detector: Detector, detectorId: PydanticObjectId, skip: int = 0, limit: int = 10
):
    
    try:
        total, images = await detector.listDetectorImage(user,detectorId,skip,limit)
        return DetectorImageListResponse(total=total, images=images)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


class DetectorImageLabelListResponse(BaseModel):
    labels: List[DetectorImageLabel]
    total: int
                                                            
                          

@router.get(
    "/image/label/list/{imageId}",
    operation_id="detectorImageLabelList",
    response_model=DetectorImageLabelListResponse,
)
async def image_label_list(
    user: CurrentUser,
    detector: Detector,
    imageId: PydanticObjectId,
    skip: int = 0,
    limit: int = 10,
    search: str = None
    
):
    try:
        total, labels = await detector.listDetectorImageLabel(user,imageId,skip,limit,search)
        return DetectorImageLabelListResponse(total=total, labels=labels)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))

                                  
class DetectorLabelListResponse(BaseModel):
    labels: List[DetectorLabel]
    total: int
                      

@router.get(
    "/label/list/{detectorId}",
    operation_id="detectorLabelList",
    response_model=DetectorLabelListResponse,
)
async def label_list(
    user: CurrentUser,
    detector: Detector,
    detectorId: PydanticObjectId,
    skip: int = 0,
    limit: int = 10,
    search: str = None,
    exclude: List[str] = []
):
    try:
        total, labels = await detector.listDetectorLabel(user,detectorId,skip,limit,search,exclude)
        return DetectorLabelListResponse(total=total, labels=labels)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


@router.get(
    "/label/exists/{detectorId}",
    operation_id="detectorLabelExists",
    response_model=bool,
)
async def label_exists(
    user: CurrentUser,
    detector: Detector,
    detectorId: PydanticObjectId,
    name:str
):
    try:
        if await detector.existsDetectorLabel(user,detectorId,name) is not None:
            return True
        else:
            return False
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



@router.post(
    "/label/add/{detectorId}",
    operation_id="detectorLabelAdd",
    response_model=DetectorLabel,
)
async def label_add(
    user: CurrentUser,
    detector: Detector,
    detectorId: PydanticObjectId,
    name:str
):
    try:
        return await detector.addDetectorLabel(user,detectorId,name)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



@router.delete(
    "/label/remove",
    operation_id="detectorLabelRemove",
    description="Removes a label from a detector",
    response_model=bool,
)
async def label_remove(user: CurrentUser, detector: Detector,labelId: PydanticObjectId):
    try:
        return await detector.removeDetectorLabel(user,labelId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


@router.get(
    "/label/removable/{labelId}",
    operation_id="detectorLabelCanRemove",
    response_model=bool,
)
async def label_can_remove(user: CurrentUser, detector: Detector, labelId: PydanticObjectId):
    try:
        return await detector.canRemoveDetectorLabel(user,labelId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



@router.get(
    "/label/count/{detectorId}",
    operation_id="detectorLabelCount",
    response_model=int,
)
async def label_count(user: CurrentUser, detector: Detector, detectorId: PydanticObjectId):
    try:
        return await detector.countDetectorLabel(user,detectorId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


@router.get(
    "/image/label/count/{imageId}",
    operation_id="detectorImageLabelCount",
    response_model=int,
)
async def image_label_count(user: CurrentUser, detector: Detector, imageId: PydanticObjectId):
    try:
        return await detector.countDetectorImageLabel(user,imageId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



              
class DetectorImageLabelAdd(BaseModel):
    image_id:PydanticObjectId
    xstart:float
    xend:float
    ystart:float
    yend:float
    label:str

@router.post(
    "/image/label/add",
    operation_id="detectorImageLabelAdd",
    description="Adds a label to an image of a detector",
    response_model=DetectorImageLabel,
)
async def image_label_add(
    user: CurrentUser,detector: Detector, req: DetectorImageLabelAdd
):
    try:
        return await detector.addDetectorImageLabel(user,req.image_id,req.xstart,req.xend,req.ystart,req.yend,req.label)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



@router.delete(
    "/image/label/remove",
    operation_id="detectorImageLabelRemove",
    description="Removes a label to an image of a detector",
    response_model=bool,
)
async def image_label_remove(user: CurrentUser, detector: Detector,labelId: PydanticObjectId):
    try:
        return await detector.removeDetectorImageLabel(user,labelId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



@router.get(
    "/image/count/{detectorId}",
    operation_id="detectorImageCount",
    response_model=int,
)
async def image_count(user: CurrentUser, detector: Detector, detectorId: PydanticObjectId):
    try:
        return await detector.countDetectorImage(user,detectorId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



@router.get(
    "/label/load/{labelId}",
    operation_id="detectorLabelLoad",
    response_model=DetectorLabel,
)
async def label_load(user: CurrentUser, detector: Detector, labelId: PydanticObjectId):
    try:
        return await detector.loadDetectorLabel(user,labelId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



@router.delete(
    "/image/remove",
    operation_id="detectorImageRemove",
    description="Performs the removal of a Detector Image",
    response_model=bool,
)
async def image_remove(imageId: PydanticObjectId, user: CurrentUser, detector: Detector):
    try:
        return await detector.removeDetectorImage(user,imageId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



@router.post(
    "/image/upload",
    operation_id="detectorImageUpload",
    description="Uploads an image to a detector",
    response_model=List[DetectorImage],
)
async def image_upload(
    user: CurrentUser,
    detector: Detector,
    detectorId: PydanticObjectId,
    data: str,
    modes: List[DetectorImageMode],
):
    try:
         return await detector.uploadDetectorImage(user,detectorId,data,modes)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))
   

@router.post(
    "/frame/upload",
    operation_id="detectorFrameUpload",
    description="Uploads an image from a recording frame to a detector",
    response_model=List[DetectorImage],
)
async def frame_upload(
    user: CurrentUser,
    detector: Detector,
    recorder: Recorder,
    recordId: PydanticObjectId,
    detectorId: PydanticObjectId,
    frame: int,
    modes: List[DetectorImageMode],
):
    try:
        frame_bytes = await recorder.loadRecordFrame(user,recordId,frame)
        data = base64.b64encode(frame_bytes).decode()
        return await detector.uploadDetectorImage(user,detectorId,data,modes)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))

@router.delete(
    "/remove",
    operation_id="detectorRemove",
    description="Performs the removal of a Detector",
    response_model=bool,
)
async def remove(detectorId: PydanticObjectId, user: CurrentUser, detector: Detector):
    try:
        return await detector.removeDetector(user,detectorId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))

@router.get("/results/{detectorId}/{filename}")
async def get_static_file(user: CurrentUser,detectorId:PydanticObjectId,filename: str, detector: Detector):
    try:
        # Call gRPC to get file bytes
        grpc_request = my_grpc_pb2.FileRequest(filename=filename)
        grpc_response = stub.GetFile(grpc_request)

        if not grpc_response.found:
            raise HTTPException(status_code=404, detail="File not found")

        # Return the file to the browser
        return Response(
            content=grpc_response.data,
            media_type=grpc_response.content_type,
            headers={
                "Content-Disposition": f"inline; filename={filename}"
            }
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))