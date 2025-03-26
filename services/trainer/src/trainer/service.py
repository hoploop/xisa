# PYTHON IMPORTS
import logging

from beanie import PydanticObjectId

# LIBRARY IMPORTS

# LOCAL IMPORTS
from common.models import MODELS
from common.models.detector import Detector
from common.models.train import TrainLesson
from common.rpc.trainer_pb2 import LessonSetDetectorRequest, LessonSetDetectorResponse, RecordCreateLessonRequest, RecordCreateLessonResponse, RecordHasLessonRequest, RecordHasLessonResponse
from common.rpc.trainer_pb2_grpc import TrainerServicer
from common.service import Service
from common.service import ServiceConfig
from common.utils.conversions import Conversions
from common.utils.mongodb import Mongodb, MongodbConfig

# INITIALIZATION
log = logging.getLogger(__name__)
RECORDS = {}

class TrainerServiceConfig(ServiceConfig):
    database: MongodbConfig

class TrainerService(Service, TrainerServicer):

    def __init__(self, config: TrainerServiceConfig):
        TrainerServicer.__init__(self)
        Service.__init__(self)
        self.config:TrainerServiceConfig = config
    
        
    async def start(self):
         await Mongodb.initialize(self.config.database,MODELS)
         
    async def recordHasLesson(self, request: RecordHasLessonRequest, context) -> RecordHasLessonResponse:
        try:
            found = await TrainLesson.find_many(TrainLesson.record == PydanticObjectId(request.record)).first_or_none()
            if not found:
                found = await TrainLesson(record=PydanticObjectId(request.record)).insert()
            return RecordHasLessonResponse(status=True,lesson=Conversions.serialize(found))
            
        except Exception as e:
            log.warning(str(e))
            return RecordHasLessonResponse(status=False,message=str(e))
        
    async def recordCreateLesson(self, request: RecordCreateLessonRequest, context) -> RecordCreateLessonResponse:
        try:
            lesson = await TrainLesson(record=PydanticObjectId(request.record)).insert()
            return RecordHasLessonRequest(status=True,lesson=Conversions.serialize(lesson))
        except Exception as e:
            log.warning(str(e))
            return RecordCreateLessonResponse(status=False,message=str(e))
        
    async def lessonSetDetector(self, request: LessonSetDetectorRequest, context) -> LessonSetDetectorResponse:
        
        try:
            lesson = await TrainLesson.find_many(TrainLesson.id == PydanticObjectId(request.lesson)).first_or_none()
            detector = await Detector.find_many(Detector.id == PydanticObjectId(request.detector)).first_or_none()
            if lesson is None:
                return LessonSetDetectorResponse(status=False,message="workspace.trainer.lesson.errors.not_found")
            if detector is None:
                return LessonSetDetectorResponse(status=False,message="workspace.detector.errors.not_found")
            lesson.detector= str(detector.id)
            await lesson.save()
            return LessonSetDetectorResponse(status=True,lesson=Conversions.serialize(lesson))
        except Exception as e:
            log.warning(str(e))
            return RecordCreateLessonResponse(status=False,message=str(e))
    