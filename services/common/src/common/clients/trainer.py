# PYTHON IMPORTS
import logging
from typing import List, Optional, Tuple

from beanie import PydanticObjectId

# LOCAL IMPORTS
from common.models.auth import User
from common.models.trainer import TrainImageObject
from common.rpc.base_pb2 import Ping, Pong
from common.rpc.trainer_pb2 import  TrainImageObjectCountByDetectorRequest, TrainImageObjectCountByDetectorResponse, TrainImageObjectListRequest, TrainImageObjectListResponse, TrainImageObjectRemoveRequest, TrainImageObjectRemoveResponse, TrainImageObjectRequest, TrainImageObjectResponse, TrainImageObjectToDetectorRequest, TrainImageObjectToDetectorResponse, TrainImageObjectUpdateRequest, TrainImageObjectUpdateResponse
from common.rpc.trainer_pb2_grpc import TrainerStub
from common.service import Client
from common.utils.conversions import Conversions

# INITIALIZATION
log = logging.getLogger(__name__)

class TrainerClient(Client):
    
    def __init__(self, client_config):
        super().__init__(client_config)
        
    async def startup(self):
        await super().startup()
        self.client = TrainerStub(self.channel)
        
    async def ping(self) -> Pong:
        req = Ping()
        res = await self.client.ping(req)
        return res
    
    
    async def trainImageObject(self,user:User,detectorId:PydanticObjectId,recordId:PydanticObjectId,frame:int,labels:List[str],xstart:float,xend:float,ystart:float,yend:float,train:bool,test:bool,val:bool) -> TrainImageObject:
        req = TrainImageObjectRequest(user=str(user.id),record=str(recordId),detector=str(detectorId),frame=frame,labels=labels,xstart=xstart,xend=xend,ystart=ystart,yend=yend,train=train,test=test,val=val)
        res: TrainImageObjectResponse = await self.client.trainImageObject(req)
        if res.status == False:
            raise Exception(res.message)
        return Conversions.deserialize(res.object)
    
    async def trainImageObjectList(self,user:User,detectorId:PydanticObjectId,recordId:PydanticObjectId,frame:int=-1) -> Tuple[int,List[TrainImageObject]]:
        req = TrainImageObjectListRequest(user=str(user.id),record=str(recordId),detector=str(detectorId),frame=frame)
        res: TrainImageObjectListResponse = await self.client.trainImageObjectList(req)
        if res.status == False:
            raise Exception(res.message)
        total = res.total
        ret = []
        for obj in res.objects:
            ret.append(Conversions.deserialize(obj))
        return total,ret
    
    
    async def trainImageObjectRemove(self,user:User,objectId:PydanticObjectId) -> bool:
        req = TrainImageObjectRemoveRequest(user=str(user.id),id=str(objectId))
        res: TrainImageObjectRemoveResponse = await self.client.trainImageObjectRemove(req)
        if res.status == False:
            raise Exception(res.message)
        return res.status
    
    
    async def trainImageObjectUpdate(self,user:User,imageObjectId:PydanticObjectId,labels:List[str],val:bool,test:bool,train:bool,xstart:float,xend:float,ystart:float,yend:float) -> bool:
        req = TrainImageObjectUpdateRequest(user=str(user.id),id=str(imageObjectId),labels=labels,val=val,test=test,train=train,xstart=xstart,xend=xend,ystart=ystart,yend=yend)
        res: TrainImageObjectUpdateResponse = await self.client.trainImageObjectUpdate(req)
        if res.status == False:
            raise Exception(res.message)
        return res.status
    
    async def trainImageObjectCountByDetector(self,user:User,detectorId:PydanticObjectId) -> int:
        req = TrainImageObjectCountByDetectorRequest(user=str(user.id),detector=str(detectorId))
        res: TrainImageObjectCountByDetectorResponse = await self.client.trainImageObjectCountByDetector(req)
        if res.status == False:
            raise Exception(res.message)
        return res.total
    
    async def trainImageObjectToDetector(self,user:User,detectorId:PydanticObjectId) -> int:
        req = TrainImageObjectToDetectorRequest(user=str(user.id),detector=str(detectorId))
        res: TrainImageObjectToDetectorResponse = await self.client.trainImageObjectToDetector(req)
        if res.status == False:
            raise Exception(res.message)
        return res.total