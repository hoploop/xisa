# PYTHON IMPORTS
import logging
from typing import List, Optional, Tuple

from beanie import PydanticObjectId

# LIBRARY IMPORTS

# LOCAL IMPORTS

from common.models.auth import User
from common.models.detector import (
    DetectObject,
    DetectText,
    Detector,
    DetectorLabel,
    DetectorImage,
    DetectorImageLabel,
    DetectorImageMode,
    DetectorSuggestion,
)
from common.rpc.base_pb2 import Ping, Pong
from common.rpc.detector_pb2 import (
    AddDetectorLabelRequest,
    AddDetectorImageLabelRequest,
    AddDetectorLabelResponse,
    CanRemoveDetectorLabelRequest,
    CanRemoveDetectorLabelResponse,
    CountDetectorLabelRequest,
    CountDetectorImageLabelRequest,
    CountDetectorImageRequest,
    CountDetectorRequest,
    CreateDetectorRequest,
    DetectObjectsRequest,
    DetectTextsRequest,
    ExistsDetectorLabelRequest,
    ExistsDetectorLabelResponse,
    ListDetectorLabelRequest,
    ListDetectorImageLabelRequest,
    ListDetectorImageRequest,
    ListDetectorLabelResponse,
    ListDetectorRequest,
    LoadDetectorRequest,
    RemoveDetectorImageLabelRequest,
    RemoveDetectorImageRequest,
    RemoveDetectorLabelRequest,
    RemoveDetectorLabelResponse,
    RemoveDetectorRequest,
    SuggestStepRequest,
    SuggestStepResponse,
    TrainDetectorRequest,
    UpdateDetectorRequest,
    UploadDetectorImageRequest,
    DetectorImageMode as RpcDetectorImageMode,
)
from common.rpc.detector_pb2_grpc import DetectorStub
from common.service import Client
from common.utils.conversions import Conversions

# INITIALIZATION
log = logging.getLogger(__name__)


