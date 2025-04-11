# PYTHON IMPORTS
import logging
from typing import Annotated, Optional

# LIBRARY IMPORTS
from fastapi import status
from beanie import PydanticObjectId
from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel

# LOCAL IMPORTS
from common.clients.player import PlayerClient

from api.routers.auth import CurrentUser


# INITIALIZATION
router = APIRouter()
log = logging.getLogger(__name__)



async def get_player(request: Request) -> PlayerClient:
    if not hasattr(request.app.state, "player"):
        config = request.app.state.config.player
        request.app.state.player = PlayerClient(config)
        await request.app.state.player.startup()
    return request.app.state.player


Player = Annotated[PlayerClient, Depends(get_player)]


@router.post("/generate/script", 
             operation_id="playerGenerateScript",
             response_model=str)
async def generate_script(
    user: CurrentUser,
    player: Player,
    recordId: PydanticObjectId,
    declarative: Optional[bool]=True,
    synthetic: Optional[bool]=False,
):
    try:
        return await player.playerScriptGenerate(user,recordId,declarative,synthetic)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))



@router.post("/run/script", 
             operation_id="playerRunScript",
             response_model=bool)
async def run_script(
    user: CurrentUser,
    player: Player,
    recordId: PydanticObjectId
):
    try:
        return await player.playerScriptExecute(user,recordId)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


class RawPayload(BaseModel):
    script: str

@router.post("/run/raw/script", 
             operation_id="playerRunRawScript",
             response_model=bool)
async def run_raw_script(
    user: CurrentUser,
    player: Player,
    payload: RawPayload
):
    try:
        return await player.playerRawScriptExecute(user,payload.script)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))




@router.put("/update/script", 
             operation_id="playerUpdateScript",
             response_model=str)
async def update_script(
    user: CurrentUser,
    player: Player,
    recordId: PydanticObjectId,
    script: str
):
    try:
        return await player.playerScriptUpdate(user,recordId,script)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))
