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
from common.models.train import TrainImageObject, TrainLesson


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


@router.get(
    "/lesson/{recordId}",
    operation_id="trainerLesson",
    description="Checks if a recorder is running",
    response_model=TrainLesson,
)
async def lesson(user: CurrentUser, trainer: Trainer, recordId: PydanticObjectId):
    try:

        found = await trainer.recordHasLesson(user, recordId)
        print(recordId)
        if found is None:
            found = await trainer.recordCreateLesson(user, recordId)
        return found
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


@router.post(
    "/lesson/detector",
    operation_id="trainerLessonSetDetector",
    response_model=TrainLesson,
)
async def lesson_set_detector(
    user: CurrentUser,
    trainer: Trainer,
    detectorId: PydanticObjectId,
    lessonId: PydanticObjectId,
):
    try:
        found = await trainer.lessonSetDetector(user, lessonId, detectorId)
        return found
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



class TrainImageObjectUpdatePayload(BaseModel):
    id: PydanticObjectId
    labels: List[str]
    val: bool
    test: bool
    train: bool


@router.put(
    "/lesson/image/object/update",
    operation_id="trainerLessonImageObjectUpdate",
    response_model=bool,
)
async def lesson_image_object_update(
    user: CurrentUser, trainer: Trainer, payload: TrainImageObjectUpdatePayload
):
    try:
        return await trainer.trainImageObjectUpdate(user,payload.id, payload.labels,payload.val,payload.test,payload.train)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


class TrainImageObjectPayload(BaseModel):
    lessonId: PydanticObjectId
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
    "/lesson/image/object",
    operation_id="trainerLessonImageObject",
    response_model=PydanticObjectId,
)
async def lesson_image_object(
    user: CurrentUser, trainer: Trainer, payload: TrainImageObjectPayload
):
    try:
        found = await trainer.trainImageObject(
            user,
            payload.lessonId,
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
    "/lesson/image/object/list/{lessonId}",
    operation_id="trainerLessonImageObjectList",
    response_model=TrainImageObjectListResponse,
)
async def lesson_image_object_list(
    user: CurrentUser, trainer: Trainer, lessonId: PydanticObjectId, frame:int = -1
):
    try:
        total, ret = await trainer.trainImageObjectList(user,lessonId,frame)
        return TrainImageObjectListResponse(total=total,objects=ret)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


@router.delete(
    "/lesson/image/object/remove/{objectId}",
    operation_id="trainerLessonImageObjectRemove",
    response_model=bool,
)
async def lesson_image_object_remove(user:CurrentUser,trainer:Trainer,objectId:PydanticObjectId):
    try:
        return await trainer.trainImageObjectRemove(user,objectId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))
 