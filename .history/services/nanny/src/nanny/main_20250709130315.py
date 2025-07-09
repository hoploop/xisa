import grpc
import time
import yaml
import subprocess
from grpc_health.v1 import health_pb2, health_pb2_grpc

class NannyService:
    def __init__(self, config_file):
        with open(config_file) as f:
            self.config = yaml.safe_load(f)
        self.services = self.config['services']
        self.check_interval = self.config.get('check_interval', 5)
        self.restart_cmd = self.config.get('restart_command')

    def check_service(self, name, host, port):
        channel = grpc.insecure_channel(f"{host}:{port}")
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

    def monitor_loop(self):
        while True:
            for svc in self.services:
                name, host, port = svc['name'], svc['host'], svc['port']
                is_up = self.check_service(name, host, port)
                if is_up:
                    print(f"[OK] {name} is up")
                else:
                    print(f"[DOWN] {name} is down!")
                    self.restart_service(name)
            time.sleep(self.check_interval)

if __name__ == "__main__":
    nanny = NannyService("conf/services.yaml")
    nanny.monitor_loop()