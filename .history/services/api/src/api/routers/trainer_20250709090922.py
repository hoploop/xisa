# PYTHON IMPORTS
import io
import logging
from typing import Annotated, List
from beanie import PydanticObjectId
from bson import ObjectId
import base64

# LIBRARY IMPORTS
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from starlette.responses import Response


# LOCAL IMPORTS
from common.clients.trainer import TrainerClient
from api.routers.auth import CurrentUser
from common.models.trainer import TrainImageObject


# INITIALIZATION
router = APIRouter()
log = logging.getLogger(__name__)


async def get_trainer(request: Request) -> TrainerClient:
    if not hasattr(request.app.state, "trainer"):
        config = request.app.state.config.trainer
        request.app.state.trainer = TrainerClient(config)
        await request.app.state.trainer.startup()
    return request.app.state.trainer


Trainer = Annotated[TrainerClient, Depends(get_trainer)]



class TrainImageObjectUpdatePayload(BaseModel):
    id: PydanticObjectId
    labels: List[str]
    val: bool
    test: bool
    train: bool
    xstart: float
    xend: float
    ystart: float
    yend: float


@router.put(
    "/image/object/update",
    operation_id="trainerImageObjectUpdate",
    response_model=bool,
)
async def image_object_update(
    user: CurrentUser, trainer: Trainer, payload: TrainImageObjectUpdatePayload
):
    try:
        return await trainer.trainImageObjectUpdate(user,payload.id, payload.labels,payload.val,payload.test,payload.train,payload.xstart,
            payload.xend,
            payload.ystart,
            payload.yend)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


class TrainImageObjectPayload(BaseModel):
    recordId: PydanticObjectId
    detectorId: PydanticObjectId
    frame: int
    labels: List[str]
    xstart: float
    xend: float
    ystart: float
    yend: float
    val: bool
    test: bool
    train: bool


@router.post(
    "/image/object/create",
    operation_id="trainerImageObjectCreate",
    response_model=TrainImageObject,
)
async def image_object_create(
    user: CurrentUser, trainer: Trainer, payload: TrainImageObjectPayload
):
    try:
        found = await trainer.trainImageObject(
            user,
            payload.detectorId,
            payload.recordId,
            payload.frame,
            payload.labels,
            payload.xstart,
            payload.xend,
            payload.ystart,
            payload.yend,
            payload.train,
            payload.test,
            payload.val,
        )
        return found
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


class TrainImageObjectListResponse(BaseModel):
    total: int
    objects: List[TrainImageObject]

@router.get(
    "/image/object/list",
    operation_id="trainerImageObjectList",
    response_model=TrainImageObjectListResponse,
)
async def image_object_list(
    user: CurrentUser, trainer: Trainer,detectorId:PydanticObjectId, recordId: PydanticObjectId, frame:int = -1
):
    try:
        log.debug('Loading lesosn image for frame: {0}'.format(frame))
        total, ret = await trainer.trainImageObjectList(user,detectorId,recordId,frame)
        return TrainImageObjectListResponse(total=total,objects=ret)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


@router.get(
    "/image/object/count/detector/{detectorId}",
    operation_id="trainerImageObjectCountByDetector",
    response_model=int,
)
async def image_object_count_by_detector(
    user: CurrentUser, trainer: Trainer, detectorId: PydanticObjectId
):
    try:
        return await trainer.trainImageObjectCountByDetector(user,detectorId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



@router.post(
    "/image/object/to/detector/{detectorId}",
    operation_id="trainerImageObjectToDetector",
    response_model=int,
)
async def image_object_to_detector(
    user: CurrentUser, trainer: Trainer, detectorId: PydanticObjectId
):
    try:
        return await trainer.trainImageObjectToDetector(user,detectorId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



@router.delete(
    "/image/object/remove/{objectId}",
    operation_id="trainerImageObjectRemove",
    response_model=bool,
)
async def image_object_remove(user:CurrentUser,trainer:Trainer,objectId:PydanticObjectId):
    try:
        return await trainer.trainImageObjectRemove(user,objectId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))
 
 
@router.post(
     "/session/create/{detectorId}",
     response_model=bool
 )
async def session_create(user:CurrentUser,trainer:Trainer,detectorId:PydanticObjectId):
    try:
        return await trainer.trainSessionCreate(user,detectorId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))
 
 
@router.post(
    "/session/update/{sessionId}",
    status:TrainSessionStatus,
    response_model=bool
 )
async def session_update(user:CurrentUser,trainer:Trainer,sessionId:PydanticObjectId):
    try:
        return await trainer.trainSessionUpdate(user,sessionId,)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))
 
 