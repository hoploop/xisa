# PYTHON IMPORTS
import io
import logging
import os
from typing import Annotated, List, Optional
from beanie import PydanticObjectId

# LIBRARY IMPORTS
from fastapi import APIRouter, Depends, Request
from fastapi.responses import StreamingResponse
from starlette.responses import Response


# LOCAL IMPORTS
from api.routers.auth import CurrentUser
from common.rpc.workspace_pb2_grpc import WorkspaceStub
from common.service import secure_channel_factory


# INITIALIZATION
router = APIRouter()
log = logging.getLogger(__name__)



async def get_workspace(request: Request) -> WorkspaceStub:
    if not hasattr(request.app.state, "workspace"):
        config = request.app.state.config.workspace
        channel = secure_channel_factory(
            security_config=config.security, client_config=config
        )
        request.app.state.workspace = WorkspaceStub(channel)
    return request.app.state.workspace


Workspace = Annotated[WorkspaceStub, Depends(get_workspace)]