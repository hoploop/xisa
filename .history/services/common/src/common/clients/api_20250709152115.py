# PYTHON IMPORTS
import logging

from pydantic import BaseModel

from common.rpc.api_pb2 import NannyUpdateRequest, NannyUpdateResponse, UpdateSessionRequest
from common.rpc.api_pb2_grpc import ApiStub
from common.rpc.base_pb2 import Ping, Pong
from common.service import Client
from common.utils.conversions import Conversions

# INITIALIZATION
log = logging.getLogger(__name__)

class ApiClient(Client):
    
    def __init__(self, client_config):
        super().__init__(client_config)
        
            
    async def startup(self):
        await super().startup()
        self.client = ApiStub(self.channel)
        
    async def ping(self) -> Pong:
        req = Ping()
        res = await self.client.ping(req)
        return res
    
    async def updateSession(self,session:str,document: BaseModel) -> bool:
        req = UpdateSessionRequest(session=session,document=Conversions.serialize(document))
        res = await self.client.updateSession(req)
        return res.status
    
    async def nannyUpdate(self,service:str,status:bool) -> bool:
        try:
            req = NannyUpdateRequest(service=service,status=status)
            res: NannyUpdateResponse = await self.client.nannyUpdate(req)
            return res.status
        except Exception as e:
            log.warning(str(e))
        finally:
            return Trye