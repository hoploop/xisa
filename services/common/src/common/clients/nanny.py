# PYTHON IMPORTS
import logging

from pydantic import BaseModel

from common.rpc.base_pb2 import Ping, Pong
from common.rpc.nanny_pb2 import NannyStatusRequest, NannyStatusResponse
from common.rpc.nanny_pb2_grpc import NannyStub
from common.service import Client
from common.utils.conversions import Conversions

# INITIALIZATION
log = logging.getLogger(__name__)

class NannyClient(Client):
    
    def __init__(self, client_config):
        super().__init__(client_config)
        
            
    async def startup(self):
        await super().startup()
        self.client = NannyStub(self.channel)
        
    async def ping(self) -> Pong:
        req = Ping()
        res = await self.client.ping(req)
        return res
    
    async def nannyStatus(self) -> dict:
        req = NannyStatusRequest()
        res: NannyStatusResponse = await self.client.nannyStatus(req,timeout=2.0)
        ret = {}
        for el in res.services:
            ret[el.name] = el.status
        return ret
        