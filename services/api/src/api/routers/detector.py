# PYTHON IMPORTS
import logging
from typing import List, Optional
from beanie import PydanticObjectId
import base64

# LIBRARY IMPORTS
from fastapi import APIRouter, BackgroundTasks

# LOCAL IMPORTS
from api.routers.auth import CurrentUser
from api.controllers.recorder import GetRecorderController
from api.routers import GetSession
from api.models.detector import (
    Detector,
    DetectorClassListResponse,
    DetectorImage,
    DetectorImageLabel,
    DetectorImageLabelAdd,
    DetectorImageLabelListResponse,
    DetectorImageListResponse,
    DetectorImageMode,
    DetectorListResponse,
)
from api.controllers.detector import GetDetectorController


# INITIALIZATION
router = APIRouter()
log = logging.getLogger(__name__)



@router.get(
    "/list/{project_id}",
    
    response_model=DetectorListResponse,
)
async def list(
    user: CurrentUser,
    detectorController: GetDetectorController,
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
async def count(user: CurrentUser, detectorController: GetDetectorController, project_id: str):
    return await detectorController.count(user.id, PydanticObjectId(project_id))


@router.post(
    "/update",  response_model=Detector
)
async def update(
    user: CurrentUser, detectorController: GetDetectorController, id: str, name: str, description: str
):
    return await detectorController.update(
        user.id, PydanticObjectId(id), name, description
    )


@router.get(
    "/load/{id}",
    
    description="Performs the loading of a Detector",
    response_model=Detector,
)
async def load(user: CurrentUser, detectorController: GetDetectorController, id: str):
    return await detectorController.load(user.id, PydanticObjectId(id))


@router.post(
    "/create/{project_id}",
    
    description="Creates a new detector",
    response_model=Detector,
)
async def create(
    user: CurrentUser,
    detectorController: GetDetectorController,
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
    detectorController: GetDetectorController,
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
    user: CurrentUser, detectorController: GetDetectorController, id: str, skip: int = 0, limit: int = 10
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
    detectorController: GetDetectorController,
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
    detectorController: GetDetectorController,
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
async def class_count(user: CurrentUser, detectorController: GetDetectorController, id: str):
    total = await detectorController.count_class(user.id, PydanticObjectId(id))
    return total


@router.get(
    "/image/label/count/{image_id}",
    
    response_model=int,
)
async def image_list(user: CurrentUser, detectorController: GetDetectorController, image_id: str):
    total = await detectorController.count_image_label(user.id, PydanticObjectId(image_id))
    return total


@router.post(
    "/image/label/add",
    
    description="Adds a label to an image of a detector",
    response_model=DetectorImageLabel,
)
async def image_label_add(
    user: CurrentUser, detectorController: GetDetectorController, req: DetectorImageLabelAdd
):
    return await detectorController.add_image_label(
        user.id, req.image_id, req.xstart, req.xend, req.ystart, req.yend, req.classes
    )


@router.delete(
    "/image/label/remove",
    
    description="Removes a label to an image of a detector",
    response_model=bool,
)
async def image_label_remove(user: CurrentUser, detectorController: GetDetectorController, id: str):
    return await detectorController.remove_image_label(user.id, PydanticObjectId(id))


@router.get(
    "/image/count/{id}",
    
    response_model=int,
)
async def image_count(user: CurrentUser, detectorController: GetDetectorController, id: str):
    return await detectorController.count_image(user.id, PydanticObjectId(id))


@router.delete(
    "/image/remove",
    
    description="Performs the removal of a Detector Image",
    response_model=bool,
)
async def image_remove(image: str, user: CurrentUser, detectorController: GetDetectorController):
    return await detectorController.remove_image(user.id, PydanticObjectId(image))


@router.post(
    "/image/upload",
    
    description="Uploads an image to a detector",
    response_model=List[DetectorImage],
)
async def image_upload(
    user: CurrentUser,
    detectorController: GetDetectorController,
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
    detectorController: GetDetectorController,
    recorderController: GetRecorderController,
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
async def remove(detector: str, user: CurrentUser, detectorController: GetDetectorController):
    return await detectorController.remove(user.id, PydanticObjectId(detector))
