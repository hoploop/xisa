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
from common.models.auth import User

# INITIALIZATION
router = APIRouter()
log = logging.getLogger(__name__)