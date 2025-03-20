# PYTHON IMPORTS
from typing import Any, List

# LIBRARY IMPORTS
from fastapi import FastAPI, Request
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware


# LOCAL IMPORTS
from common.models.defaults import empty_list

class CORSConfig(BaseModel):
    origins: List[str] = []
    allow_credentials: bool = True
    allow_methods: List[str] = []
    allow_headers: List[str] = []

class ApiConfig(BaseModel):
    cors: CORSConfig
    openapi_url: str
    version:str
    title:str
    description:str
    summary:str
    swagger_persistent: bool = False
    terms_of_service: str = "http://example.com/terms/"
    contact: dict = {"name": "Hoploop",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    }
    license_info: dict = {
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }
    tags: List[Any] = Field(default_factory=empty_list)

class Api:
    
    @staticmethod
    async def locale_middleware(request: Request, call_next):
        locale = request.headers.get("X-Locale", "en")
        response = await call_next(request)
        # response.headers['X-Locale'] = 'kajsdhkjqhe'
        return response


    @staticmethod
    async def session_middleware(request: Request, call_next):
        session = request.headers.get("X-Session", "")
        response = await call_next(request)
        return response

    
    @staticmethod
    def initialize(config:ApiConfig,lifespan) -> FastAPI:
        app = FastAPI(
            title=config.title,
            description=config.description,
            summary=config.summary,
            version=config.version,
            terms_of_service=config.terms_of_service,
            contact=config.contact,
            license_info=config.license_info,
            openapi_tags=config.tags,
            swagger_ui_parameters={"persistAuthorization": config.swagger_persistent},
            openapi_url=config.openapi_url,
            lifespan=lifespan,
            
        )
        
            
        app.add_middleware(
            CORSMiddleware,
            allow_origins=config.cors.origins,
            allow_credentials=config.cors.allow_credentials,
            allow_methods=config.cors.allow_methods,
            allow_headers=config.cors.allow_headers,
            expose_headers=["X-Locale", "X-Session",'Content-Range'],
        )

        app.add_middleware(BaseHTTPMiddleware, dispatch=Api.locale_middleware)
        app.add_middleware(BaseHTTPMiddleware, dispatch=Api.session_middleware)
        return app