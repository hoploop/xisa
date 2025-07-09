# PYTHON IMPORTS
import logging
import os
from typing import Dict, List

# LIBRARY IMPORTS
from beanie import PydanticObjectId
from beanie.operators import And, Or
from pydantic import BaseModel

import tiktoken

# LOCAL IMPORTS
from common.clients.auth import AuthClient
from common.models import MODELS
from common.rpc.language_pb2 import LanguageDecodeRequest, LanguageDecodeResponse, LanguageEncodeRequest, LanguageEncodeResponse, LanguageTranslateRequest, LanguageTranslateResponse
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
    
class AnnoyConfig(BaseModel):
    path: str = 'data/annoy.db'

class LanguageServiceConfig(ServiceConfig):
    database: MongodbConfig
    auth: ClientConfig
    tiktoken: TikTokenConfig
    annoy: AnnoyConfig
    i18n: str

class LanguageService(Service, LanguageServicer):

    def __init__(self, config: LanguageServiceConfig):
        LanguageServicer.__init__(self)
        Service.__init__(self)
        self.config:LanguageServiceConfig = config
        self.auth: AuthClient = AuthClient(self.config.auth)
        self.translations = {}
        
    async def start(self):
        await Mongodb.initialize(self.config.database,MODELS)
        cache_dir = os.path.join(os.getcwd(),self.config.tiktoken.path)
        os.environ["TIKTOKEN_CACHE_DIR"] = cache_dir
        self.enc = tiktoken.get_encoding(self.config.tiktoken.model)
        
        log.info("Initializing Annoy db")
        
        #await self.auth.startup()
        
    #async def tokenize(self):   
        #assert enc.decode(enc.encode("hello world")) == "hello world"
        
    async def vectorInsert(self,collection:str,data:Dict,partition:str=None):
        #data: {"id":int,"vector":List[float],attrs...}
        if not self.milvus.has_collection(collection):
            self.milvus.create_collection(collection)
        
        if partition is not None and not self.milvus.has_partition(collection,partition):
            self.milvus.create_partition(collection,partition)
            
        self.milvus.insert(collection,data,partition_name=partition)
        
    async def vectorUpsert(self,collection:str,data:Dict,partition:str=None):
        #data: {"id":int,"vector":List[float],attrs...}
        if not self.milvus.has_collection(collection):
            self.milvus.create_collection(collection)
        
        if partition is not None and not self.milvus.has_partition(collection,partition):
            self.milvus.create_partition(collection,partition)
            
        self.milvus.upsert(collection,data,partition_name=partition)
        
    async def vectorDelete(self,collection:str,filt:str,partition:str=None) -> int:
        #data: {"id":int,"vector":List[float],attrs...}
        # filt="color in ['red_7025', 'purple_4976]"
            
        res = self.milvus.delete(collection_name=collection,partition_name=partition,filter=filt)
        return res['delete_count']
    
    async def vectorDeleteByIds(self,collection:str,ids:List[int],partition:str=None) -> int:
        #data: {"id":int,"vector":List[float],attrs...}
        # filt="color in ['red_7025', 'purple_4976]"
            
        res = self.milvus.delete(collection_name=collection,partition_name=partition,ids=ids)
        return res['delete_count']
    
    async def vectorSearch(self,collection:str,query: List[float],partition:str=None,fields:List[str]=None,filt:str=None,offset:int=0):
        #query_vector = [0.3580376395471989, -0.6023495712049978, 0.18414012509913835, -0.26286205330961354, 0.9029438446296592]
        # filt = 'color like "red%" and likes > 50',
        '''
        res = self.milvus.search(
            collection_name=collection,
            anns_field="vector",
            data=[query],
            filter=filt 
            limit=3,
            search_params={"metric_type": "IP","offset":offset},
            output_fields=fields
        )

        for hits in res:
            for hit in hits:
                print(hit)
                
                # {
#             "id": 551,
#             "distance": 0.08821295201778412,
#             "entity": {"fields"}
#         },
        '''
        
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

        
    async def languageTranslate(self, request:LanguageTranslateRequest, context)-> LanguageTranslateResponse:
        try:
            translationPath = request.text.split(".")
            
        except Exception as e:
            log.warning(str(e))
            return LanguageTranslateResponse(text=str(e))