
# PYTHON IMPORTS
import logging

from beanie import PydanticObjectId

from common.models.auth import User
from common.rpc.base_pb2 import Ping, Pong
from common.rpc.player_pb2 import PlayerScriptGenerateRequest, PlayerScriptGenerateResponse
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