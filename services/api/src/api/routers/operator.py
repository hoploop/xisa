# PYTHON IMPORTS
import logging
from typing import Annotated, Optional
from uuid import uuid4

# LIBRARY IMPORTS
from fastapi import status
from beanie import PydanticObjectId
from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel

# LOCAL IMPORTS
from common.clients.operator import OperatorClient

from api.routers.auth import CurrentUser
from api.routers import GetSession


# INITIALIZATION
router = APIRouter()
log = logging.getLogger(__name__)



async def get_operator(request: Request) -> OperatorClient:
    if not hasattr(request.app.state, "operator"):
        config = request.app.state.config.operator
        request.app.state.operator = OperatorClient(config)
        await request.app.state.operator.startup()
    return request.app.state.operator


Operator = Annotated[OperatorClient, Depends(get_operator)]



@router.post("/ask", 
             operation_id="operatorAsk",
             response_model=str)
async def ask(
    user: CurrentUser,
    operator: Operator,
    session: GetSession,
    message:str,
    
):
    try:
        return await operator.ask(user,session,message)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e))


