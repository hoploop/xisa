# LOCAL IMPORTS
from common.service import Client
from common.rpc.vision_pb2_grpc import VisionStub
from common.rpc.base_pb2 import Ping, Pong


class VisionClient(Client):
    
    def __init__(self, security_config, client_config):
        super().__init__(security_config, client_config)
        self.client: VisionStub = VisionStub(self.channel)
        
    async def ping(self) -> Pong:
        pong: Pong = await self.client.ping(Ping())
        return pong
