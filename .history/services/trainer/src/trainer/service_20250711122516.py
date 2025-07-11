# PYTHON IMPORTS
import logging
from uuid import uuid4


# LIBRARY IMPORTS
from beanie import PydanticObjectId
from beanie.operators import And, Or

# LOCAL IMPORTS
from common.clients.auth import AuthClient
from common.clients.detector import DetectorClient
from common.clients.recorder import RecorderClient
from common.clients.storage import StorageClient
from common.models import MODELS
from common.models.auth import User
from common.models.detector import Detector, DetectorImageMode, DetectorLabel
from common.models.recorder import Record
from common.models.trainer import (
    TrainImageObject,
    TrainSession,
    TrainSessionStatus as ModelTrainSessionStatus,
)
from common.rpc.trainer_pb2 import (
    TrainImageObjectCountByDetectorRequest,
    TrainImageObjectCountByDetectorResponse,
    TrainImageObjectListRequest,
    TrainImageObjectListResponse,
    TrainImageObjectRemoveRequest,
    TrainImageObjectRemoveResponse,
    TrainImageObjectRequest,
    TrainImageObjectResponse,
    TrainImageObjectToDetectorRequest,
    TrainImageObjectToDetectorResponse,
    TrainImageObjectUpdateRequest,
    TrainImageObjectUpdateResponse,
    TrainSessionCreateRequest,
    TrainSessionCreateResponse,
    TrainSessionDetectorRunningRequest,
    TrainSessionDetectorRunningResponse,
    TrainSessionListRequest,
    TrainSessionListResponse,
    TrainSessionRemoveRequest,
    TrainSessionRemoveResponse,
    TrainSessionUpdateRequest,
    TrainSessionUpdateResponse,
)
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
    recorder: ClientConfig
    storage: ClientConfig


