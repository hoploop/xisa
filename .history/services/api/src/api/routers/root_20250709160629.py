# PYTHON IMPORTS
import logging
from typing import Annotated, Optional
from pydantic import BaseModel

# LIBRARY IMPORTS

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Request,
    status,
)
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    SecurityScopes,
)

# LOCAL IMPORTS
from api.routers import GetSession, GetHost
from common.clients.auth import AuthClient
from common.clients.nanny import NannyClient
from common.models.auth import User

# INITIALIZATION
router = APIRouter()
log = logging.getLogger(__name__)


async def get_nanny(request: Request) -> NannyClient:
    if not hasattr(request.app.state, "nanny"):
        config = request.app.state.config.nanny
        request.app.state.nanny = NannyClient(config)
        await request.app.state.nanny.startup()
    return request.app.state.nanny


Nanny = Annotated[NannyClient, Depends(get_nanny)]

