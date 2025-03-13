# PYTHON IMPORTS
import logging
from typing import Any, Callable, Sequence

# LIBRARY IMPORTS
import grpc
from grpc.aio import Metadata
from grpc_interceptor import AsyncServerInterceptor, ClientInterceptor
from grpc_interceptor.exceptions import GrpcException
from pydantic import BaseModel, Field

# LOCAL IMPORtS
from common.rpc.base_pb2 import Ping, Pong
from common.utils.config import Config

# INITIALIZATION
MAX_MESSAGE_LENGTH = -1#30 * 1024 * 1024
log = logging.getLogger(__name__)


class ExceptionInterceptor(AsyncServerInterceptor):

    def __init__(self, log):
        AsyncServerInterceptor.__init__(self)
        self.log = log

    async def intercept(
            self,
            method: Callable,
            request_or_iterator: Any,
            context: grpc.ServicerContext,
            method_name: str,
    ) -> Any:
        try:
            response_or_iterator = method(request_or_iterator, context)
            if not hasattr(response_or_iterator, "__aiter__"):
                # Unary, just await and return the response
                return await response_or_iterator
        except GrpcException as e:
            self.log.warning(str(e))
            context.set_code(e.status_code)
            context.set_details(e.details)
            raise
        except Exception as e:
            self.log.warning(str(e))
            context.set_code(grpc.StatusCode.CANCELLED)
            context.set_details(str(e))
            raise

        # Server streaming responses, delegate to an async generator helper.
        # Note that we do NOT await this.
        return self._intercept_streaming(response_or_iterator, context)

    async def _intercept_streaming(self, iterator, context):
        try:
            async for r in iterator:
                yield r
        except GrpcException as e:
            self.log.warning(str(e))
            context.set_code(e.status_code)
            context.set_details(e.details)
            

class SecurityConfig(BaseModel):
    cert: str
    key: str
    chain: str
    cn: str = 'pin'            

class ClientConfig(BaseModel):
    address: str
    cert: str
    key: str
    chain:str
    security: SecurityConfig


class ServiceConfig(Config):
    max_receive: int = Field(default=MAX_MESSAGE_LENGTH)
    max_send: int = Field(default=MAX_MESSAGE_LENGTH)
    address: str
    cn: str = None    
    security: SecurityConfig
    

def secure_channel_factory(security_config: SecurityConfig, client_config: ClientConfig, interceptors: Sequence[ClientInterceptor]|None=None) -> grpc.aio.Channel:
        if client_config.key not in Service.KEYS:
            Service.KEYS[client_config.key] = open(client_config.key, 'rb').read()
        key = Service.KEYS[client_config.key]

        if client_config.cert not in Service.CERTS:
            Service.CERTS[client_config.cert] = open(client_config.cert, 'rb').read()
        cert = Service.CERTS[client_config.cert]

        if security_config.chain not in Service.CHAINS:
            Service.CHAINS[security_config.chain] = open(security_config.chain, 'rb').read()
        chain = Service.CHAINS[security_config.chain]

        credentials = grpc.ssl_channel_credentials(root_certificates=chain,
                                                   private_key=key,
                                                   certificate_chain=cert)
        cert_cn = security_config.cn  # or parse it out of the cert data
        #MAX_MESSAGE_LENGTH = -1#30 * 1024 * 1024
        options = (('grpc.ssl_target_name_override', cert_cn),
                   ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
                   ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH),)
        return grpc.aio.secure_channel(client_config.address, credentials, options,None,interceptors)


def secure_credentials_factory(security_config: SecurityConfig) -> grpc.ServerCredentials:
    if security_config.key not in Service.KEYS:
        Service.KEYS[security_config.key] = open(security_config.key, 'rb').read()
    key = Service.KEYS[security_config.key]
    if security_config.cert not in Service.CERTS:
        Service.CERTS[security_config.cert] = open(security_config.cert, 'rb').read()
    cert = Service.CERTS[security_config.cert]
    return grpc.ssl_server_credentials([(key, cert)])    
     
class Client:
    
    def __init__(self,security_config: SecurityConfig, client_config: ClientConfig):
        self.channel = secure_channel_factory(security_config=secure_channel_factory,client_config=client_config)
        

class Service:
    KEYS = {}
    CERTS = {}
    CHAINS = {}
  
    @classmethod
    def bind_server(cls,server:grpc.aio.Server):
        pass    

    def secure_channel(self, security_config: SecurityConfig, client_config: ClientConfig) -> grpc.aio.Channel:
        return secure_channel_factory(security_config, client_config)

    def secure_credentials(self, security_config: SecurityConfig) -> grpc.ServerCredentials:
        return secure_credentials_factory(security_config)
        
    async def ping(self, request: Ping, context):
        log.debug('Received ping, answering with pong')
        return Pong(status=True)

    def meta(self,context,key:str):
        meta: Metadata = Metadata.from_tuple(context.invocation_metadata())
        if key in meta:
            return meta[key]
        return None
    
    def init(self):
        pass            
            
    async def start(self):
        pass
    
    async def stop(self):
        pass


    @property
    def options(self):
        ret = (
            ('grpc.max_send_message_length', self.config.max_send),
            ('grpc.max_receive_message_length', self.config.max_receive),)

        if self.config.cn:

            ret = (('grpc.ssl_target_name_override', self.config.cn),
                            ('grpc.max_send_message_length', self.config.max_send),
                            ('grpc.max_receive_message_length', self.config.max_receive),
                            )
        return ret
