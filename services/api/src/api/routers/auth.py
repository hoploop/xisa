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


async def get_auth(request: Request) -> AuthClient:
    if not hasattr(request.app.state, "auth"):
        config = request.app.state.config.auth
        request.app.state.auth = AuthClient(config)
        await request.app.state.auth.startup()
    return request.app.state.auth


Auth = Annotated[AuthClient, Depends(get_auth)]

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
    user = await auth.user(token)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not logged in",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


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
    operation_id="authCheck",
    description="Checks the current token",
    response_model=bool,
)
async def check(host: GetHost, token: TokenOrNone, session: GetSession, auth: Auth):
    return await auth.check(token)


@router.post("/login", 
             operation_id="authLogin",
             description="Performs the login")
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    host: GetHost,
    session: GetSession,
    auth: Auth,
):
    token = await auth.login(form_data.username,form_data.password,host)
    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": token, "token_type": "bearer"}


@router.get(
    "/logout",
    operation_id="authLogout",
    description="Performs the logout",
    response_model=bool,
)
async def logout(host: GetHost, token: TokenOrNone, session: GetSession, auth: Auth):
    return await auth.logout(token)
    

class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str
    name: str = ""

@router.put("/register", 
            operation_id="authRegister",
            response_model=bool)
async def register(req: RegisterRequest, auth: Auth):
    # return await auth.register(req.username, req.email, req.password)
    try:
        return await auth.register(req.username,req.email,req.password)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )
    


@router.post("/unregister", 
             operation_id="authUnregister",
             response_model=bool)
async def unregister(token: TokenOrNone, auth: Auth):
    try:
        return await auth.unregister(token)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )
    


@router.post("/password/reset", 
             operation_id="authPasswordReset",
             response_model=bool)
async def password_reset(
    old: str, new: str, token: TokenOrNone, host: GetHost, auth: Auth
):
    try:
        return await auth.resetPassword(host,token,old,new)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    