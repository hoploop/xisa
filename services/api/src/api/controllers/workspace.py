
# PYTHON IMPORTS
from typing import Annotated, List, Tuple
import logging

# LIBRARY IMPORTS
from beanie import PydanticObjectId
from beanie.operators import And, Or, In, RegEx
from fastapi import Depends, HTTPException, Request,status

# LOCAL IMPORTS
from api.models.auth import User, Group
from api.models.workspace import Project

# INITIALIZATION
log = logging.getLogger


class WorkspaceController:
    pass
    
        

async def get_workspace(request: Request) ->  WorkspaceController:
    if not hasattr(request.app.state,'workspace'):
        request.app.state.workspace = WorkspaceController()
    return request.app.state.workspace

Workspace = Annotated[WorkspaceController,Depends(get_workspace)]