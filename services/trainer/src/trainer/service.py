# PYTHON IMPORTS
import logging


# LIBRARY IMPORTS
from beanie import PydanticObjectId
from beanie.operators import And, Or

# LOCAL IMPORTS
from common.clients.auth import AuthClient
from common.clients.detector import DetectorClient
from common.clients.recorder import RecorderClient
from common.models import MODELS
from common.models.auth import User
from common.models.detector import Detector, DetectorImageMode, DetectorLabel
from common.models.trainer import TrainImageObject, TrainLesson
from common.rpc.trainer_pb2 import LessonSetDetectorRequest, LessonSetDetectorResponse, LessonSetObjectConfidenceRequest, LessonSetObjectConfidenceResponse, LessonSetTextConfidenceRequest, LessonSetTextConfidenceResponse, RecordCreateLessonRequest, RecordCreateLessonResponse, RecordHasLessonRequest, RecordHasLessonResponse, TrainImageObjectCountByDetectorRequest, TrainImageObjectCountByDetectorResponse, TrainImageObjectListRequest, TrainImageObjectListResponse, TrainImageObjectRemoveRequest, TrainImageObjectRemoveResponse, TrainImageObjectRequest, TrainImageObjectResponse, TrainImageObjectToDetectorRequest, TrainImageObjectToDetectorResponse, TrainImageObjectUpdateRequest, TrainImageObjectUpdateResponse
from common.rpc.trainer_pb2_grpc import TrainerServicer
from common.service import ClientConfig, Service
from common.service import ServiceConfig
from common.utils.conversions import Conversions
from common.utils.mongodb import Mongodb, MongodbConfig

# INITIALIZATION
log = logging.getLogger(__name__)
RECORDS = {}

class TrainerServiceConfig(ServiceConfig):
    database: MongodbConfig
    detector: ClientConfig
    auth: ClientConfig
    recorder:ClientConfig

