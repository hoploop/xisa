
# PYTHON IMPORTS
import logging

# LOCAL IMPORTS
from common.models.auth import User
from common.rpc.base_pb2 import Ping, Pong
from common.rpc.operator_pb2 import Answer, Question
from common.rpc.operator_pb2_grpc import OperatorStub
from common.service import Client

# INITIALIZATION
log = logging.getLogger(__name__)


class OperatorClient(Client):

    def __init__(self, client_config):
        super().__init__(client_config)

    async def startup(self):
        await super().startup()
        self.client = OperatorStub(self.channel)

    async def ping(self) -> Pong:
        req = Ping()
        res = await self.client.ping(req)
        return res
    
    async def ask(self,user:User,session:str,message:str) -> str:
        req = Question(user=str(user.id),session=session,message=message)
        res: Answer = await self.client.ask(req)
        if res.status == False:
            raise Exception(res.message)
        return res.text
    