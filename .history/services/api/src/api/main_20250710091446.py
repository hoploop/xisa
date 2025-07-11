# PYTHON IMPORTS

# LIBRARY IMPORTS
import re
from typing import Any
from fastapi import FastAPI, Response
from fastapi.routing import APIRoute
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
import grpc
from grpc_health.v1._async import HealthServicer
from grpc_health.v1.health_pb2_grpc import add_HealthServicer_to_server


# LOCAL IMPORTS
from common.models import MODELS
from common.rpc.api_pb2_grpc import add_ApiServicer_to_server
from common.service import ClientConfig, ExceptionInterceptor
from common.utils.environment import Environment
from common.utils.log import Logger
from common.utils.config import Config
from api.controllers.api import Api, ApiConfig
from api.routers.ws import manager as ws_manager
from api.routers import ws
from api.routers import auth
from api.routers import player
from api.routers import detector
from api.routers import recorder
from api.routers import operator
from api.routers import language
from api.service import ApiService, ApiServiceConfig
from common.utils.mongodb import Mongodb, MongodbConfig
from api.routers import trainer
from api.routers import project
from api.routers import root

# CONSTANTS
ENV_CONF = "../.env"
LOGGING_CONF = "conf/logging.json"
API_CONF = "conf/config.json"


# CONFIG
class MainConfig(Config):
    workspace: ClientConfig
    auth: ClientConfig
    api: ApiConfig
    recorder: ClientConfig
    translations: str
    detector: ClientConfig
    operator: ClientConfig
    player: ClientConfig
    trainer: ClientConfig
    language: ClientConfig
    service: ApiServiceConfig
    database: MongodbConfig
    

# INITIALIZATION
env = Environment(ENV_CONF)
logger = Logger.initialize(LOGGING_CONF)
log = logger.getLogger(__name__)
config = MainConfig.factory(API_CONF, env)


# LIFECYCLE
@asynccontextmanager
async def lifespan(app: FastAPI):
    log.info("Starting up")
    app.state.config = config
    
    await Mongodb.initialize(config.database,MODELS)
    
    log.info('Initting and starting up API RPC Service')
    service = ApiService(config.service,ws_manager)
    await service.start() 
    server = grpc.aio.server(interceptors=[ExceptionInterceptor(log)],options=service.options)
    add_ApiServicer_to_server(service, server)
    add_HealthServicer_to_server(HealthServicer(), server)
    log.info('Starting rpc service on address: {0}'.format(config.service.address)) 
    server.add_secure_port(config.service.address,service.secure_credentials(config.service.security)) 
    log.info("Server started: {0}".format(config.service.address))
    await server.start()

    
    yield
    # Shutdown
    await server.stop(grace=1)

    log.info("Shutting down")

    log.info("Shutting down websocket manager")
    await ws_manager.stop()

    log.debug("Server stopped")


# API App
app = Api.initialize(config.api, lifespan)


# MIDDLEWARES


def to_camel_case(snake_str):
    """Convert snake_case to camelCase."""
    components = snake_str.split("_")
    return components[0] + "".join(x.title() for x in components[1:])


def generate_operation_id(route):
    """Generate a short, unique, camelCase operation_id."""
    path = re.sub(r"[/{}/]", "_", route.path).strip(
        "_"
    )  # Convert path to a safe string
    operation_id_snake = f"{path}"  # Example: 'get_items_item_id'
    return to_camel_case(operation_id_snake)  # Convert to camelCase


def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            if hasattr(route, "path"):
                route.operation_id = generate_operation_id(route)


class StaticFilesCache(StaticFiles):
    def __init__(
        self, *args, cachecontrol="public, max-age=0, s-maxage=0, immutable", **kwargs
    ):
        self.cachecontrol = "max-age=0, no-cache, no-store, , must-revalidate"
        self.pragma = "no-cache"
        self.expires = "0"
        super().__init__(*args, **kwargs)

    def file_response(self, *args: Any, **kwargs: Any) -> Response:
        resp = super().file_response(*args, **kwargs)
        resp.headers.setdefault("Cache-Control", self.cachecontrol)
        resp.headers.setdefault("Pragma", self.pragma)
        resp.headers.setdefault("Expires", self.expires)
        return resp


# ROUTERS
app.mount("/i18n", StaticFilesCache(directory=config.translations), name="static")
app.include_router(ws.router, tags=["ws"], prefix="/ws")
app.include_router(root.router)
app.include_router(auth.router, tags=["auth"], prefix="/auth")
app.include_router(detector.router, tags=["detector"], prefix="/detector")
app.include_router(project.router, tags=["project"], prefix="/project")
app.include_router(recorder.router, tags=["recorder"], prefix="/recorder")
app.include_router(player.router, tags=["player"], prefix="/player")
app.include_router(trainer.router, tags=["trainer"], prefix="/trainer")
app.include_router(operator.router, tags=["operator"], prefix="/operator")
app.include_router(language.router, tags=["language"], prefix="/language")
#use_route_names_as_operation_ids(app)
