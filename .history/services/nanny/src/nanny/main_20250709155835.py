import asyncio
from datetime import datetime
import os
import signal
from typing import Dict
import grpc
import time
from pydantic import BaseModel, Field
import yaml
import subprocess
from grpc_health.v1._async import HealthServicer
from grpc_health.v1.health_pb2_grpc import add_HealthServicer_to_server
from grpc_health.v1 import health_pb2, health_pb2_grpc
from common.clients.api import ApiClient
from common.models.defaults import empty_dict
from common.rpc.nanny_pb2 import NannyServiceStatus, NannyStatusResponse
from common.rpc.nanny_pb2_grpc import NannyServicer, add_NannyServicer_to_server
from common.service import ClientConfig, ExceptionInterceptor, Service, ServiceConfig, secure_channel_factory
from common.utils.environment import Environment
from common.utils.log import Logger

# CONSTANTS
ENV_CONF = '../.env'
LOGGING_CONF = 'conf/logging.json'
SERVICE_CONF = 'conf/config.json'


# INITIALIZATION
os.chdir("../")
env = Environment(ENV_CONF)
logger = Logger.initialize(LOGGING_CONF)
log = logger.getLogger(__name__)

    

class NannyConfig(ServiceConfig):
    interval:int = 1000
    services: Dict[str,ClientConfig] = Field(default_factory=empty_dict)

class NannyMonitor:
    def __init__(self, config: NannyConfig):
        self.config = config
        
        #self.restart_cmd = self.config.get('restart_command')
        

        

class NannyService(Service, NannyServicer):

    def __init__(self, config: NannyConfig):
        NannyServicer.__init__(self)
        Service.__init__(self)
        self.config:NannyConfig = config     
        self.services = self.config.services
        self.check_interval = self.config.interval
        self.statuses = {}
        
        for key in self.services:
            self.statuses[key] = False
        
    async def nannyStatus(self, request, context):
        ss = []
        for key in self.statuses:
            ss.append(NannyServiceStatus(name=key,status=self.statuses[key]))
        return NannyStatusResponse(services=ss)
    
    async def start(self):
        asyncio.create_task(self.monitor_loop())
    
    
    async def check_service(self, name):
        
        
        try:
            channel = await secure_channel_factory(self.config.security,self.services[name])
            stub = health_pb2_grpc.HealthStub(channel)
            response = await asyncio.wait_for(
                stub.Check(health_pb2.HealthCheckRequest(service=''), timeout=2),
                timeout=4
            )
            return response.status == health_pb2.HealthCheckResponse.SERVING
        except grpc.RpcError as e:
            print(f"[ERROR] {name} is not responding: {e}")
            return False
        except asyncio.TimeoutError as e:
            print(f"[ERROR] {name} is not responding: {e}")
            return False
        except grpc.aio.AioRpcError as e:
            print(f"[ERROR] {name} is not responding: {e}")
            return False
        except Exception as e:
            print(f"[ERROR] {name} is not responding: {e}")
            return False

    def restart_service(self, name):
        if self.restart_cmd:
            cmd = self.restart_cmd.format(service=name)
            print(f"[INFO] Restarting {name} with: {cmd}")
            subprocess.run(cmd, shell=True)
        else:
            print(f"[WARN] No restart command defined for {name}")

    async def monitor_loop(self):
        await self.api.startup()
        # Handle graceful shutdown
        stop_event = asyncio.Event()

        def handle_signal(*_):
            log.info("Shutting down gracefully...")
            stop_event.set()
            
        # Listen for termination signals
        loop = asyncio.get_running_loop()
        loop.add_signal_handler(signal.SIGINT, handle_signal)
        loop.add_signal_handler(signal.SIGTERM, handle_signal)


        while not stop_event.is_set():
            now = datetime.now()
            print("======= NANNY CHECK: "+now.strftime("%Y-%m-%d %H:%M:%S"))
            for name in self.services:
                is_up = await self.check_service(name)
                if is_up:
                    self.statuses[name] = True
                    print(f"[OK] {name} is up")
                else:
                    print(f"[DOWN] {name} is down!")
                    self.statuses[name] = False
                    #self.restart_service(name)
            await asyncio.sleep(self.check_interval)
            
        # Wait for termination signal
        await stop_event.wait()



async def main():    
    # Initting and loading the API RPC Service, to be used mainly for async ws calls
    log.info('Initting and starting up API RPC Service')
    service = NannyService(config)
    await service.start() 
    server = grpc.aio.server(interceptors=[ExceptionInterceptor(log)],options=service.options)
    add_NannyServicer_to_server(service, server)
    add_HealthServicer_to_server(HealthServicer(), server)
    log.info('Starting rpc service on address: {0}'.format(config.address)) 
    server.add_secure_port(config.address,service.secure_credentials(config.security)) 
    await server.start()
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


if __name__ == "__main__":
    config = NannyConfig.factory(SERVICE_CONF,env)
    nanny = NannyMonitor(config) 
    
    asyncio.run(nanny.monitor_loop())