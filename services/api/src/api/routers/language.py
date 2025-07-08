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
from common.clients.language import LanguageClient
from common.clients.trainer import TrainerClient
from api.routers.auth import CurrentUser



# INITIALIZATION
router = APIRouter()
log = logging.getLogger(__name__)


async def get_language(request: Request) -> LanguageClient:
    if not hasattr(request.app.state, "language"):
        config = request.app.state.config.language
        request.app.state.language = LanguageClient(config)
        await request.app.state.language.startup()
    return request.app.state.language


Language = Annotated[LanguageClient, Depends(get_language)]