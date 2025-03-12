# PYTHON IMPORTS
import logging
from typing import Annotated, Dict, Optional

# LIBRARY IMPORTS
from beanie import PydanticObjectId
from api.models.auth import RegisterRequest, Token, User

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
from api.controllers.auth import Auth, AuthController

# INITIALIZATION
router = APIRouter()
log = logging.getLogger(__name__)


oauth2_scheme: OAuth2PasswordBearer = OAuth2PasswordBearer(
    tokenUrl="auth/login",
    scopes={
        "me": "Read information about the current user.",
        "items": "Read items.",
    },
)



async def get_current_user(
    security_scopes: SecurityScopes, token: Annotated[str, Depends(oauth2_scheme)]
):
    if token in AuthController.USERS:
        return AuthController.USERS[token]
    else:
        token_doc = await Token.find_many(Token.code == token).first_or_none()
        if token_doc is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not logged in",
                headers={"WWW-Authenticate": "Bearer"},
            )
        user = await User.find_many(User.id == token_doc.user).first_or_none()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not logged in",
                headers={"WWW-Authenticate": "Bearer"},
            )
        AuthController.USERS[token] = user
        return AuthController.USERS[token]


oauth2_scheme_no_error: OAuth2PasswordBearer = OAuth2PasswordBearer(
    tokenUrl="auth/login",
    scopes={
        "me": "Read information about the current user.",
        "items": "Read items.",
    },
    auto_error=False,
)


async def get_current_token_or_none(
    token: Annotated[str, Depends(oauth2_scheme_no_error)]
) -> Optional[str]:
    try:
        return token
    except Exception as e:
        return None


TokenOrNone = Annotated[str | None, Depends(get_current_token_or_none)]
CurrentUser = Annotated[User, Depends(get_current_user)]

@router.get(
    "/check",
    
    description="Checks the current token",
    response_model=bool,
)
async def check(host: GetHost, token: TokenOrNone, session: GetSession, auth: Auth):
    if token is None: return False
    return await auth.check_token(token)


@router.post("/login",  description="Performs the login")
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    host: GetHost,
    session: GetSession,
    auth: Auth,
):
    return await auth.login(form_data.username, form_data.password,host)


@router.get(
    "/logout",
    description="Performs the logout",
    
    response_model=bool,
)
async def logout(host: GetHost, token: TokenOrNone, session: GetSession, auth: Auth):
    return await auth.logout(token)


@router.put("/register",  response_model=bool)
async def register(req: RegisterRequest, auth: Auth):
    return await auth.register(req.username, req.email, req.password)


@router.post("/unregister",  response_model=bool)
async def unregister(token: TokenOrNone, auth: Auth):
    return await auth.unregister(token)


@router.post("/password/reset",  response_model=bool)
async def password_reset(old: str, new: str, token: TokenOrNone,host:GetHost,auth:Auth):
    return await auth.password_reset(token,host,old,new)
    