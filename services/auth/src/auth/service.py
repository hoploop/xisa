# PYTHON IMPORTS
import logging

# LIBRARY IMPORTS
from pydantic import BaseModel

# LOCAL IMPORTS
from common.models import MODELS
from common.rpc.auth_pb2 import CheckRequest, CheckResponse, LoginRequest, LoginResponse, LogoutRequest, LogoutResponse, RegisterRequest, RegisterResponse, ResetPasswordRequest, ResetPasswordResponse, UnregisterRequest, UnregisterResponse, UserRequest, UserResponse
from common.service import Service
from common.service import ServiceConfig
from common.utils.conversions import Conversions
from common.utils.mongodb import Mongodb, MongodbConfig
from common.rpc.auth_pb2_grpc import AuthServicer
from common.models.auth import Token, User

# INITIALIZATION
log = logging.getLogger(__name__)


class AuthServiceConfig(ServiceConfig):
    database: MongodbConfig


class AuthService(Service, AuthServicer):

    def __init__(self, config: AuthServiceConfig):
        AuthServicer.__init__(self)
        Service.__init__(self)
        self.config: AuthServiceConfig = config
        self.USERS = {}
        self.TOKENS = {}
        
    async def start(self):
        await Mongodb.initialize(self.config.database,MODELS)
        
    async def user(self, request:UserRequest, context) -> UserResponse:
        try:
            if request.token in self.USERS:
                return UserResponse(status=True,user=Conversions.serialize(self.USERS[request.token]))
            else:
                token_doc = await Token.find_many(Token.code == request.token).first_or_none()
                if token_doc is None:
                    return UserResponse(status=False,message="Not logged in")
                    
                user_doc = await User.find_many(User.id == token_doc.user).first_or_none()
                if user_doc is None:
                    return UserResponse(status=False,message="Not logged in")
                    
                self.USERS[request.token] = user_doc
                return UserResponse(status=True,user=Conversions.serialize(user_doc))
        except Exception as e:
            log.warning(str(e))
            return UserResponse(status=False,message=str(e))
            
        
    async def check(self, request: CheckRequest, context) -> CheckResponse:
        try:
            if request.token is None:
                return CheckResponse(status=False)
            found = await Token.find_many(Token.code == request.token).first_or_none()
            if not found:
                return CheckResponse(status=False)
            return CheckResponse(status=True)
        except Exception as e:
            log.warning(str(e))
            return CheckResponse(status=False,message=str(e))


    async def login(self, request:LoginRequest,context) -> LoginResponse:
        try:
            user = await User.find_many(User.username == request.username).first_or_none()
            if user is None:
                return LoginResponse(status=False,message="Invalid authentication credentials")
                
            verified = await user.verify_password(request.password)
            if not verified:
                return LoginResponse(status=False,message="Invalid authentication credentials")
                

            token_doc = Token(user=user.id, host=request.host)
            await token_doc.insert()
            self.USERS[token_doc.code] = user
            self.TOKENS[token_doc.code] = token_doc

            return LoginResponse(status=True,token=token_doc.code)
        except Exception as e:
            log.warning(str(e))
            return LoginResponse(status=False,message=str(e))

    async def logout(self, request:LogoutRequest,context) -> LogoutResponse:
        try:
            if request.token is None:
                return LogoutResponse(status=False)
            await Token.find_many(Token.code == request.token).delete()
            if request.token in self.USERS:
                del self.USERS[request.token]
            if request.token in self.TOKENS:
                del self.TOKENS[request.token]
            return LogoutResponse(status=True)
        except Exception as e:
            log.warning(str(e))
            return LogoutResponse(status=False,message=str(e))

    async def register(self,request: RegisterRequest, context) -> RegisterResponse:
        try:
            user = await User.find_one(User.username == request.username)

            if user is None:
                log.debug("Creating user: {0}".format(request.username))
                user = User(
                    username=request.username,
                    email=request.email,
                    password=request.password,
                    full_name=request.username,
                )
                await User.insert_one(user)
                return RegisterResponse(status=True)
            return RegisterResponse(status=False,message="User already exists")
        except Exception as e:
            log.warning(str(e))
            return RegisterResponse(status=False,message=str(e))


    async def unregister(self, request:UnregisterRequest,context) -> UnregisterResponse:
        try:
            log.debug("Unregistering")
            token_doc = await Token.find_many(Token.code == request.token).first_or_none()
            if token_doc is None:
                return False
            await User.find(User.id == token_doc.user).delete()
            await token_doc.delete()
            if request.token in self.TOKENS:
                del self.TOKENS[request.token]
            if request.token in self.USERS:
                del self.USERS[request.token]
            return UnregisterResponse(status=True)
        except Exception as e:
            log.warning(str(e))
            return UnregisterResponse(status=False,message=str(e))
        
    async def resetPassword(self, request: ResetPasswordRequest, context) -> ResetPasswordResponse:
        try:
            token_doc = await Token.find_many(Token.code == request.token, Token.host == request.host).first_or_none()
            if token_doc is None:
                return ResetPasswordResponse(status=False)
            user = await User.find_many(User.id == token_doc.user).first_or_none()
            if user is None:
                return ResetPasswordResponse(status=False)
            verified = await user.verify_password(request.old)
            if not verified:
                return ResetPasswordResponse(status=False)
            user.password = request.new
            await user.save()
            return ResetPasswordResponse(status=True)
        except Exception as e:
            log.warning(str(e))
            return ResetPasswordResponse(status=False,message=str(e))
        