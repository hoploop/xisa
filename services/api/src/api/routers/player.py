# PYTHON IMPORTS
import logging
from typing import Annotated, Optional

# LIBRARY IMPORTS
from fastapi import status
from beanie import PydanticObjectId
from fastapi import APIRouter, Depends, HTTPException, Request

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
