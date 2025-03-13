# PYTHON IMPORTS
import logging
from typing import Annotated, List, Optional
from beanie import PydanticObjectId
import base64

# LIBRARY IMPORTS
from fastapi import APIRouter, BackgroundTasks, Depends, Request

# LOCAL IMPORTS
from api.routers.auth import CurrentUser
from api.routers import GetSession
from api.models.detector import (
    
    DetectorClassListResponse,
    
    DetectorImageLabelAdd,
    DetectorImageLabelListResponse,
    DetectorImageListResponse,
    DetectorListResponse,
)
from common.models.detector import Detector as DetectorDocument
from common.models.detector import DetectorImage,DetectorImageLabel,DetectorImageMode
from common.rpc.detector_pb2_grpc import DetectorStub
from common.service import secure_channel_factory
from api.routers.recorder import Recorder


# INITIALIZATION
router = APIRouter()
log = logging.getLogger(__name__)


async def get_detector(request: Request) -> DetectorStub:
    if not hasattr(request.app.state, "detector"):
        config = request.app.state.config.detector
        channel = secure_channel_factory(
            security_config=config.security, client_config=config
        )
        request.app.state.detector = DetectorStub(channel)
    return request.app.state.detector


Detector = Annotated[DetectorStub, Depends(get_detector)]


@router.get(
    "/list/{project_id}",
    
    response_model=DetectorListResponse,
)
async def list(
    user: CurrentUser,
    detector: Detector,
    project_id: str,
    skip: int = 0,
    limit: int = 10,
    search: str = None,
):
    total, detectors = await detectorController.list(
        user.id, PydanticObjectId(project_id), skip, limit, search
    )
    return DetectorListResponse(total=total, detectors=detectors)


@router.get(
    "/count/{project_id}",  response_model=int
)
async def count(user: CurrentUser, detector: Detector, project_id: str):
    return await detectorController.count(user.id, PydanticObjectId(project_id))


@router.post(
    "/update",  response_model=DetectorDocument
)
async def update(
    user: CurrentUser, detector: Detector, id: str, name: str, description: str
):
    return await detectorController.update(
        user.id, PydanticObjectId(id), name, description
    )


@router.get(
    "/load/{id}",
    
    description="Performs the loading of a Detector",
    response_model=DetectorDocument,
)
async def load(user: CurrentUser, detector: Detector, id: str):
    return await detectorController.load(user.id, PydanticObjectId(id))


@router.post(
    "/create/{project_id}",
    
    description="Creates a new detector",
    response_model=DetectorDocument,
)
async def create(
    user: CurrentUser,
    detector: Detector,
    project_id: str,
    name: str,
    origin: Optional[str] = None,
    description: Optional[str] = "",
):
    return await detectorController.create(
        user.id, PydanticObjectId(project_id), name, description, origin
    )


@router.post(
    "/train/{id}",
    description="Trains a detector",
    response_model=bool,
)
async def train(
    user: CurrentUser,
    detector: Detector,
    backgroundTasks: BackgroundTasks,
    id: str,
    session: GetSession,
    epoch: Optional[int] = 100,
    size: Optional[int] = 640
    
):
    await detectorController.train(session,user.id, PydanticObjectId(id), epoch, size)
    return True


@router.get(
    "/image/list/{id}",
    
    response_model=DetectorImageListResponse,
)
async def image_list(
    user: CurrentUser, detector: Detector, id: str, skip: int = 0, limit: int = 10
):
    total, images = await detectorController.list_image(
        user.id, PydanticObjectId(id), skip, limit
    )
    return DetectorImageListResponse(total=total, images=images)


@router.get(
    "/image/label/list/{image_id}",
    
    response_model=DetectorImageLabelListResponse,
)
async def image_label_list(
    user: CurrentUser,
   detector: Detector,
    image_id: str,
    skip: int = 0,
    limit: int = 10,
    search: str = None,
):
    total, labels = await detectorController.rename_image_label(
        user.id, PydanticObjectId(image_id), skip, limit, search
    )
    return DetectorImageLabelListResponse(total=total, labels=labels)


@router.get(
    "/class/list/{id}",
    
    response_model=DetectorClassListResponse,
)
async def class_list(
    user: CurrentUser,
    detector: Detector,
    id: str,
    skip: int = 0,
    limit: int = 10,
    search: str = None,
):
    total, classes = await detectorController.list_class(
        user.id, PydanticObjectId(id), skip, limit, search
    )
    return DetectorClassListResponse(total=total, classes=classes)


@router.get(
    "/class/count/{id}",
    response_model=int,
)
async def class_count(user: CurrentUser, detector: Detector, id: str):
    total = await detectorController.count_class(user.id, PydanticObjectId(id))
    return total


@router.get(
    "/image/label/count/{image_id}",
    
    response_model=int,
)
async def image_list(user: CurrentUser, detector: Detector, image_id: str):
    total = await detectorController.count_image_label(user.id, PydanticObjectId(image_id))
    return total


@router.post(
    "/image/label/add",
    
    description="Adds a label to an image of a detector",
    response_model=DetectorImageLabel,
)
async def image_label_add(
    user: CurrentUser,detector: Detector, req: DetectorImageLabelAdd
):
    return await detectorController.add_image_label(
        user.id, req.image_id, req.xstart, req.xend, req.ystart, req.yend, req.classes
    )


@router.delete(
    "/image/label/remove",
    
    description="Removes a label to an image of a detector",
    response_model=bool,
)
async def image_label_remove(user: CurrentUser, detector: Detector,id: str):
    return await detectorController.remove_image_label(user.id, PydanticObjectId(id))


@router.get(
    "/image/count/{id}",
    
    response_model=int,
)
async def image_count(user: CurrentUser, detector: Detector, id: str):
    return await detectorController.count_image(user.id, PydanticObjectId(id))


@router.delete(
    "/image/remove",
    
    description="Performs the removal of a Detector Image",
    response_model=bool,
)
async def image_remove(image: str, user: CurrentUser, detector: Detector):
    return await detectorController.remove_image(user.id, PydanticObjectId(image))


@router.post(
    "/image/upload",
    
    description="Uploads an image to a detector",
    response_model=List[DetectorImage],
)
async def image_upload(
    user: CurrentUser,
  detector: Detector,
    id: str,
    data: str,
    modes: List[DetectorImageMode],
):
    return await detectorController.upload_image(
        user.id, PydanticObjectId(id), data, modes
    )


@router.post(
    "/frame/upload",
    
    description="Uploads an image from a recording frame to a detector",
    response_model=List[DetectorImage],
)
async def frame_upload(
    user: CurrentUser,
    detector: Detector,
    recorder: Recorder,
    record_id: str,
    id: str,
    frame: int,
    modes: List[DetectorImageMode],
):
    frame_bytes = await recorderController.load_record_frame(
        None, PydanticObjectId(record_id), frame
    )
    return await detectorController.upload_image(
        user.id,
        PydanticObjectId(id),
        base64.b64encode(frame_bytes).decode(),
        modes,
    )


@router.delete(
    "/remove",
    
    description="Performs the removal of a Detector",
    response_model=bool,
)
async def remove(detector_id: str, user: CurrentUser, detector: Detector,):
    return await detectorController.remove(user.id, PydanticObjectId(detector_id))
