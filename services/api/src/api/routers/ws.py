# PYTHON IMPORTS
import json
import logging
from typing import Annotated, Dict, List, Union

# LIBRARY IMPORTS
from fastapi import (
    APIRouter,
    Depends,
    Request,
    WebSocket,
    Cookie,
    Query,
    WebSocketException,
    status,
    WebSocketDisconnect,
)
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from common.models.ws import WS_MESSAGES

# INITIALIZATION
router = APIRouter()
log = logging.getLogger(__name__)


async def get_cookie_or_token(
    websocket: WebSocket,
    session: Annotated[str | None, Cookie()] = None,
    token: Annotated[str | None, Query()] = None,
):
    if session is None and token is None:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
    return session or token



class WsManager:
    def __init__(self):
        self.session_connections: Dict[str, WebSocket] = {}
        self.token_connections: Dict[str,List[WebSocket]] = {}
        self.active_connections: list[WebSocket] = []    
        
    async def stop(self):
        for websocket in self.active_connections:
            await websocket.close()
        
    @staticmethod
    async def get_from_ws(request):
        return request.app.state.ws
        
    
    async def connect(self, session: str, token: str|None,websocket: WebSocket):
        log.info('Connecting websocket: {0}'.format(session))
        
        await websocket.accept()
        self.active_connections.append(websocket)
        self.session_connections[session] = websocket
        if token is not None:
            if token in self.token_connections:
                self.token_connections[token].append(websocket)
            else:
                self.token_connections[token] = [websocket]

    async def disconnect(self, session:str, token:str|None,websocket: WebSocket):
        log.info('Disconnecting websocket: {0}'.format(session))
        self.active_connections.remove(websocket)
        if session in self.session_connections:
            del self.session_connections[session]
        if token is not None and token in self.token_connections:
            del self.token_connections[token]

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    
    async def update(self,data: BaseModel, session: str) -> bool:
        if session not in self.session_connections: return False
        await self.session_connections[session].send_text(json.dumps(jsonable_encoder(data)))
        return True
    
    
    async def broadcast(self, data: BaseModel) -> bool:
        for connection in self.active_connections:
            await connection.send_text(json.dumps(jsonable_encoder(data)))
        return True


    async def sessions(self,tokens:List[str], data: BaseModel) -> bool:
        for token in tokens:
            if token in self.token_connections:
                connection = self.token_connections[token]
                await connection.send_text(json.dumps(jsonable_encoder(data)))
        return True

manager = WsManager()


async def get_websocket(request: Request) -> WsManager:

    if not hasattr(request.app.state, "ws"):
        request.app.state.ws = manager
        return manager
    return request.app.state.ws


Websocket = Annotated[WsManager, Depends(get_websocket)]

@router.get('/models',response_model=WS_MESSAGES)
async def websocket_models():
    return None

@router.websocket("/connection/{session}")
async def websocket_endpoint(
    websocket: WebSocket,
    session: str,
    token: Annotated[str | None, Query()] = None,
):
    await manager.connect(session, token, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            jsoned = json.loads(json.loads(data))
            user = None

    except WebSocketDisconnect:
        await manager.disconnect(session, token, websocket)
        # await manager.broadcast(f"Client #{session} left the chat")

