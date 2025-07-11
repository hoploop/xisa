
# PYTHON IMPORTS
from typing import Annotated

# LIBRARY IMPORTS
from uuid import uuid4
from fastapi import Depends, FastAPI, Request
from motor.motor_asyncio import AsyncIOMotorGridFSBucket


async def get_host(request: Request) -> str:
    return request.client.host

async def get_session(request:Request) -> str:
    session = request.headers.get('X-Session',str(uuid4()))
    return session

async def get_app(request: Request) -> FastAPI:
    return request.app

async def get_filesystem(request: Request) ->  AsyncIOMotorGridFSBucket:
    return request.app.state.fs

async def get_config(request: Request):
    return request.app.state.config

GetFilesystem = Annotated[AsyncIOMotorGridFSBucket,Depends(get_filesystem)]
GetHost = Annotated[str,Depends(get_host)]
GetSession = Annotated[str,Depends(get_session)]
GetApp = Annotated[FastAPI,Depends(get_app)]

