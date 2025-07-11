# PYTHON IMPORTS
from datetime import datetime
import logging

from beanie import PydanticObjectId

# LIBRARY IMPORTS

# LOCAL IMPORTS
from common.clients.api import ApiClient
from common.clients.language import LanguageClient
from common.models import MODELS
from common.rpc.storage_pb2_grpc import StorageServicer

from common.rpc.player_pb2_grpc import PlayerServicer
from common.service import ClientConfig, Service
from common.service import ServiceConfig
from common.utils.mongodb import Mongodb, MongodbConfig

# INITIALIZATION
log = logging.getLogger(__name__)


class StorageServiceConfig(ServiceConfig):
    database: MongodbConfig
    

class StorageService(Service, StorageServicer):

    def __init__(self, config: PlayerServiceConfig):
        PlayerServicer.__init__(self)
        Service.__init__(self)
        self.config: PlayerServiceConfig = config
        self.api: ApiClient = ApiClient(self.config.api)
        self.language: LanguageClient = LanguageClient(self.config.language)

    async def start(self):
        await Mongodb.initialize(self.config.database, MODELS)
        await self.api.startup()
