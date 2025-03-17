# PYTHON IMPORTS
import logging
from typing import List, Optional, Tuple

from beanie import PydanticObjectId

# LOCAL IMPORTS
from common.models.auth import User
from common.models.recorder import Record
from common.rpc.base_pb2 import Ping, Pong
from common.rpc.recorder_pb2 import CountRecordRequest, DeleteRecordRequest, ListRecordRequest, LoadRecordRequest, RunningRequest, UpdateRecordRequest
from common.rpc.recorder_pb2_grpc import RecorderStub
from common.service import Client
from common.utils.conversions import Conversions


# INITIALIZATION
log = logging.getLogger(__name__)

class RecorderClient(Client):
    
    def __init__(self, client_config):
        super().__init__(client_config)
        self.client = RecorderStub(self.channel)
        
    async def ping(self) -> Pong:
        req = Ping()
        res = await self.client.ping(req)
        return res
    
    
    async def running(self)-> bool:
        req = RunningRequest()
        res = await self.client.running(req)
        return res.status
    
    async def loadRecord(self,user:User,recorderId:PydanticObjectId) -> Optional[Record]:
        req = LoadRecordRequest(user=str(user.id),id=str(recorderId))
        res = await self.client.loadRecord(req)
        if res.status == False:
            raise Exception(res.message)
        return Conversions.deserialize(res.record)
        
    async def updateRecord(self,user:User,recorderId:PydanticObjectId,name:str,description:str) -> Optional[Record]:
        req = UpdateRecordRequest(user=str(user.id),id=str(recorderId),name=name,description=description)
        res = await self.client.updateRecord(req)
        if res.status == False:
            raise Exception(res.message)
        return Conversions.deserialize(res.record)
    
    async def listRecord(self,user:User,projectId:PydanticObjectId,skip:int, limit:int,search:str) -> Tuple[int,List[Record]]:
        req = ListRecordRequest(user=str(user.id),project=str(projectId),skip=skip,limit=limit,search=search)
        res = await self.client.listRecord(req)
        if res.status == False:
            raise Exception(res.message)
        total = res.total
        ret = []
        for record in res.records:
            ret.append(Conversions.deserialize(record))
        return total,ret
    
    async def deleteRecord(self,user:User,recordId:PydanticObjectId) -> bool:
        req = DeleteRecordRequest(user=str(user.id),record=str(recordId))
        res = await self.client.deleteRecord(req)
        if res.status == False:
            raise Exception(res.message)
        return res.status
    
    async def countRecord(self,user:User,projectId:PydanticObjectId) -> int:
        req = CountRecordRequest(user=str(user.id),project=str(projectId))
        res = await self.client.countRecord(req)
        if res.status == False:
            raise Exception(res.message)
        return res.total