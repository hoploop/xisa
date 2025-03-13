# PYTHON IMPORTS
import logging

# LIBRARY IMPORTS
from pydantic import BaseModel

# LOCAL IMPORTS
from common.models import MODELS
from common.service import Service
from common.rpc.detector_pb2_grpc import DetectorServicer
from common.service import ServiceConfig
from common.utils.mongodb import Mongodb, MongodbConfig

# INITIALIZATION
log = logging.getLogger(__name__)

class DetectorServiceConfig(ServiceConfig):
    database: MongodbConfig
    path: str
    original: str
    name: str
    data: str
    runs: str
    classes: str
    video:str

class DetectorService(Service, DetectorServicer):

    def __init__(self, config: DetectorServiceConfig):
        DetectorServicer.__init__(self)
        Service.__init__(self)
        self.config:DetectorServiceConfig = config
        
    async def start(self):
         await Mongodb.initialize(self.config.database,MODELS)