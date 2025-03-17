# PYTHON IMPORTS
import logging
from typing import Optional

# LOCAL IMPORTS
from common.models.auth import User
from common.rpc.auth_pb2 import CheckRequest, LoginRequest, LogoutRequest, RegisterRequest, ResetPasswordRequest, UnregisterRequest, UserRequest
from common.rpc.auth_pb2_grpc import AuthStub
from common.rpc.base_pb2 import Ping, Pong
from common.service import Client
from common.utils.conversions import Conversions

# INITIALIZATION
log = logging.getLogger(__name__)

class AuthClient(Client):
    
    def __init__(self, client_config):
        super().__init__(client_config)
        self.client = AuthStub(self.channel)
        
    async def ping(self) -> Pong:
        req = Ping()
        res = await self.client.ping(req)
        return res
        
    async def user(self,token:str) -> Optional[User]:
        req = UserRequest(token=token)
        res = await self.client.user(req)
        if res.status == False:
            return None
        return Conversions.deserialize(res.user)
    

    async def check(self,token:str) -> bool:
        if token is None:
            return False
        req = CheckRequest(token=token)
        res = await self.client.check(req)
        return res.status
    
    async def login(self,username:str,password:str,host:str) -> Optional[str]:
        req = LoginRequest(username=username, password=password, host=host)
        res = await self.client.login(req)
        if res.status == False:
            return None
        return res.token
    
    async def logout(self,token:str) -> bool:
        req = LogoutRequest(token=token)
        res = await self.client.logout(req)
        return res.status
    
    async def register(self,username:str,email:str,password:str) -> bool:
        req = RegisterRequest(username=req.usernamer, password=req.password, email=req.email)
        res = await self.client.register(req)
        if res.status == False:
            raise Exception(str(res.message))
        return res.status
    
    async def unregister(self,token:str) -> bool:
        req = UnregisterRequest(token=token)
        res = await self.client.unregister(req)
        if res.status == False:
            raise Exception(res.message)
        return res.status
    
    
    async def resetPassword(self,host:str,token:str,old:str,new: str) -> bool:
        req = ResetPasswordRequest(token=token, host=host, old=old, new=new)
        res = await self.client.resetPassword(req)
        if res.status == False:
            raise Exception(res.message)
        return res.status
    