# PYTHON IMPORTS
import logging

# LOCAL IMPORTS
from common.rpc.api_pb2 import NannyUpdateRequest, NannyUpdateResponse, UpdateSessionRequest, UpdateSessionResponse
from common.rpc.api_pb2_grpc import ApiServicer
from common.service import Service, ServiceConfig
from api.routers.ws import WsManager
from common.utils.conversions import Conversions

# INITIALIZATION
log = logging.getLogger(__name__)

class ApiServiceConfig(ServiceConfig):
    pass

class ApiService(Service, ApiServicer):

    def __init__(self, config: ApiServiceConfig,ws: WsManager):
        ApiServicer.__init__(self)
        Service.__init__(self)
        self.config:ApiServiceConfig = config
        self.ws: WsManager = ws
        self.services = {}
        
    async def updateSession(self, request: UpdateSessionRequest, context) -> UpdateSessionResponse:
        try:
            log.debug('Update:')
            document = Conversions.deserialize(request.document)
            await self.ws.update(document,request.session)
            return UpdateSessionResponse(status=True)
        except Exception as e:
            log.warning(str(e))
            return UpdateSessionResponse(status=False,message=str(e))
        
        
    async def nannyUpdate(self, request:NannyUpdateRequest,context)-> NannyUpdateResponse:
        self.services[request.service] = request.status
        return NannyUpdateResponse(status=True)