class DetectorClient(Client):

    def __init__(self, client_config):
        super().__init__(client_config)

    async def startup(self):
        await super().startup()
        self.client = DetectorStub(self.channel)

    async def ping(self) -> Pong:
        req = Ping()
        res = await self.client.ping(req)
        return res

    async def detectObjects(
        self,
        user: User,
        detectorId: PydanticObjectId,
        data: str,
        confidence: float = 0.7,
    ) -> List[DetectObject]:
        req = DetectObjectsRequest(
            user=str(user.id),
            data=data,
            detector=str(detectorId),
            confidence=confidence,
        )
        res = await self.client.detectObjects(req)
        if res.status == False:
            raise Exception(res.message)
        ret = []
        for obj in res.objects:
            ret.append(
                DetectObject(
                    x=obj.x,
                    y=obj.y,
                    w=obj.w,
                    h=obj.h,
                    confidence=obj.confidence,
                    code=obj.code,
                    name=obj.name,
                    row=obj.row,
                    col=obj.col,
                )
            )
        return ret
    
    async def findDetectorLabel(self,user:User,detectorId:PydanticObjectId,name:str) -> DetectorLabel:
        req = AddDetectorLabelRequest(user=str(user.id),detector=str(detectorId),name=name)
        res: AddDetectorLabelResponse = await self.client.findDetectorImageLabel(req)
        if res.status == False:
            raise Exception(res.message)
        return Conversions.deserialize(res.label)

    async def suggestStep(
        self,
        user: User,
        data: str,
        detectorId: PydanticObjectId,
        eventId: PydanticObjectId,
        confidence: float = 0.1,
    ) -> List[DetectorSuggestion]:
        req = SuggestStepRequest(
            user=str(user.id),
            data=data,
            event=str(eventId),
            detector=str(detectorId),
            confidence=confidence,
        )
        res: SuggestStepResponse = await self.client.suggestStep(req)
        if res.status == False:
            raise Exception(res.message)
        ret = []
        for su in res.suggestions:
            ret.append(
                Conversions.deserialize(su)
            )
        return ret

    async def addDetectorLabel(
        self, user: User, detectorId: PydanticObjectId, name: str
    ) -> Optional[DetectorLabel]:
        req = AddDetectorLabelRequest(
            user=str(user.id), detector=str(detectorId), name=name
        )
        res:AddDetectorLabelResponse = await self.client.addDetectorLabel(req)
        if res.status == False:
            raise Exception(res.message)
        if res.label:
            return Conversions.deserialize(res.label)
        else:
            return None

    async def existsDetectorLabel(
        self, user: User, detectorId: PydanticObjectId, name: str
    ) -> Optional[DetectorLabel]:
        req = ExistsDetectorLabelRequest(
            user=str(user.id), detector=str(detectorId), name=name
        )
        res:ExistsDetectorLabelResponse = await self.client.existsDetectorLabel(req)
        if res.status == False:
            raise Exception(res.message)
        if res.label:
            return Conversions.deserialize(res.label)
        else:
            return None

    async def detectTexts(
        self, user: User, data: str, confidence: float = 0.7
    ) -> List[DetectText]:
        req = DetectTextsRequest(user=str(user.id), data=data, confidence=confidence)
        res = await self.client.detectTexts(req)
        if res.status == False:
            raise Exception(res.message)
        ret = []
        for text in res.texts:
            ret.append(
                DetectText(
                    x=text.x,
                    y=text.y,
                    w=text.w,
                    h=text.h,
                    page=text.page,
                    block=text.block,
                    par=text.par,
                    line=text.line,
                    word=text.word,
                    value=text.value,
                    confidence=text.confidence,
                )
            )
        return ret

    async def listDetector(
        self,
        user: User,
        projectId: PydanticObjectId,
        skip: int,
        limit: int,
        search: str,
    ) -> Tuple[int, List[Detector]]:
        req = ListDetectorRequest(
            user=str(user.id),
            project=str(projectId),
            skip=skip,
            limit=limit,
            search=search,
        )
        res = await self.client.listDetector(req)
        if res.status == False:
            raise Exception(res.message)
        total = res.total
        ret = []
        for detector in res.detectors:
            ret.append(Conversions.deserialize(detector))
        return total, ret

    async def countDetector(self, user: User, projectId: PydanticObjectId) -> int:
        req = CountDetectorRequest(user=str(user.id), project=str(projectId))
        res = await self.client.countDetector(req)
        if res.status == False:
            raise Exception(res.message)
        return res.total

    async def updateDetector(
        self, user: User, detectorId: PydanticObjectId, name: str, description: str
    ) -> Detector:
        req = UpdateDetectorRequest(
            user=str(user.id), id=str(detectorId), name=name, description=description
        )
        res = await self.client.updateDetector(req)
        if res.status == False:
            raise Exception(res.message)
        return Conversions.deserialize(res.detector)

    async def loadDetector(self, user: User, detectorId: PydanticObjectId) -> Detector:
        req = LoadDetectorRequest(user=str(user.id), id=str(detectorId))
        res = await self.client.loadDetector(req)
        if res.status == False:
            raise Exception(res.message)
        return Conversions.deserialize(res.detector)

    async def createDetector(
        self,
        user: User,
        projectId: PydanticObjectId,
        name: str,
        description: str,
        origin: str = None,
    ) -> Detector:
        req = CreateDetectorRequest(
            user=str(user.id),
            project=str(projectId),
            name=name,
            description=description,
            origin=origin,
        )
        res = await self.client.createDetector(req)
        if res.status == False:
            raise Exception(res.message)
        return Conversions.deserialize(res.detector)

    async def trainDetector(
        self,
        user: User,
        detectorId: PydanticObjectId,
        session: str,
        epochs: int,
        image_size: int,
    ):
        req = TrainDetectorRequest(
            user=str(user.id),
            session=session,
            detector=str(detectorId),
            epochs=epochs,
            imageSize=image_size,
        )
        res = await self.client.trainDetector(req)
        if res.status == False:
            raise Exception(res.message)
        return res.status

    async def listDetectorImage(
        self, user: User, detectorId: PydanticObjectId, skip: int, limit: int
    ) -> Tuple[int, List[DetectorImage]]:
        req = ListDetectorImageRequest(
            user=str(user.id), detector=str(detectorId), skip=skip, limit=limit
        )
        res = await self.client.listDetectorImage(req)
        if res.status == False:
            raise Exception(res.message)
        total = res.total
        ret = []
        for image in res.images:
            ret.append(Conversions.deserialize(image))
        return total, ret

    async def countDetectorImage(self, user: User, detectorId: PydanticObjectId) -> int:
        req = CountDetectorImageRequest(user=str(user.id), detector=str(detectorId))
        res = await self.client.countDetectorImage(req)
        if res.status == False:
            raise Exception(res.message)
        return res.total

    async def removeDetectorImage(self, user: User, imageId: PydanticObjectId) -> bool:
        req = RemoveDetectorImageRequest(user=str(user.id), id=str(imageId))
        res = await self.client.removeDetectorImage(req)
        if res.status == False:
            raise Exception(res.message)
        return res.status

    async def removeDetector(self, user: User, detectorId: PydanticObjectId) -> bool:
        req = RemoveDetectorRequest(user=str(user.id), id=str(detectorId))
        res = await self.client.removeDetector(req)
        if res.status == False:
            raise Exception(res.message)
        return res.status

    async def addDetectorImageLabel(
        self,
        user: User,
        imageId: PydanticObjectId,
        xstart: float,
        xend: float,
        ystart: float,
        yend: float,
        label: str,
    ) -> DetectorImageLabel:
        req = AddDetectorImageLabelRequest(
            user=str(user.id),
            image=str(imageId),
            xstart=xstart,
            xend=xend,
            ystart=ystart,
            yend=yend,
            label=label,
        )
        res = await self.client.addDetectorImageLabel(req)
        if res.status == False:
            raise Exception(res.message)
        return Conversions.deserialize(res.label)

    async def uploadDetectorImage(
        self,
        user: User,
        detectorId: PydanticObjectId,
        data: str,
        modes: List[DetectorImageMode],
    ) -> List[DetectorImage]:
        RpcDetectorImageMode
        rmodes = []
        for mode in modes:
            if mode == DetectorImageMode.test:
                rmodes.append(RpcDetectorImageMode.TEST)
            elif mode == DetectorImageMode.train:
                rmodes.append(RpcDetectorImageMode.TRAIN)
            elif mode == DetectorImageMode.val:
                rmodes.append(RpcDetectorImageMode.VAL)

        req = UploadDetectorImageRequest(
            user=str(user.id), detector=str(detectorId), data=data, modes=rmodes
        )
        res = await self.client.uploadDetectorImage(req)
        if res.status == False:
            raise Exception(res.message)
        ret = []
        for image in res.images:
            ret.append(Conversions.deserialize(image))
        return ret
    
    async def removeDetectorLabel(self,user:User,labelId:PydanticObjectId) -> bool:
        req = RemoveDetectorLabelRequest(user=str(user.id),id=str(labelId))
        res: RemoveDetectorLabelResponse = await self.client.removeDetectorLabel(req)
        if res.status == False:
            raise Exception(res.message)
        return res.status
    
    async def canRemoveDetectorLabel(self,user:User,labelId:PydanticObjectId) -> bool:
        req = CanRemoveDetectorLabelRequest(user=str(user.id),id=str(labelId))
        res: CanRemoveDetectorLabelResponse = await self.client.canRemoveDetectorLabel(req)
        if res.status == False:
            raise Exception(res.message)
        return res.result

    async def listDetectorImageLabel(
        self, user: User, imageId: PydanticObjectId, skip: int, limit: int, search: str
    ) -> Tuple[int, List[DetectorImageLabel]]:
        req = ListDetectorImageLabelRequest(
            user=str(user.id), image=str(imageId), skip=skip, limit=limit, search=search
        )
        res = await self.client.listDetectorImageLabel(req)
        if res.status == False:
            raise Exception(res.message)
        ret = []
        total = res.total
        for label in res.labels:
            ret.append(Conversions.deserialize(label))
        return total, ret

    async def listDetectorLabel(
        self,
        user: User,
        detectorId: PydanticObjectId,
        skip: int,
        limit: int,
        search: str,
        exclude: List[str]=[]
    ) -> Tuple[int, List[DetectorLabel]]:
        req = ListDetectorLabelRequest(
            user=str(user.id),
            detector=str(detectorId),
            skip=skip,
            limit=limit,
            search=search,
            exclude=exclude
        )
        res: ListDetectorLabelResponse = await self.client.listDetectorLabel(req)
        if res.status == False:
            raise Exception(res.message)
        ret = []
        total = res.total
        
        for label in res.labels:
            ret.append(Conversions.deserialize(label))
        return total, ret

    async def countDetectorLabel(self, user: User, detectorId: PydanticObjectId) -> int:
        req = CountDetectorLabelRequest(user=str(user.id), detector=str(detectorId))
        res = await self.client.countDetectorLabel(req)
        if res.status == False:
            raise Exception(res.message)
        return res.total

    async def removeDetectorImageLabel(
        self, user: User, labelId: PydanticObjectId
    ) -> bool:
        req = RemoveDetectorImageLabelRequest(user=str(user.id), label=str(labelId))
        res = await self.client.removeDetectorImageLabel(req)
        if res.status == False:
            raise Exception(res.message)
        return res.status

    async def countDetectorImageLabel(
        self, user: User, imageId: PydanticObjectId
    ) -> int:
        req = CountDetectorImageLabelRequest(user=str(user.id), image=str(imageId))
        res = await self.client.countDetectorImageLabel(req)
        if res.status == False:
            raise Exception(res.message)
        return res.total
