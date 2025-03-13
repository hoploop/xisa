# PYTHON IMPORTS
import os
import asyncio
import signal


# RPC IMPORTS
import grpc
from grpc_health.v1._async import HealthServicer
from grpc_health.v1.health_pb2_grpc import add_HealthServicer_to_server
from common.rpc.player_pb2_grpc import add_PlayerServicer_to_server
import grpc

# LOCAL IMPORTS
from common.service import ExceptionInterceptor
from common.utils.log import Logger
from common.utils.environment import Environment
from player.service import PlayerService, PlayerServiceConfig
 
# CONSTANTS
ENV_CONF = '../.env'
LOGGING_CONF = 'conf/logging.json'
SERVICE_CONF = 'conf/config.json'


# INITIALIZATION

os.chdir("../")
env = Environment(ENV_CONF)
logger = Logger.initialize(LOGGING_CONF)
log = logger.getLogger(__name__)
config = PlayerServiceConfig.factory(SERVICE_CONF,env)



async def main():    
    # Initting and loading the API RPC Service, to be used mainly for async ws calls
    log.info('Initting and starting up API RPC Service')
    service = PlayerService(config)
    await service.start() 
    server = grpc.aio.server(interceptors=[ExceptionInterceptor(log)],options=service.options)
    add_PlayerServicer_to_server(service, server)
    add_HealthServicer_to_server(HealthServicer(), server)
    log.info('Starting rpc service on address: {0}'.format(config.address)) 
    server.add_secure_port(config.address,service.secure_credentials(config.security)) 
    log.info("Server started: {0}".format(config.address))
    
   # Handle graceful shutdown
    stop_event = asyncio.Event()

    def handle_signal(*_):
        log.info("Shutting down gracefully...")
        stop_event.set()

    # Listen for termination signals
    loop = asyncio.get_running_loop()
    loop.add_signal_handler(signal.SIGINT, handle_signal)
    loop.add_signal_handler(signal.SIGTERM, handle_signal)

    # Wait for termination signal
    await stop_event.wait()
    
    # Gracefully shut down the server
    await server.stop(5)  # 5 seconds to allow ongoing requests to finish
    log.info("Server shut down.")
    log.debug("Server stopped: {0}".format(config.address))



if __name__ == '__main__':
    asyncio.run(main())