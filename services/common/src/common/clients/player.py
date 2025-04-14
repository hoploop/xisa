
# PYTHON IMPORTS
import logging

from beanie import PydanticObjectId

from common.models.auth import User
from common.rpc.base_pb2 import Ping, Pong
from common.rpc.player_pb2 import PlayerRawScriptExecuteRequest, PlayerRawScriptExecuteResponse, PlayerScriptExecuteRequest, PlayerScriptExecuteResponse, PlayerScriptGenerateRequest, PlayerScriptGenerateResponse, PlayerScriptUpdateRequest, PlayerScriptUpdateResponse
from common.rpc.player_pb2_grpc import PlayerStub
from common.service import Client

# INITIALIZATION
log = logging.getLogger(__name__)


class PlayerClient(Client):

    def __init__(self, client_config):
        super().__init__(client_config)

    async def startup(self):
        await super().startup()
        self.client = PlayerStub(self.channel)

    async def ping(self) -> Pong:
        req = Ping()
        res = await self.client.ping(req)
        return res
    
    async def playerScriptGenerate(self,user:User,recordId:PydanticObjectId,declarative:bool=True,synthetic:bool=False)-> str:
        req = PlayerScriptGenerateRequest(user=str(user.id),record=str(recordId),declarative=declarative,synthetic=synthetic)
        res: PlayerScriptGenerateResponse = await self.client.playerScriptGenerate(req)
        if res.status == False:
            raise Exception(res.message)
        return res.script
    
    async def playerScriptUpdate(self,user:User,recordId:PydanticObjectId,script:str)-> bool:
        req = PlayerScriptUpdateRequest(user=str(user.id),record=str(recordId),script=script)
        res: PlayerScriptUpdateResponse = await self.client.playerScriptUpdate(req)
        if res.status == False:
            raise Exception(res.message)
        return res.status
    
    async def playerScriptExecute(self,user:User,session:str,recordId:PydanticObjectId,declarative:bool=True,synthetic:bool=False)-> bool:
        req = PlayerScriptExecuteRequest(user=str(user.id),record=str(recordId),session=session)
        res: PlayerScriptExecuteResponse = await self.client.playerScriptExecute(req)
        if res.status == False:
            raise Exception(res.message)
        return res.status
    
    async def playerRawScriptExecute(self,user:User,session:str,script:str)-> bool:
        req = PlayerRawScriptExecuteRequest(user=str(user.id),script=script,session=session)
        res: PlayerRawScriptExecuteResponse = await self.client.playerRawScriptExecute(req)
        if res.status == False:
            raise Exception(res.message)
        return res.status