# PYTHON IMPORTS
import logging
from typing import List, Optional, Tuple

from beanie import PydanticObjectId

# LOCAL IMPORTS
from common.models.auth import User
from common.models.recorder import EVENTS, Action, Record
from common.rpc.base_pb2 import Ping, Pong
from common.rpc.recorder_pb2 import (
    CountRecordActionRequest,
    CountRecordActionResponse,
    CountRecordEventRequest,
    CountRecordFrameRequest,
    CountRecordRequest,
    CreateRecordActionRequest,
    CreateRecordActionResponse,
    DeleteRecordRequest,
    ExistRecordEventActionRequest,
    ExistRecordEventActionResponse,
    ListRecordActionRequest,
    ListRecordActionResponse,
    ListRecordEventRequest,
    ListRecordRequest,
    LoadEventRequest,
    LoadRecordActionByEventRequest,
    LoadRecordActionByEventResponse,
    LoadRecordActionRequest,
    LoadRecordActionResponse,
    LoadRecordFrameBase64Request,
    LoadRecordFrameRequest,
    LoadRecordRequest,
    RemoveRecordActionRequest,
    RemoveRecordActionResponse,
    RunningRequest,
    SizeRecordRequest,
    SizeRecordVideoRequest,
    StartRecordRequest,
    StopRecordRequest,
    StreamRangeRecordVideoRequest,
    StreamRangeRecordVideoResponse,
    StreamRecordVideoRequest,
    UpdateRecordActionRequest,
    UpdateRecordActionResponse,
    UpdateRecordRequest,
)
from common.rpc.recorder_pb2_grpc import RecorderStub
from common.service import Client
from common.utils.conversions import Conversions


# INITIALIZATION
log = logging.getLogger(__name__)