class TrainerService(Service, TrainerServicer):

    def __init__(self, config: TrainerServiceConfig):
        TrainerServicer.__init__(self)
        Service.__init__(self)
        self.config: TrainerServiceConfig = config
        self.detector: DetectorClient = DetectorClient(self.config.detector)
        self.auth: AuthClient = AuthClient(self.config.auth)
        self.recorder: RecorderClient = RecorderClient(self.config.recorder)
        self.storage: StorageClient = StorageClient(self.config.storage)

    async def start(self):
        await Mongodb.initialize(self.config.database, MODELS)
        await self.auth.startup()
        await self.detector.startup()
        await self.recorder.startup()
        await self.storage.startup()

    async def trainImageObjectList(
        self, request: TrainImageObjectListRequest, context
    ) -> TrainImageObjectListResponse:
        try:
            detectorId = PydanticObjectId(request.detector)
            recordId = PydanticObjectId(request.record)
            qry = And(
                TrainImageObject.detector == detectorId,
                TrainImageObject.record == recordId,
                TrainImageObject.archived == False,
            )
            if request.frame >= 0:
                qry = And(
                    TrainImageObject.detector == detectorId,
                    TrainImageObject.record == recordId,
                    TrainImageObject.archived == False,
                    TrainImageObject.frame == request.frame,
                )
            tios = await TrainImageObject.find_many(qry).to_list()
            ret = []
            total = 0
            for tio in tios:
                total += 1
                ret.append(Conversions.serialize(tio))
            return TrainImageObjectListResponse(status=True, total=total, objects=ret)
        except Exception as e:
            log.warning(str(e))
            return TrainImageObjectListResponse(status=False, message=str(e))

    async def trainImageObjectRemove(
        self, request: TrainImageObjectRemoveRequest, context
    ) -> TrainImageObjectRemoveResponse:
        try:
            found = await TrainImageObject.find_many(
                TrainImageObject.id == PydanticObjectId(request.id)
            ).first_or_none()
            if not found:
                return TrainImageObjectRemoveResponse(
                    status=False, message="trainer.lesson.errors.object_not_found"
                )
            await found.delete()
            return TrainImageObjectRemoveResponse(status=True)
        except Exception as e:
            log.warning(str(e))
            return TrainImageObjectRemoveResponse(status=False, message=str(e))

    async def trainImageObjectCountByDetector(
        self, request: TrainImageObjectCountByDetectorRequest, context
    ) -> TrainImageObjectCountByDetectorResponse:
        try:
            detectorId = PydanticObjectId(request.detector)
            total = await TrainImageObject.find_many(
                TrainImageObject.detector == detectorId,
                TrainImageObject.archived == False,
            ).count()
            return TrainImageObjectCountByDetectorResponse(status=True, total=total)
        except Exception as e:
            log.warning(str(e))
            return TrainImageObjectCountByDetectorResponse(status=False, message=str(e))

    async def trainImageObjectUpdate(
        self, request: TrainImageObjectUpdateRequest, context
    ) -> TrainImageObjectUpdateResponse:
        try:
            found = await TrainImageObject.find_many(
                TrainImageObject.id == PydanticObjectId(request.id)
            ).first_or_none()
            if found is None:
                return TrainImageObjectUpdateResponse(
                    status=False, message="workspace.trainer.label.errors.not_found"
                )
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
            return TrainImageObjectUpdateResponse(status=False, message=str(e))

    async def trainImageObject(
        self, request: TrainImageObjectRequest, context
    ) -> TrainImageObjectResponse:
        try:

            detector = await Detector.find_many(
                Detector.id == PydanticObjectId(request.detector)
            ).first_or_none()
            if detector is None:
                return TrainImageObjectResponse(
                    status=False, message="detector.errors.not_found"
                )

            record = await Record.find_many(
                Record.id == PydanticObjectId(request.record)
            ).first_or_none()
            if record is None:
                return TrainImageObjectResponse(
                    status=False, message="record.errors.not_found"
                )

            tio = await TrainImageObject(
                record=record.id,
                detector=detector.id,
                frame=request.frame,
                labels=request.labels,
                xstart=request.xstart,
                xend=request.xend,
                ystart=request.ystart,
                yend=request.yend,
                val=request.val,
                train=request.train,
                test=request.test,
            ).insert()
            user_id = PydanticObjectId(request.user)
            return TrainImageObjectResponse(
                status=True, object=Conversions.serialize(tio)
            )
        except Exception as e:
            log.warning(str(e))
            return TrainImageObjectResponse(status=False, message=str(e))

    async def trainImageObjectToDetector(
        self, request: TrainImageObjectToDetectorRequest, context
    ) -> TrainImageObjectToDetectorResponse:
        try:
            detectorId = PydanticObjectId(request.detector)
            user = await User.find(
                User.id == PydanticObjectId(request.user)
            ).first_or_none()
            total = 0

            tios = await TrainImageObject.find(
                TrainImageObject.detector == detectorId,
                TrainImageObject.archived == False,
            ).to_list()
            for tio in tios:
                try:
                    imageData = await self.recorder.loadRecordFrameBase64(
                        user, tio.record, tio.frame
                    )  ##str base 64
                    filename = str(uuid4())+'.png'
                    file_id = await self.storage.save(filename,str(detectorId),imageData,'image/png')
                    modes = []
                    if tio.test:
                        modes.append(DetectorImageMode.test)
                    if tio.train:
                        modes.append(DetectorImageMode.train)
                    if tio.val:
                        modes.append(DetectorImageMode.val)
                    detectorImages = await self.detector.uploadDetectorImage(
                        user, detectorId, file_id, modes
                    )
                    for detectorImage in detectorImages:
                        for label in tio.labels:
                            await self.detector.addDetectorImageLabel(
                                user,
                                detectorImage.id,
                                tio.xstart,
                                tio.xend,
                                tio.ystart,
                                tio.yend,
                                label,
                            )
                            total += 1
                    tio.archived = True
                    await tio.save()
                except Exception as e:
                    log.warning(str(e))

            return TrainImageObjectToDetectorResponse(status=True, total=total)
        except Exception as e:
            log.warning(str(e))
            return TrainImageObjectToDetectorResponse(status=False, message=str(e))

    async def trainSessionCreate(
        self, request: TrainSessionCreateRequest, context
    ) -> TrainSessionCreateResponse:
        try:

            ts = TrainSession(
                user=PydanticObjectId(request.user),
                detector=PydanticObjectId(request.detector),
                status=ModelTrainSessionStatus.IDLE,
            )
            await ts.save()
            return TrainSessionCreateResponse(status=True, id=str(ts.id))
        except Exception as e:
            log.warning(str(e))
            return TrainSessionCreateResponse(status=False, message=str(e))

    async def trainSessionUpdate(
        self, request: TrainSessionUpdateRequest, context
    ) -> TrainSessionUpdateResponse:
        try:
            found = await TrainSession.find(
                TrainSession.id == PydanticObjectId(request.id)
            ).first_or_none()
            if found:
                if request.results and request.results!="":
                    found.results = request.results
                if request.error and request.error !="":
                    found.errors.append(request.error)
                found.status = request.status or ModelTrainSessionStatus.IDLE
                await found.save()
                return TrainSessionUpdateResponse(status=True)

            else:
                TrainSessionUpdateResponse(
                    status=False, message="trainer.errors.session_not_found"
                )
        except Exception as e:
            log.warning(str(e))
            return TrainSessionUpdateResponse(status=False, message=str(e))

    async def trainSessionList(
        self, request: TrainSessionListRequest, context
    ) -> TrainSessionListResponse:
        try:
            sessions = (
                await TrainSession.find(
                    TrainSession.detector == PydanticObjectId(request.detector)
                )
                .skip(request.skip)
                .limit(request.limit)
                .to_list()
            )
            count = await TrainSession.find(
                TrainSession.detector == PydanticObjectId(request.detector)
            ).count()
            ret = []
            for session in sessions:
                ret.append(Conversions.serialize(session))
            return TrainSessionListResponse(status=True, total=count, sessions=ret)
        except Exception as e:
            log.warning(str(e))
            return TrainSessionListResponse(status=False, message=str(e))

    async def trainSessionDetectorRunning(
        self, request: TrainSessionDetectorRunningRequest, context
    ) -> TrainSessionDetectorRunningResponse:
        try:
            count = await TrainSession.find(
                TrainSession.detector == PydanticObjectId(request.detector),
                TrainSession.status == ModelTrainSessionStatus.RUNNING,
            ).count()
            return TrainSessionDetectorRunningResponse(status=True, running=False)
        except Exception as e:
            log.warning(str(e))
            return TrainSessionDetectorRunningResponse(status=False, message=str(e))
        
        
    async def trainSessionRemove(self, request:TrainSessionRemoveRequest, context) -> TrainSessionRemoveResponse:
        try:
            found = await TrainSession.find(TrainSession.id == PydanticObjectId(request.id)).first_or_none()
            if not found:
                return TrainSessionRemoveResponse(status=False,message="trainer.errors.session_not_found")
            await found.delete()
            return TrainSessionRemoveResponse(status=True)
        except Exception as e:
            log.warning(str(e))
            return TrainSessionRemoveResponse(status=False, message=str(e))
