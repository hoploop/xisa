# PYTHON IMPORTS
import asyncio
import functools
import logging
import time
from typing import Any, Callable, Sequence
from typing import Type

# LIBRARY IMPORTS
import grpc
from grpc.aio import Metadata
from grpc_interceptor import AsyncServerInterceptor, ClientInterceptor
from grpc_interceptor.exceptions import GrpcException
from pydantic import BaseModel, Field
from grpc import aio
from grpc import StatusCode

# LOCAL IMPORtS
from common.rpc.base_pb2 import Ping, Pong
from common.utils.config import Config

# INITIALIZATION
MAX_MESSAGE_LENGTH = -1  # 30 * 1024 * 1024
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
    cn: str = "pin"


class ClientConfig(BaseModel):
    address: str
    cert: str
    key: str
    chain: str
    security: SecurityConfig


class ServiceConfig(Config):
    max_receive: int = Field(default=MAX_MESSAGE_LENGTH)
    max_send: int = Field(default=MAX_MESSAGE_LENGTH)
    address: str
    cn: str = None
    security: SecurityConfig


async def secure_channel_factory(
    security_config: SecurityConfig,
    client_config: ClientConfig,
    interceptors: Sequence[ClientInterceptor] | None = None,
    max_retries=5,
    retry_delay=3,
    timeout=30,
) -> grpc.aio.Channel:
    if client_config.key not in Service.KEYS:
        Service.KEYS[client_config.key] = open(client_config.key, "rb").read()
    key = Service.KEYS[client_config.key]

    if client_config.cert not in Service.CERTS:
        Service.CERTS[client_config.cert] = open(client_config.cert, "rb").read()
    cert = Service.CERTS[client_config.cert]

    if security_config.chain not in Service.CHAINS:
        Service.CHAINS[security_config.chain] = open(security_config.chain, "rb").read()
    chain = Service.CHAINS[security_config.chain]

    credentials = grpc.ssl_channel_credentials(
        root_certificates=chain, private_key=key, certificate_chain=cert
    )
    cert_cn = security_config.cn  # or parse it out of the cert data
    # MAX_MESSAGE_LENGTH = -1#30 * 1024 * 1024
    options = (
        ("grpc.ssl_target_name_override", cert_cn),
        ("grpc.max_send_message_length", MAX_MESSAGE_LENGTH),
        ("grpc.keepalive_timeout_ms", 5000),  # 5 seconds
        # ('grpc.enable_retries', 0),
        ("grpc.max_receive_message_length", MAX_MESSAGE_LENGTH),
    )

    retries = 0
    while retries < max_retries:
        try:

            # Create secure channel with credentials
            channel = grpc.aio.secure_channel(
                client_config.address, credentials, options, None, interceptors
            )

            # Wait until the channel is ready
            #await asyncio.wait_for(channel.channel_ready(), timeout=timeout)
            log.debug(f"Connected to {client_config.address} securely!")
            return channel

        except grpc.FutureTimeoutError:
            print(f"Connection failed. Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
            retries += 1
            retry_delay *= 2  # Exponential backoff

    raise Exception(f"Could not connect to {client_config.address} after several retries.")


def secure_credentials_factory(
    security_config: SecurityConfig,
) -> grpc.ServerCredentials:
    if security_config.key not in Service.KEYS:
        Service.KEYS[security_config.key] = open(security_config.key, "rb").read()
    key = Service.KEYS[security_config.key]
    if security_config.cert not in Service.CERTS:
        Service.CERTS[security_config.cert] = open(security_config.cert, "rb").read()
    cert = Service.CERTS[security_config.cert]
    return grpc.ssl_server_credentials([(key, cert)])


RETRYABLE_CODES = {
    StatusCode.UNAVAILABLE,
    StatusCode.DEADLINE_EXCEEDED,
    StatusCode.RESOURCE_EXHAUSTED,
    StatusCode.INTERNAL,
}


class Client:

    def __init__(
        self,
        client_config: ClientConfig,
        retry_attempts: int = 5,
        retry_backoff: float = 1.0,
        monitor_interval: float = 3.0,
    ):
        self.config = client_config
        self.retry_attempts = retry_attempts
        self.retry_backoff = retry_backoff
        self.monitor_interval = monitor_interval
        self._shutdown = asyncio.Event()
        self._ready = asyncio.Event()  # Set when channel READY

    async def startup(self):
        self.channel = await secure_channel_factory(
            security_config=self.config.security, client_config=self.config
        )
        asyncio.create_task(self._monitor_channel_state())

    async def _monitor_channel_state(self):
        """Monitor channel state and handle reconnections"""
        while not self._shutdown.is_set():
            state = self.channel.get_state(try_to_connect=True)
            #log.debug(f"{self.config.address} state: {state.name}")
            if state == grpc.ChannelConnectivity.READY:
                if not self._ready.is_set():
                    log.info(f"{self.config.address} is READY.")
                    self._ready.set()
            else:
                if self._ready.is_set():
                    log.warning(
                        f"{self.config.address} is {state.name}. Blocking calls until READY."
                    )
                    self._ready.clear()
            await asyncio.sleep(self.monitor_interval)

    async def stop(self):
        self._shutdown.set()
        if self.channel:
            await self.channel.close()

    async def _wait_until_ready(self, timeout: float = 10.0):
        """Block until channel is READY or timeout"""
        try:
            await asyncio.wait_for(self._ready.wait(), timeout=timeout)
        except asyncio.TimeoutError:
            raise RuntimeError(f"{self.config.address} not ready within timeout.")


def retry_rpc_call(timeout: float = 10.0):
    """
    Async decorator for retrying RPC calls with channel readiness check.

    Args:
        timeout (float): Time in seconds to wait for channel readiness.
    """
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(self, *args, **kwargs):
            await self._wait_until_ready(timeout)
            for attempt in range(1, self.retry_attempts + 1):
                try:
                    return await func(self, *args, **kwargs)
                except aio.AioRpcError as e:
                    if e.code() in RETRYABLE_CODES:
                        log.warning(
                            f"RPC failed ({e.code().name}), retrying {attempt}/{self.retry_attempts}..."
                        )
                        await asyncio.sleep(self.retry_backoff * attempt)
                        continue
                    else:
                        log.error(f"RPC failed (non-retryable): {e.code().name}")
                        raise
            raise RuntimeError(f"RPC failed after {self.retry_attempts} attempts.")
        return wrapper
    return decorator

class Service:
    KEYS = {}
    CERTS = {}
    CHAINS = {}

    @classmethod
    def bind_server(cls, server: grpc.aio.Server):
        pass

    async def secure_channel(
        self, security_config: SecurityConfig, client_config: ClientConfig
    ) -> grpc.aio.Channel:
        return await secure_channel_factory(security_config, client_config)

    def secure_credentials(
        self, security_config: SecurityConfig
    ) -> grpc.ServerCredentials:
        return secure_credentials_factory(security_config)

    async def ping(self, request: Ping, context):
        log.debug("Received ping, answering with pong")
        return Pong(status=True)

    def meta(self, context, key: str):
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
            ("grpc.max_send_message_length", self.config.max_send),
            ("grpc.max_receive_message_length", self.config.max_receive),
        )

        if self.config.cn:

            ret = (
                ("grpc.ssl_target_name_override", self.config.cn),
                ("grpc.max_send_message_length", self.config.max_send),
                ("grpc.max_receive_message_length", self.config.max_receive),
            )
        return ret
