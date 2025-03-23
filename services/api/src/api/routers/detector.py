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
from common.models.detector import DetectObject, DetectText, Detector as DetectorDocument, DetectorClass
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
    "/count/{projectId}",  response_model=int
)
async def count(user: CurrentUser, detector: Detector, projectId: PydanticObjectId):
    try:
        return await detector.countDetector(user,projectId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


@router.post(
    "/update",  response_model=DetectorDocument
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
    operation_id="detectObjects",
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
    operation_id="detectObjectsFromFrame",
    response_model=List[DetectObject]
)
async def objects_frame(user:CurrentUser,detector: Detector,recorder:Recorder,detectorId:PydanticObjectId,recordId: PydanticObjectId,frame:int, confidence:float):
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
    operation_id="detectTexts",
    response_model=List[DetectText]
)
async def texts(user:CurrentUser,detector: Detector,payload:DetectorTextsPayload):
    try:
        return await detector.detectTexts(user,payload.data,payload.confidence)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



@router.post(
    "/frame/texts",
    description="Performs the detection of texts from recording frame image",
    operation_id="detectTextsFromFrame",
    response_model=List[DetectText]
)
async def texts_frame(user:CurrentUser,detector: Detector,recorder:Recorder,recordId: PydanticObjectId,frame:int, confidence:float):
    try:
        data = await recorder.loadRecordFrameBase64(user,recordId,frame)
        return await detector.detectTexts(user,data,confidence)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


@router.post(
    "/create/{projectId}",
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
    response_model=DetectorImageLabelListResponse,
)
async def image_label_list(
    user: CurrentUser,
    detector: Detector,
    imageId: PydanticObjectId,
    skip: int = 0,
    limit: int = 10,
    search: str = None,
):
    try:
        total, labels = await detector.listDetectorImageLabel(user,imageId,skip,limit,search)
        return DetectorImageLabelListResponse(total=total, labels=labels)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))

                                  
class DetectorClassListResponse(BaseModel):
    classes: List[DetectorClass]
    total: int
                      

@router.get(
    "/class/list/{detectorId}",
    
    response_model=DetectorClassListResponse,
)
async def class_list(
    user: CurrentUser,
    detector: Detector,
    detectorId: PydanticObjectId,
    skip: int = 0,
    limit: int = 10,
    search: str = None,
):
    try:
        total, classes = await detector.listDetectorClass(user,detectorId,skip,limit,search)
        return DetectorClassListResponse(total=total, classes=classes)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


@router.get(
    "/class/exists/{detectorId}",
    response_model=bool,
)
async def class_exists(
    user: CurrentUser,
    detector: Detector,
    detectorId: PydanticObjectId,
    name:str
):
    try:
        if await detector.existsDetectorClass(user,detectorId,name) is not None:
            return True
        else:
            return False
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



@router.post(
    "/class/add/{detectorId}",
    response_model=DetectorClass,
)
async def class_add(
    user: CurrentUser,
    detector: Detector,
    detectorId: PydanticObjectId,
    name:str
):
    try:
        return await detector.addDetectorClass(user,detectorId,name)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))




@router.get(
    "/class/count/{detectorId}",
    response_model=int,
)
async def class_count(user: CurrentUser, detector: Detector, detectorId: PydanticObjectId):
    try:
        return await detector.countDetectorClass(user,detectorId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


@router.get(
    "/image/label/count/{imageId}",
    response_model=int,
)
async def image_list(user: CurrentUser, detector: Detector, imageId: PydanticObjectId):
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
    classes:List[str]  

@router.post(
    "/image/label/add",
    description="Adds a label to an image of a detector",
    response_model=DetectorImageLabel,
)
async def image_label_add(
    user: CurrentUser,detector: Detector, req: DetectorImageLabelAdd
):
    try:
        return await detector.addDetectorImageLabel(user,req.image_id,req.xstart,req.xend,req.ystart,req.yend,req.classes)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



@router.delete(
    "/image/label/remove",
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
    response_model=int,
)
async def image_count(user: CurrentUser, detector: Detector, detectorId: PydanticObjectId):
    try:
        return await detector.countDetectorImage(user,detectorId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



@router.delete(
    "/image/remove",
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
    description="Performs the removal of a Detector",
    response_model=bool,
)
async def remove(detectorId: PydanticObjectId, user: CurrentUser, detector: Detector,):
    try:
        return await detector.removeDetector(user,detectorId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))
