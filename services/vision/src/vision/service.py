# PYTHON IMPORTS
import logging

# LIBRARY IMPORTS
from pydantic import BaseModel

# LOCAL IMPORTS
from common.service import Service
from common.rpc.vision_pb2_grpc import VisionServicer
from common.service import ServiceConfig
from common.utils.mongodb import MongodbConfig

# INITIALIZATION
log = logging.getLogger(__name__)

class VisionServiceConfig(ServiceConfig):
    database: MongodbConfig

class VisionService(Service, VisionServicer):

    def __init__(self, config: VisionServiceConfig):
        VisionServicer.__init__(self)
        Service.__init__(self)
        self.config:VisionServiceConfig = config