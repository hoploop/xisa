# PYTHON IMPORTS
import io
import logging
from typing import Annotated
from bson import ObjectId
import base64

# LIBRARY IMPORTS
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi import FastAPI, File, UploadFile
from starlette.responses import Response


# LOCAL IMPORTS
from api.routers import GetFilesystem
from common.rpc.player_pb2_grpc import PlayerStub
from common.service import secure_channel_factory


# INITIALIZATION
router = APIRouter()
log = logging.getLogger(__name__)



async def get_player(request: Request) -> PlayerStub:
    if not hasattr(request.app.state, "player"):
        config = request.app.state.config.player
        channel = secure_channel_factory(
            security_config=config.security, client_config=config
        )
        request.app.state.player = PlayerStub(channel)
    return request.app.state.player


Player = Annotated[PlayerStub, Depends(get_player)]