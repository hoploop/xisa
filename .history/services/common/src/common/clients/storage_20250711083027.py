# LOCAL IMPORTS

from typing import Optional
from common.rpc.storage_pb2 import StorageSaveRequest, StorageSaveResponse
from common.rpc.storage_pb2_grpc import StorageStub
from common.service import Client

# INITIALIZATION
import logging



log = logging.getLogger(__name__)


class StorageClient(Client):

    def __init__(self, client_config):
        super().__init__(client_config)

    async def startup(self):
        await super().startup()
        self.client = StorageStub(self.channel)
        
    async def save(self,filename:str,folder:str,data:bytes,content_type:Optional[str]=None) -> str:
        req = StorageSaveRequest(filename=filename,folder=folder,data=data,content_type=content_type)
        res: StorageSaveResponse = await self.client.storageSave(req)
        if res.status==False:
            raise Exception(res.message)
        return res.id
    
    async def load(self,filename:str,folder:str)
