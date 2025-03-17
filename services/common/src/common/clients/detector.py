
# PYTHON IMPORTS
import logging
from typing import List, Tuple

from beanie import PydanticObjectId

# LIBRARY IMPORTS

# LOCAL IMPORTS

from common.models.auth import User
from common.models.detector import Detector, DetectorClass, DetectorImage, DetectorImageLabel, DetectorImageMode
from common.rpc.base_pb2 import Ping, Pong
from common.rpc.detector_pb2 import AddDetectorImageLabelRequest, CountDetectorClassRequest, CountDetectorImageLabelRequest, CountDetectorImageRequest, CountDetectorRequest, CreateDetectorRequest, ListDetectorClassRequest, ListDetectorImageLabelRequest, ListDetectorImageRequest, ListDetectorRequest, LoadDetectorRequest, RemoveDetectorImageLabelRequest, RemoveDetectorImageRequest, RemoveDetectorRequest, TrainDetectorRequest, UpdateDetectorRequest, UploadDetectorImageRequest
from common.rpc.detector_pb2_grpc import DetectorStub
from common.service import Client
from common.utils.conversions import Conversions

# INITIALIZATION
log = logging.getLogger(__name__)

class DetectorClient(Client):
    
    def __init__(self, client_config):
        super().__init__(client_config)
        self.client = DetectorStub(self.channel)
        
    async def ping(self) -> Pong:
        req = Ping()
        res = await self.client.ping(req)
        return res
    
    async def listDetector(self,user:User,projectId:PydanticObjectId,skip:int,limit:int,search:str)-> Tuple[int,List[Detector]]:
        req = ListDetectorRequest(user=str(user.id),project=str(projectId),skip=skip,limit=limit,search=search)
        res = await self.client.listDetector(req)
        if res.status == False:
            raise Exception(res.message)
        total = res.total
        ret = []
        for detector in res.detectors:
            ret.append(Conversions.deserialize(detector))
        return total,detector
    
    async def countDetector(self,user:User,projectId:PydanticObjectId)-> int:
        req = CountDetectorRequest(user=str(user.id),project=str(projectId))
        res = await self.client.countDetector(req)
        if res.status == False:
            raise Exception(res.message)
        return res.total
    
    async def updateDetector(self,user:User,detectorId:PydanticObjectId,name:str,description:str)-> Detector:
        req = UpdateDetectorRequest(user=str(user.id),id=str(detectorId),name=name,description=description)
        res = await self.client.updateDetector(req)
        if res.status == False:
            raise Exception(res.message)
        return Conversions.deserialize(res.detector)
    
    async def loadDetector(self,user:User,detectorId:PydanticObjectId)-> Detector:
        req = LoadDetectorRequest(user=str(user.id),id=str(detectorId))
        res = await self.client.loadDetector(req)
        if res.status == False:
            raise Exception(res.message)
        return Conversions.deserialize(res.detector)
        
        
    async def createDetector(self,user:User,projectId:PydanticObjectId,name:str,description:str,origin:str=None) -> Detector:
        req = CreateDetectorRequest(user=str(user.id),project=str(projectId),name=name,description=description,origin=origin)
        res = await self.client.createDetector(req)
        if res.status == False:
            raise Exception(res.message)
        return Conversions.deserialize(res.detector)
    
    async def trainDetector(self,user:User,detectorId:PydanticObjectId,session:str,epochs:int,image_size:int):
        req = TrainDetectorRequest(user=str(user.id),session=session,detector=str(detectorId),epochs=epochs,imageSize=image_size)
        res = await self.client.trainDetector(req)
        if res.status == False:
            raise Exception(res.message)
        return res.status
    
    async def listDetectorImage(self,user:User,detectorId:PydanticObjectId,skip:int,limit:int)-> Tuple[int,List[DetectorImage]]:
        req = ListDetectorImageRequest(user=str(user.id),detector=str(detectorId),skip=skip,limit=limit)
        res = await self.client.listDetectorImage(req)
        if res.status == False:
            raise Exception(res.message)
        total = res.total
        ret = []
        for image in res.images:
            ret.append(Conversions.deserialize(image))
        return total,ret
    
     
    async def countDetectorImage(self,user:User,detectorId:PydanticObjectId,skip:int,limit:int)-> int:
        req = CountDetectorImageRequest(user=str(user.id),detector=str(detectorId))
        res = await self.client.countDetectorImage(req)
        if res.status == False:
            raise Exception(res.message)
        return res.total
    
    async def removeDetectorImage(self,user:User,imageId:PydanticObjectId)-> bool:
        req = RemoveDetectorImageRequest(user=str(user.id),id=str(imageId))
        res = await self.client.removeDetectorImage(req)
        if res.status == False:
            raise Exception(res.message)
        return res.status
    
    async def removeDetector(self,user:User,detectorId:PydanticObjectId)-> bool:
        req = RemoveDetectorRequest(user=str(user.id),id=str(detectorId))
        res = await self.client.removeDetector(req)
        if res.status == False:
            raise Exception(res.message)
        return res.total
    
    async def addDetectorImageLabel(self,user:User,imageId:PydanticObjectId,xstart:float,xend:float,ystart:float,yend:float,classes:List[str])-> DetectorImageLabel:
        req = AddDetectorImageLabelRequest(user=str(user.id),image=str(imageId),xstart=xstart,xend=xend,ystart=ystart,yend=yend,classes=classes)
        res = await self.client.addDetectorImageLabel(req)
        if res.status == False:
            raise Exception(res.message)
        return Conversions.deserialize(res.label)
    
    async def uploadDetectorImage(self,user:User,detectorId:PydanticObjectId,data:str,modes:List[DetectorImageMode])-> List[DetectorImage]:
        req = UploadDetectorImageRequest(user=str(user.id),detector=str(detectorId),data=data,modes=modes)
        res = await self.client.uploadDetectorImage(req)
        if res.status == False:
            raise Exception(res.message)
        ret = []
        for image in res.images:
            ret.append(Conversions.deserialize(image))
        return ret
        
    async def listDetectorImageLabel(self,user:User,imageId:PydanticObjectId,skip:int,limit:int,search:str)-> Tuple[int,List[DetectorImageLabel]]:
        req = ListDetectorImageLabelRequest(user=str(user.id),image=str(imageId),skip=skip,limit=limit,search=search)
        res = await self.client.listDetectorImageLabel(req)
        if res.status == False:
            raise Exception(res.message)
        ret = []
        total = res.total
        for label in res.labels:
            ret.append(Conversions.deserialize(label))
        return total,ret
    
    async def listDetectorClass(self,user:User,detectorId:PydanticObjectId,skip:int,limit:int,search:str)-> Tuple[int,List[DetectorClass]]:
        req = ListDetectorClassRequest(user=str(user.id),detector=str(detectorId),skip=skip,limit=limit,search=search)
        res = await self.client.listDetectorClass(req)
        if res.status == False:
            raise Exception(res.message)
        ret = []
        total = res.total
        for clazz in res.classes:
            ret.append(Conversions.deserialize(clazz))
        return total,ret
    
    async def countDetectorClass(self,user:User,detectorId:PydanticObjectId)-> int:
        req = CountDetectorClassRequest(user=str(user.id),detector=str(detectorId))
        res = await self.client.countDetectorClass(req)
        if res.status == False:
            raise Exception(res.message)
        return res.total
    
    async def removeDetectorImageLabel(self,user:User,labelId:PydanticObjectId)-> bool:
        req = RemoveDetectorImageLabelRequest(user=str(user.id),label=str(labelId))
        res = await self.client.removeDetectorImageLabel(req)
        if res.status == False:
            raise Exception(res.message)
        return res.status
    
    async def countDetectorImageLabel(self,user:User,imageId:PydanticObjectId) -> int:
        req = CountDetectorImageLabelRequest(user=str(user.id),image=str(imageId))
        res = await self.client.countDetectorImageLabel(req)
        if res.status == False:
            raise Exception(res.message)
        return res.total