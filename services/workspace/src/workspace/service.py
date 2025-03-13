# PYTHON IMPORTS
import logging

# LIBRARY IMPORTS
from pydantic import BaseModel

# LOCAL IMPORTS
from common.models import MODELS
from common.rpc.workspace_pb2_grpc import WorkspaceServicer
from common.service import Service
from common.service import ServiceConfig
from common.utils.mongodb import Mongodb, MongodbConfig

# INITIALIZATION
log = logging.getLogger(__name__)

class WorkspaceServiceConfig(ServiceConfig):
    database: MongodbConfig

class WorkspaceService(Service, WorkspaceServicer):

    def __init__(self, config: WorkspaceServiceConfig):
        WorkspaceServicer.__init__(self)
        Service.__init__(self)
        self.config:WorkspaceServiceConfig = config
        
    async def start(self):
         await Mongodb.initialize(self.config.database,MODELS)
    