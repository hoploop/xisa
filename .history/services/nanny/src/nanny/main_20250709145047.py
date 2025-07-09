import asyncio
import logging
import os
from typing import Dict
import grpc
import time
from pydantic import BaseModel, Field
import yaml
import subprocess
from grpc_health.v1 import health_pb2, health_pb2_grpc
from common.models.defaults import empty_dict
from common.service import ClientConfig, SecurityConfig, ServiceConfig, secure_channel_factory
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
    security: SecurityConfig
    services: Dict[str,ClientConfig] = Field(default_factory=empty_dict)

class NannyService:
    def __init__(self, config: NannyConfig):
        self.config = config
        self.services = self.config['services']
        self.check_interval = self.config.interval
        #self.restart_cmd = self.config.get('restart_command')
        
    

    async def check_service(self, name):
        channel = secure_channel_factory(self.config.security,self.services[name])
        stub = health_pb2_grpc.HealthStub(channel)
        try:
            response = stub.Check(health_pb2.HealthCheckRequest(service=''), timeout=2)
            return response.status == health_pb2.HealthCheckResponse.SERVING
        except grpc.RpcError as e:
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
        while True:
            for name in self.services:
                is_up = await self.check_service(name)
                if is_up:
                    print(f"[OK] {name} is up")
                else:
                    print(f"[DOWN] {name} is down!")
                    #self.restart_service(name)
            time.sleep(self.check_interval)

if __name__ == "__main__":
    config = NannyConfig.factory(SERVICE_CONF,env)
    nanny = NannyService(config) 
    
    asyncio.run(nanny.monitor_loop())