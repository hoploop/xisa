# PYTHON IMPORTS
import logging
from typing import List, Optional, Tuple

from beanie import PydanticObjectId

# LOCAL IMPORTS
from common.models.auth import User
from common.rpc.base_pb2 import Ping, Pong
from common.rpc.language_pb2 import LanguageDecodeRequest, LanguageDecodeResponse, LanguageEncodeRequest, LanguageEncodeResponse, LanguageTranslateRequest, LanguageTranslateResponse
from common.rpc.language_pb2_grpc import LanguageStub
from common.service import Client

# INITIALIZATION
log = logging.getLogger(__name__)

class LanguageClient(Client):
    
    def __init__(self, client_config):
        super().__init__(client_config)
        
    async def startup(self):
        await super().startup()
        self.client = LanguageStub(self.channel)
        
    async def ping(self) -> Pong:
        req = Ping()
        res = await self.client.ping(req)
        return res
    
    async def languageEncode(self,user:User,text:str)-> List[int]:
        req = LanguageEncodeRequest(user=str(user.id),text=text)
        res: LanguageEncodeResponse = await self.client.languageEncode(req)
        if res.status == False:
            raise Exception(str(res.message))
        return res.tokens
    
    
    async def languageDecode(self,user:User,tokens:List[int])-> str:
        req = LanguageDecodeRequest(user=str(user.id),tokens=tokens)
        res: LanguageDecodeResponse = await self.client.languageDecode(req)
        if res.status == False:
            raise Exception(str(res.message))
        return res.text
    
    async def languageTranslate(self,lang:str,text:str)->str:
        req = LanguageTranslateRequest(lang=lang,text=text)
        res: LanguageTranslateResponse = await self.client.languageTranslate(req)
        return res.text
    
    
        