# PYTHON IMPORTS
import logging
import os

# LIBRARY IMPORTS
from beanie import PydanticObjectId
from beanie.operators import And, Or
from pydantic import BaseModel
import tiktoken

# LOCAL IMPORTS
from common.clients.auth import AuthClient
from common.models import MODELS
from common.rpc.language_pb2 import LanguageDecodeRequest, LanguageDecodeResponse, LanguageEncodeRequest, LanguageEncodeResponse
from common.rpc.language_pb2_grpc import LanguageServicer
from common.service import ClientConfig, Service
from common.service import ServiceConfig
from common.utils.mongodb import Mongodb, MongodbConfig

# INITIALIZATION
log = logging.getLogger(__name__)
RECORDS = {}

class TikTokenConfig(BaseModel):
    model: str = "o200k_base"
    path: str = 'data'

class LanguageServiceConfig(ServiceConfig):
    database: MongodbConfig
    auth: ClientConfig
    tiktoken: TikTokenConfig

class LanguageService(Service, LanguageServicer):

    def __init__(self, config: LanguageServiceConfig):
        LanguageServicer.__init__(self)
        Service.__init__(self)
        self.config:LanguageServiceConfig = config
        self.auth: AuthClient = AuthClient(self.config.auth)
        
    async def start(self):
        await Mongodb.initialize(self.config.database,MODELS)
        cache_dir = os.path.join(os.getcwd(),self.config.tiktoken.path)
        os.environ["TIKTOKEN_CACHE_DIR"] = cache_dir
        self.enc = tiktoken.get_encoding(self.config.tiktoken.model)
        
        #await self.auth.startup()
        
    #async def tokenize(self):   
        #assert enc.decode(enc.encode("hello world")) == "hello world"
        
    async def languageEncode(self, request:LanguageEncodeRequest, context) -> LanguageEncodeResponse:
        try:
            tokens = self.enc.encode(request.text)
            return LanguageEncodeResponse(status=True,tokens=tokens)
        except Exception as e:
            log.warning(str(e))
            return LanguageEncodeResponse(status=False,message=str(e))
    
    async def languageDecode(self, request: LanguageDecodeRequest, context) -> LanguageDecodeResponse:
        try:
            text = self.enc.decode(request.tokens)
            return LanguageDecodeResponse(status=True,text=text)
        except Exception as e:
            log.warning(str(e))
            return LanguageDecodeResponse(status=False,message=str(e))

        