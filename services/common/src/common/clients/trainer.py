# PYTHON IMPORTS
import logging
from typing import Optional

from beanie import PydanticObjectId

# LOCAL IMPORTS
from common.models.auth import User
from common.models.train import TrainLesson
from common.rpc.auth_pb2 import CheckRequest, LoginRequest, LogoutRequest, RegisterRequest, ResetPasswordRequest, UnregisterRequest, UserRequest
from common.rpc.auth_pb2_grpc import AuthStub
from common.rpc.base_pb2 import Ping, Pong
from common.rpc.trainer_pb2 import LessonSetDetectorRequest, LessonSetDetectorResponse, RecordCreateLessonRequest, RecordCreateLessonResponse, RecordHasLessonRequest, RecordHasLessonResponse
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
    
    async def recordHasLesson(self,user:User,recordId:PydanticObjectId) -> Optional[TrainLesson]:
        req = RecordHasLessonRequest(user=str(user.id),record=str(recordId))
        res: RecordHasLessonResponse = await self.client.recordHasLesson(req)
        
        if res.status == False:
            raise Exception(res.message)
        
        return Conversions.deserialize(res.lesson)
        

    async def recordCreateLesson(self,user:User,recordId:PydanticObjectId) -> TrainLesson:
        req = RecordCreateLessonRequest(user=str(user.id),record=str(recordId))
        res: RecordCreateLessonResponse = await self.client.recordCreateLesson(req)
        if res.status == False:
            raise Exception(res.message)
        return Conversions.deserialize(res.lesson)
        
    
    async def lessonSetDetector(self,user:User,lessonId:PydanticObjectId,detectorId:PydanticObjectId) -> TrainLesson:
        
        req = LessonSetDetectorRequest(user=str(user.id),lesson=str(lessonId),detector=str(detectorId))
        res: LessonSetDetectorResponse = await self.client.lessonSetDetector(req)
        if res.status == False:
            raise Exception(res.message)
        
        return Conversions.deserialize(res.lesson)