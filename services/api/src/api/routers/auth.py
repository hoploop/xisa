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
from common.models.auth import User
from common.rpc.auth_pb2 import (
    CheckRequest,
    LoginRequest,
    LogoutRequest,
    ResetPasswordRequest,
    UnregisterRequest,
    UserRequest,
    RegisterRequest as RpcRegisterRequest,
)
from common.rpc.auth_pb2_grpc import AuthStub
from common.service import secure_channel_factory
from common.utils.conversions import Conversions

# INITIALIZATION
router = APIRouter()
log = logging.getLogger(__name__)


async def get_auth(request: Request) -> AuthStub:
    if not hasattr(request.app.state, "auth"):
        config = request.app.state.config.auth
        channel = secure_channel_factory(
            security_config=config.security, client_config=config
        )
        request.app.state.auth = AuthStub(channel)
    return request.app.state.auth


Auth = Annotated[AuthStub, Depends(get_auth)]

oauth2_scheme: OAuth2PasswordBearer = OAuth2PasswordBearer(
    tokenUrl="auth/login",
    scopes={
        "me": "Read information about the current user.",
        "items": "Read items.",
    },
)


async def get_current_user(
    security_scopes: SecurityScopes,
    token: Annotated[str, Depends(oauth2_scheme)],
    auth: Auth,
):
    req = UserRequest(token=token)
    res = await auth.user(req)
    if res.status == False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not logged in",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return Conversions.deserialize(res.user)


oauth2_scheme_no_error: OAuth2PasswordBearer = OAuth2PasswordBearer(
    tokenUrl="auth/login",
    scopes={
        "me": "Read information about the current user.",
        "items": "Read items.",
    },
    auto_error=False,
)


async def get_current_token_or_none(
    token: Annotated[str, Depends(oauth2_scheme_no_error)],
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
    if token is None:
        return False
    req = CheckRequest(token=token)
    res = await auth.check(req)
    return res.status


@router.post("/login", description="Performs the login")
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    host: GetHost,
    session: GetSession,
    auth: Auth,
):
    req = LoginRequest(
        username=form_data.username, password=form_data.password, host=host
    )
    res = await auth.login(req)
    if res.status == False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": res.token, "token_type": "bearer"}


@router.get(
    "/logout",
    description="Performs the logout",
    response_model=bool,
)
async def logout(host: GetHost, token: TokenOrNone, session: GetSession, auth: Auth):
    req = LogoutRequest(token=token)
    res = await auth.logout(res)
    return res.status
class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str
    name: str = ""

@router.put("/register", response_model=bool)
async def register(req: RegisterRequest, auth: Auth):
    # return await auth.register(req.username, req.email, req.password)

    req = RpcRegisterRequest(
        username=req.usernamer, password=req.password, email=req.email
    )
    res = await auth.register(req)
    if res.status == False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(res.message),
            headers={"WWW-Authenticate": "Bearer"},
        )
    return res.status


@router.post("/unregister", response_model=bool)
async def unregister(token: TokenOrNone, auth: Auth):
    req = UnregisterRequest(token=token)
    res = await auth.unregister(req)
    if res.status == False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(res.message),
            headers={"WWW-Authenticate": "Bearer"},
        )
    return res.status


@router.post("/password/reset", response_model=bool)
async def password_reset(
    old: str, new: str, token: TokenOrNone, host: GetHost, auth: Auth
):
    req = ResetPasswordRequest(token=token, host=host, old=old, new=new)
    res = await auth.resetPassword(req)
    if res.status == False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(res.message),
            headers={"WWW-Authenticate": "Bearer"},
        )
    return res.status
