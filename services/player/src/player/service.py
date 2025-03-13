# PYTHON IMPORTS
import logging

# LIBRARY IMPORTS

# LOCAL IMPORTS
from common.models import MODELS
from common.rpc.player_pb2_grpc import PlayerServicer
from common.service import Service
from common.service import ServiceConfig
from common.utils.mongodb import Mongodb, MongodbConfig

# INITIALIZATION
log = logging.getLogger(__name__)

class PlayerServiceConfig(ServiceConfig):
    database: MongodbConfig
    detectors: str

class PlayerService(Service, PlayerServicer):

    def __init__(self, config: PlayerServiceConfig):
        PlayerServicer.__init__(self)
        Service.__init__(self)
        self.config:PlayerServiceConfig = config
        
    async def start(self):
         await Mongodb.initialize(self.config.database,MODELS)
    