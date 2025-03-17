# PYTHON IMPORTS
import logging
import os

# LIBRARY IMPORTS
from beanie import PydanticObjectId
from beanie.operators import In,And,Or,RegEx

# LOCAL IMPORTS
from common.models import MODELS
from common.models.recorder import Record
from common.rpc.recorder_pb2 import CountRecordRequest, CountRecordResponse, DeleteRecordRequest, DeleteRecordResponse, ListRecordRequest, ListRecordResponse, LoadRecordRequest, LoadRecordResponse, RunningRequest, RunningResponse, UpdateRecordRequest, UpdateRecordResponse
from common.rpc.recorder_pb2_grpc import RecorderServicer
from common.service import Service
from common.service import ServiceConfig
from common.utils.conversions import Conversions
from common.utils.mongodb import Mongodb, MongodbConfig
from recorder.constants import VIDEO_EXT

# INITIALIZATION
log = logging.getLogger(__name__)
RECORDS = {}

class RecorderServiceConfig(ServiceConfig):
    video: str
    fps:float = 20.0    
    database: MongodbConfig

class RecorderService(Service, RecorderServicer):

    def __init__(self, config: RecorderServiceConfig):
        RecorderServicer.__init__(self)
        Service.__init__(self)
        self.config:RecorderServiceConfig = config
        self.is_running = False
        self.record = None
        self.events = []

        
    async def start(self):
         await Mongodb.initialize(self.config.database,MODELS)
         
    async def running(self, request: RunningRequest, context) -> RunningResponse:
        return RunningResponse(status=self.is_running)
    
    async def loadRecord(self, request:LoadRecordRequest, context) -> LoadRecordResponse:
        try:
            user_id = PydanticObjectId(request.user)
            record_id = PydanticObjectId(request.id)
            found = await Record.find_many(Record.id == record_id,In(Record.users,[user_id])).first_or_none()
            if not found:
                raise LoadRecordResponse(status=False,message="workspace.record.errors.not_found")
            return LoadRecordResponse(status=True,record=Conversions.serialize(found))
        except Exception as e:
            log.warning(str(e))
            return LoadRecordResponse(status=False,message=str(e))
        
        
    async def updateRecord(self, request: UpdateRecordRequest, context) -> UpdateRecordResponse:
        try:
            user_id = PydanticObjectId(request.user)
            record_id = PydanticObjectId(request.id)
            name = request.name
            description = request.description
            found = await Record.find_many(Record.id == record_id,In(Record.users,[user_id])).first_or_none()
            if not found:
                return LoadRecordResponse(status=False,message="workspace.record.errors.not_found")
            others_found = await Record.find_many(Record.project == found.project,Record.name == name,Record.id != found.id).first_or_none()
            if others_found:
                raise LoadRecordResponse(status=False,message="workspace.record.errors.already_existing")
            found.name = name
            found.description= description
            await found.save()
            return LoadRecordResponse(status=1,record=Conversions.serialize(found))
        
        except Exception as e:
            log.warning(str(e))
            return UpdateRecordResponse(status=False,message=str(e))
    
    
    async def listRecord(self, request:ListRecordRequest, context) -> ListRecordResponse:
        try:
            project_id = PydanticObjectId(request.project)
            user_id = PydanticObjectId(request.user)
            search = request.search
            skip = request.skip
            limit = request.limit
            qry = And(Record.project == project_id,In(Record.users,[user_id]))
            if search is not None and search.strip()!='':
                qry = And(
                    Record.project == project_id,
                    In(Record.users,[user_id]),
                    Or(
                        RegEx(Record.name, search, options="i"),
                        RegEx(Record.description, search, options="i"),
                    ),
                )
            total = await Record.find(qry).count()
            records = await Record.find(qry).skip(skip).limit(limit).sort(-Record.created).to_list()
            ret = []
            for record in records:
                ret.append(Conversions.serialize(record))
            return ListRecordResponse(status=True,total=total,records=ret)
        except Exception as e:
            log.warning(str(e))
            return ListRecordResponse(status=False,message=str(e))
        
    async def countRecord(self, request:CountRecordRequest, context) -> CountRecordResponse:
        try:
            project_id = PydanticObjectId(request.project)
            user_id = PydanticObjectId(request.user)
            qry = And(Record.project == project_id,In(Record.users,[user_id]))
            total = await Record.find(qry).count()
            return CountRecordResponse(status=True,total=total)
        except Exception as e:
            log.warning(str(e))
            return CountRecordResponse(status=False,message=str(e))
        
    async def deleteRecord(self, request: DeleteRecordRequest, context) -> DeleteRecordResponse:
        try:
            user_id = PydanticObjectId(request.user)
            record_id = PydanticObjectId(request.record)
            record = await Record.find_many(Record.id == record_id,In(Record.users,[user_id])).first_or_none()
            if record:
                filename = os.path.join(self.config.video,str(record.id)+VIDEO_EXT)
                if os.path.exists(filename):
                    os.remove(filename)
                await record.delete()
                return DeleteRecordResponse(status=True)
            else:
                raise Exception("workspace.record.errors.not_found")
        except Exception as e:
            log.warning(str(e))
            return DeleteRecordResponse(status=False,message=str(e))
        