# PYTHON IMPORTS
import io
import logging
from typing import Annotated
from beanie import PydanticObjectId
from bson import ObjectId
import base64

# LIBRARY IMPORTS
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi import FastAPI, File, UploadFile
from starlette.responses import Response


# LOCAL IMPORTS
from common.clients.trainer import TrainerClient
from api.routers.auth import CurrentUser
from common.models.train import TrainLesson


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
async def lesson(user: CurrentUser, trainer: Trainer,recordId:PydanticObjectId):
    try:
        
        found = await trainer.recordHasLesson(user,recordId)
        print(recordId)
        if found is None:
            found = await trainer.recordCreateLesson(user,recordId)
        return found 
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


@router.post(
    "/lesson/detector",
    operation_id="trainerLessonSetDetector",
    response_model=TrainLesson
)
async def lesson_set_detector(user:CurrentUser,trainer:Trainer,detectorId:PydanticObjectId,lessonId:PydanticObjectId):
    try:
        found = await trainer.lessonSetDetector(user,lessonId,detectorId)
        return found
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))
