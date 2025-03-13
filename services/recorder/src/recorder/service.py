# PYTHON IMPORTS
import logging

# LIBRARY IMPORTS
from pydantic import BaseModel

# LOCAL IMPORTS
from common.models import MODELS
from common.rpc.recorder_pb2_grpc import RecorderServicer
from common.service import Service
from common.service import ServiceConfig
from common.utils.mongodb import Mongodb, MongodbConfig

# INITIALIZATION
log = logging.getLogger(__name__)

class RecorderServiceConfig(ServiceConfig):
    video: str
    fps:float = 20.0    
    database: MongodbConfig

class RecorderService(Service, RecorderServicer):

    def __init__(self, config: RecorderServiceConfig):
        RecorderServicer.__init__(self)
        Service.__init__(self)
        self.config:RecorderServiceConfig = config
        
    async def start(self):
         await Mongodb.initialize(self.config.database,MODELS)
    