class RecorderClient(Client):

    def __init__(self, client_config):
        super().__init__(client_config)

    async def startup(self):
        await super().startup()
        self.client = RecorderStub(self.channel)

    async def ping(self) -> Pong:
        req = Ping()
        res = await self.client.ping(req)
        return res

    async def running(self) -> bool:
        req = RunningRequest()
        res = await self.client.running(req)
        return res.status

    async def loadRecord(
        self, user: User, recorderId: PydanticObjectId
    ) -> Optional[Record]:
        req = LoadRecordRequest(user=str(user.id), id=str(recorderId))
        res = await self.client.loadRecord(req)
        if res.status == False:
            raise Exception(res.message)
        return Conversions.deserialize(res.record)

    async def updateRecord(
        self, user: User, recorderId: PydanticObjectId, name: str, description: str
    ) -> Optional[Record]:
        req = UpdateRecordRequest(
            user=str(user.id), id=str(recorderId), name=name, description=description
        )
        res = await self.client.updateRecord(req)
        if res.status == False:
            raise Exception(res.message)
        return Conversions.deserialize(res.record)

    async def listRecord(
        self,
        user: User,
        projectId: PydanticObjectId,
        skip: int,
        limit: int,
        search: str,
    ) -> Tuple[int, List[Record]]:
        req = ListRecordRequest(
            user=str(user.id),
            project=str(projectId),
            skip=skip,
            limit=limit,
            search=search,
        )
        res = await self.client.listRecord(req)
        if res.status == False:
            raise Exception(res.message)
        total = res.total
        ret = []
        for record in res.records:
            ret.append(Conversions.deserialize(record))
        return total, ret

    async def deleteRecord(self, user: User, recordId: PydanticObjectId) -> bool:
        req = DeleteRecordRequest(user=str(user.id), record=str(recordId))
        res = await self.client.deleteRecord(req)
        if res.status == False:
            raise Exception(res.message)
        return res.status

    async def countRecord(self, user: User, projectId: PydanticObjectId) -> int:
        req = CountRecordRequest(user=str(user.id), project=str(projectId))
        res = await self.client.countRecord(req)
        if res.status == False:
            raise Exception(res.message)
        return res.total

    async def startRecord(
        self, user: User, projectId: PydanticObjectId, name: str, description: str
    ) -> Record:
        req = StartRecordRequest(
            user=str(user.id),
            project=str(projectId),
            name=name,
            description=description,
        )
        res = await self.client.startRecord(req)
        if res.status == False:
            raise Exception(res.message)
        return Conversions.deserialize(res.record)

    async def stopRecord(self, user: User) -> bool:
        req = StopRecordRequest(user=str(user.id))
        res = await self.client.stopRecord(req)
        if res.status == False:
            raise Exception(res.message)
        return res.status

    async def countRecordEvent(self, user: User, recordId: PydanticObjectId) -> int:
        req = CountRecordEventRequest(user=str(user.id), record=str(recordId))
        res = await self.client.countRecordEvent(req)
        if res.status == False:
            raise Exception(res.message)
        return res.total

    async def listRecordEvent(
        self, user: User, recordId: PydanticObjectId
    ) -> List[EVENTS]:
        req = ListRecordEventRequest(user=str(user.id), record=str(recordId))
        res = await self.client.listRecordEvent(req)
        if res.status == False:
            raise Exception(res.message)
        ret = []
        for event in res.events:
            ret.append(Conversions.deserialize(event))
        return ret

    async def countRecordFrame(self, user: User, recordId: PydanticObjectId) -> int:
        req = CountRecordFrameRequest(user=str(user.id), record=str(recordId))
        res = await self.client.countRecordFrame(req)
        if res.status == False:
            raise Exception(res.message)
        return res.total

    async def loadEvent(self, user: User, eventId: PydanticObjectId) -> EVENTS:
        req = LoadEventRequest(user=str(user.id), id=str(eventId))
        res = await self.client.loadEvent(req)
        if res.status == False:
            raise Exception(res.message)
        return Conversions.deserialize(res.event)

    async def loadRecordFrame(
        self, user: User, recordId: PydanticObjectId, frame: int, thumbnail:bool=False
    ) -> bytes:
        req = LoadRecordFrameRequest(
            user=str(user.id), record=str(recordId), frame=frame, thumbnail=thumbnail
        )
        res = await self.client.loadRecordFrame(req)
        if res.status == False:
            raise Exception(res.message)
        return res.frame

    async def loadRecordFrameBase64(
        self, user: User, recordId: PydanticObjectId, frame: int, thumbnail:bool=False
    ) -> str:
        req = LoadRecordFrameBase64Request(
            user=str(user.id), record=str(recordId), frame=frame, thumbnail=thumbnail
        )
        res = await self.client.loadRecordFrameBase64(req)
        if res.status == False:
            raise Exception(res.message)
        return res.frame

    async def sizeRecord(self, user: User, recordId: PydanticObjectId) -> int:
        req = SizeRecordRequest(user=str(user.id), record=str(recordId))
        res = await self.client.sizeRecord(req)
        if res.status == False:
            raise Exception(res.message)
        return res.size

    async def sizeRecordVideo(self, user: User, recordId: PydanticObjectId) -> int:
        req = SizeRecordVideoRequest(user=str(user.id), record=str(recordId))
        res = await self.client.sizeRecordVideo(req)
        if res.status == False:
            raise Exception(res.message)
        return res.size

    async def streamRecordVideo(self, user: User, recordId: PydanticObjectId):
        req = StreamRecordVideoRequest(user=str(user.id), record=str(recordId))
        return self.client.streamRecordVideo(req)

    async def streamRangeRecordVideo(
        self, user: User, recordId: PydanticObjectId, start_byte: int, end_byte: int
    ) -> bytes:
        req = StreamRangeRecordVideoRequest(
            user=str(user.id),
            record=str(recordId),
            start_byte=start_byte,
            end_byte=end_byte,
        )
        res:StreamRangeRecordVideoResponse = await self.client.streamRangeRecordVideo(req)
        
        if res.status == False:
            raise Exception(res.message)
        return res.data

    async def createRecordAction(
        self,
        user: User,
        recordId: PydanticObjectId,
        eventId: PydanticObjectId,
        byLabel: Optional[str] = None,
        byText: Optional[str] = None,
        byRegex: Optional[str] = None,
        byOrder: List[str] = [],
        byPosition: List[float] = [],
        confidence: float = 0.0,
        image: Optional[str] = None,
    ) -> Action:
        req = CreateRecordActionRequest(
            user=str(user.id),
            record=str(recordId),
            event=str(eventId),
            byLabel=byLabel,
            byText=byText,
            byRegex=byRegex,
            byOrder=byOrder,
            byPosition=byPosition,
            confidence=confidence,
            image=image,
        )
        res: CreateRecordActionResponse = await self.client.createRecordAction(req)
        if res.status == False:
            raise Exception(res.message)
        return Conversions.deserialize(res.action)

    async def listRecordAction(
        self,
        user: User,
        recordId: PydanticObjectId,
        eventId: Optional[PydanticObjectId] = None,
        skip: int = 0,
        limit: int = 10,
        search: Optional[str] = None,
    ) -> Tuple[int, List[Action]]:
        if eventId is None:
            event = None
        else:
            event = str(eventId)
        req = ListRecordActionRequest(
            user=str(user.id),
            record=str(recordId),
            event=event,
            skip=skip,
            limit=limit,
            search=search,
        )
        res: ListRecordActionResponse = await self.client.listRecordAction(req)
        if res.status == False:
            raise Exception(res.message)
        total = res.total
        ret = []
        for act in res.actions:
            ret.append(Conversions.deserialize(act))
        return total, ret

    async def countRecordAction(
        self,
        user: User,
        recordId: PydanticObjectId,
        eventId: Optional[PydanticObjectId] = None,
        search: Optional[str] = None,
    ) -> int:
        if eventId is None:
            event = None
        else:
            event = str(eventId)
        req = CountRecordActionRequest(
            user=str(user.id), record=str(recordId), event=event, search=search
        )
        res: CountRecordActionResponse = await self.client.countRecordAction(req)
        if res.status == False:
            raise Exception(res.message)
        return res.total

    async def loadRecordAction(self, user: User, actionId: PydanticObjectId) -> Action:
        req = LoadRecordActionRequest(user=str(user.id), id=str(actionId))
        res: LoadRecordActionResponse = await self.client.loadRecordAction(req)
        if res.status == False:
            raise Exception(res.message)
        return Conversions.deserialize(res.action)

    async def loadRecordActionByEvent(
        self, user: User, eventId: PydanticObjectId
    ) -> Action:
        req = LoadRecordActionByEventRequest(user=str(user.id), event=str(eventId))
        res: LoadRecordActionByEventResponse = (
            await self.client.loadRecordActionByEvent(req)
        )
        if res.status == False:
            raise Exception(res.message)
        return Conversions.deserialize(res.action)

    async def existRecordEventAction(
        self, user: User, eventId: PydanticObjectId
    ) -> bool:
        req = ExistRecordEventActionRequest(user=str(user.id), event=str(eventId))
        res: ExistRecordEventActionResponse = await self.client.existRecordEventAction(
            req
        )
        if res.status == False:
            raise Exception(res.message)
        return res.found

    async def removeRecordAction(self, user: User, actionId: PydanticObjectId) -> bool:
        req = RemoveRecordActionRequest(user=str(user.id), id=str(actionId))
        res: RemoveRecordActionResponse = await self.client.removeRecordAction(req)
        if res.status == False:
            raise Exception(res.message)
        return res.status

    async def updateRecordAction(
        self,
        user: User,
        actionId: PydanticObjectId,
        eventId: PydanticObjectId,
        byLabel: Optional[str] = None,
        byText: Optional[str] = None,
        byRegex: Optional[str] = None,
        byOrder: List[str] = [],
        byPosition: List[float] = [],
        confidence: float = 0.0,
        image: Optional[str] = None,
    ) -> Action:
        req = UpdateRecordActionRequest(
            user=str(user.id),
            id=str(actionId),
            event=str(eventId),
            byLabel=byLabel,
            byText=byText,
            byRegex=byRegex,
            byOrder=byOrder,
            byPosition=byPosition,
            confidence=confidence,
            image=image,
        )
        res: UpdateRecordActionResponse = await self.client.updateRecordAction(req)
        if res.status == False:
            raise Exception(res.message)
        return Conversions.deserialize(res.action)
