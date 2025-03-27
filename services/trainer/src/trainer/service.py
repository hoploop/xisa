# PYTHON IMPORTS
import logging

from beanie import PydanticObjectId

# LIBRARY IMPORTS

# LOCAL IMPORTS
from common.models import MODELS
from common.models.detector import Detector, DetectorLabel
from common.models.train import TrainImageObject, TrainLesson
from common.rpc.trainer_pb2 import LessonSetDetectorRequest, LessonSetDetectorResponse, RecordCreateLessonRequest, RecordCreateLessonResponse, RecordHasLessonRequest, RecordHasLessonResponse, TrainImageObjectRequest, TrainImageObjectResponse
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
        
    async def trainImageObject(self, request:TrainImageObjectRequest, context) -> TrainImageObjectResponse:
        try:
            lesson = await TrainLesson.find_many(TrainLesson.id == PydanticObjectId(request.lesson)).first_or_none()
            if lesson is None:
                return TrainImageObjectResponse(status=False,message="workspace.trainer.lesson.errors.not_found")
            detectorId = lesson.detector
            detector = await Detector.find_many(Detector.id == PydanticObjectId(lesson.detector)).first_or_none()
            if detector is None:
                return TrainImageObjectResponse(status=False,message="workspace.detector.errors.not_found")
            
            class_id = None
            class_name = request.label
            found_class = await DetectorLabel.find_many(
                DetectorLabel.detector == detectorId, DetectorLabel.name == class_name
            ).first_or_none()
            if found_class is None:
                found_class = await DetectorLabel(
                    detector=detectorId, name=class_name
                ).insert()
            class_id = found_class.id
            
            tio = await TrainImageObject(
                frame=request.frame,
                label=class_id,
                xstart=request.xstart,
                xend=request.xend,
                ystart=request.ystart,
                yend=request.yend,
            ).insert()
            user_id = PydanticObjectId(request.user)
            return TrainImageObjectResponse(status=True,id=str(tio.id))
        except Exception as e:
            log.warning(str(e))
            return TrainImageObjectResponse(status=False,message=str(e))
    