class TrainerService(Service, TrainerServicer):

    def __init__(self, config: TrainerServiceConfig):
        TrainerServicer.__init__(self)
        Service.__init__(self)
        self.config:TrainerServiceConfig = config
        self.detector: DetectorClient = DetectorClient(self.config.detector)
        self.auth: AuthClient = AuthClient(self.config.auth)
        self.recorder: RecorderClient = RecorderClient(self.config.recorder)
        
    async def start(self):
        await Mongodb.initialize(self.config.database,MODELS)
        await self.auth.startup()
        await self.detector.startup()
        await self.recorder.startup()
         
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
        
    async def lessonSetObjectConfidence(self, request:LessonSetObjectConfidenceRequest, context) ->LessonSetObjectConfidenceResponse:
        try:
            lesson = await TrainLesson.find_many(TrainLesson.id == PydanticObjectId(request.lesson)).first_or_none()
            if lesson is None:
                return LessonSetObjectConfidenceResponse(status=False,message="trainer.errors.lesson_not_found")
            lesson.objectConfidence = request.confidence
            await lesson.save()
            return LessonSetObjectConfidenceResponse(status=True,lesson=Conversions.serialize(lesson))
        except Exception as e:
            log.warning(str(e))
            return LessonSetObjectConfidenceResponse(status=False,message=str(e))
        
    async def lessonSetTextConfidence(self, request:LessonSetTextConfidenceRequest, context) -> LessonSetTextConfidenceResponse:
        try:
            lesson = await TrainLesson.find_many(TrainLesson.id == PydanticObjectId(request.lesson)).first_or_none()
            if lesson is None:
                return LessonSetTextConfidenceResponse(status=False,message="trainer.errors.lesson_not_found")
            lesson.textConfidence = request.confidence
            await lesson.save()
            return LessonSetTextConfidenceResponse(status=True,lesson=Conversions.serialize(lesson))
        except Exception as e:
            log.warning(str(e))
            return LessonSetTextConfidenceResponse(status=False,message=str(e))
        
        
    async def lessonSetDetector(self, request: LessonSetDetectorRequest, context) -> LessonSetDetectorResponse:
        
        try:
            lesson = await TrainLesson.find_many(TrainLesson.id == PydanticObjectId(request.lesson)).first_or_none()
            detector = await Detector.find_many(Detector.id == PydanticObjectId(request.detector)).first_or_none()
            if lesson is None:
                return LessonSetDetectorResponse(status=False,message="workspace.trainer.lesson.errors.not_found")
            if detector is None:
                return LessonSetDetectorResponse(status=False,message="workspace.detector.errors.not_found")
            lesson.detector= detector.id
            await lesson.save()
            return LessonSetDetectorResponse(status=True,lesson=Conversions.serialize(lesson))
        except Exception as e:
            log.warning(str(e))
            return RecordCreateLessonResponse(status=False,message=str(e))
        
    async def trainImageObjectList(self, request:TrainImageObjectListRequest, context) -> TrainImageObjectListResponse:
        try:
            lessonId = PydanticObjectId(request.lesson)
            qry = And(TrainImageObject.lesson == lessonId, TrainImageObject.archived == False)
            if request.frame and request.frame >=0:
                qry = And(TrainImageObject.lesson == lessonId, TrainImageObject.archived == False,TrainImageObject.frame == request.frame)
            tios = await TrainImageObject.find_many(qry).to_list()
            ret = []
            total = 0
            for tio in tios:
                total +=1
                ret.append(Conversions.serialize(tio))
            return TrainImageObjectListResponse(status=True,total=total,objects=ret)
        except Exception as e:
            log.warning(str(e))
            return TrainImageObjectListResponse(status=False,message=str(e))
        
    async def trainImageObjectRemove(self, request: TrainImageObjectRemoveRequest, context) -> TrainImageObjectRemoveResponse:
        try:
            found = await TrainImageObject.find_many(TrainImageObject.id == PydanticObjectId(request.id)).first_or_none()
            if not found:
                return TrainImageObjectRemoveResponse(status=False,message='workspace.trainer.lesson.errors.object_not_found')
            await found.delete()
            return TrainImageObjectRemoveResponse(status=True)
        except Exception as e:
            log.warning(str(e))
            return TrainImageObjectRemoveResponse(status=False,message=str(e))
        
    async def trainImageObjectCountByDetector(self, request: TrainImageObjectCountByDetectorRequest, context) -> TrainImageObjectCountByDetectorResponse:
        try:
            detectorId= PydanticObjectId(request.detector)
            log.debug('Finding lesson by detector: '+str(detectorId))
            total = 0
            async for lesson in TrainLesson.find(Or(TrainLesson.detector == detectorId,TrainLesson.detector == request.detector)):
                log.debug('Listing lesson')
                ptotal = await TrainImageObject.find_many(TrainImageObject.lesson == lesson.id, TrainImageObject.archived == False).count()
                total += ptotal
            return TrainImageObjectCountByDetectorResponse(status=True,total=total)
        except Exception as e:
            log.warning(str(e))
            return TrainImageObjectCountByDetectorResponse(status=False,message=str(e))
        
    async def trainImageObjectUpdate(self, request:TrainImageObjectUpdateRequest, context) -> TrainImageObjectUpdateResponse:
        try:
            found = await TrainImageObject.find_many(TrainImageObject.id == PydanticObjectId(request.id)).first_or_none()
            if found is None:
                return TrainImageObjectUpdateResponse(status=False,message="workspace.trainer.label.errors.not_found")
            found.labels = request.labels
            found.train = request.train
            found.val = request.val
            found.test = request.test
            found.xstart = request.xstart
            found.xend = request.xend
            found.ystart = request.ystart
            found.yend = request.yend
            await found.save()
            return TrainImageObjectUpdateResponse(status=True)
        except Exception as e:
            log.warning(str(e))
            return TrainImageObjectUpdateResponse(status=False,message=str(e))
        
    async def trainImageObject(self, request:TrainImageObjectRequest, context) -> TrainImageObjectResponse:
        try:
            lesson = await TrainLesson.find_many(TrainLesson.id == PydanticObjectId(request.lesson)).first_or_none()
            if lesson is None:
                return TrainImageObjectResponse(status=False,message="workspace.trainer.lesson.errors.not_found")
            detector = await Detector.find_many(Detector.id == PydanticObjectId(lesson.detector)).first_or_none()
            if detector is None:
                return TrainImageObjectResponse(status=False,message="workspace.detector.errors.not_found")
            
            tio = await TrainImageObject(
                lesson=lesson.id,
                frame=request.frame,
                labels=request.labels,
                xstart=request.xstart,
                xend=request.xend,
                ystart=request.ystart,
                yend=request.yend,
                val=request.val,
                train=request.train,
                test=request.test
            ).insert()
            user_id = PydanticObjectId(request.user)
            return TrainImageObjectResponse(status=True,object=Conversions.serialize(tio))
        except Exception as e:
            log.warning(str(e))
            return TrainImageObjectResponse(status=False,message=str(e))
    
    async def trainImageObjectToDetector(self, request:TrainImageObjectToDetectorRequest, context) -> TrainImageObjectToDetectorResponse:
        try:
            detectorId = PydanticObjectId(request.detector)
            user = await User.find(User.id == PydanticObjectId(request.user)).first_or_none()
            lessons = await TrainLesson.find(Or(TrainLesson.detector == detectorId,TrainLesson.detector == request.detector)).to_list()
            total = 0
            for lesson in lessons:
                tios = await TrainImageObject.find(TrainImageObject.lesson == lesson.id, TrainImageObject.archived==False).to_list()
                for tio in tios:
                    imageData = await self.recorder.loadRecordFrameBase64(user,lesson.record,tio.frame) ##str base 64
                    modes = []
                    if tio.test:
                        modes.append(DetectorImageMode.test)
                    if tio.train:
                        modes.append(DetectorImageMode.train)
                    if tio.val:
                        modes.append(DetectorImageMode.val)
                    detectorImages = await self.detector.uploadDetectorImage(user,lesson.detector,imageData,modes)
                    for detectorImage in detectorImages:
                        for label in tio.labels:
                            await self.detector.addDetectorImageLabel(user,detectorImage.id,tio.xstart,tio.xend,tio.ystart,tio.yend,label)
                            total += 1
                    tio.archived = True
                    await tio.save()
            
            return TrainImageObjectToDetectorResponse(status=True,total=total)
        except Exception as e:
            log.warning(str(e))
            return TrainImageObjectToDetectorResponse(status=False,message=str(e))
        