# LOCAL IMPORTS

from typing import Optional, Tuple

from beanie import PydanticObjectId
from common.rpc.storage_pb2 import StorageExistsRequest, StorageExistsResponse, StorageLoadByIdRequest, StorageLoadByIdResponse, StorageLoadRequest, StorageLoadResponse, StorageRemoveFolderRequest, StorageRemoveFolderResponse, StorageRemoveRequest, StorageRemoveResponse, StorageSaveRequest, StorageSaveResponse
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
        
    async def save(self,filename:str,folder:str,data:bytes,content_type:Optional[str]=None) -> PydanticObjectId:
        req = StorageSaveRequest(filename=filename,folder=folder,data=data,content_type=content_type)
        res: StorageSaveResponse = await self.client.storageSave(req)
        if res.status==False:
            raise Exception(res.message)
        return PydanticObjectId(res.id)
    
    async def load(self,filename:str,folder:str) -> Tuple[bytes,str,int]:
        req = StorageLoadRequest(filename=filename,folder=folder)
        res: StorageLoadResponse = await self.client.storageLoad(req)
        if res.status == False:
            raise Exception(res.message)
        return res.data,res.content_type,res.size
    
    async def loadById(self,id:PydanticObjectId) -> Tuple[bytes,str,int]:
        req = StorageLoadByIdRequest(id=str(id))
        res: StorageLoadByIdResponse = await self.client.storageLoadById(req)
        if res.status == False:
            raise Exception(res.message)
        return res.data,res.content_type,res.size
    
    async def remove(self,filename:str,folder:str) -> bool:
        req = StorageRemoveRequest(filename=filename,folder=folder)
        res: StorageRemoveResponse = await self.client.storageRemove(req)
        if res.status == False:
            raise Exception(res.message)
        return res.status
    
    async def exists(self,filename:str,folder:str) -> bool:
        req = StorageExistsRequest(filename=filename,folder=folder)
        res: StorageExistsResponse = await self.client.storageExists(req)
        if res.status == False:
            raise Exception(res.message)
        return res.exists
    
    async def removeFolder(self,folder:str)-> bool:
        req = StorageRemoveFolderRequest(folder=folder)
        res: StorageRemoveFolderResponse = await self.client.storageRemoveFolder(req)
        if res.status == False:
            raise Exception(res.message)
        return res.status
