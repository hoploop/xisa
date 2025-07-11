# INITIALIZATION
import logging

from common.rpc.storage_pb2_grpc import StorageStub


log = logging.getLogger(__name__)


class StorageClient(Client):

    def __init__(self, client_config):
        super().__init__(client_config)

    async def startup(self):
        await super().startup()
        self.client = StorageStub(self.channel)
