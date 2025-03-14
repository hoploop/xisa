# PYTHON IMPORTS
import io
import logging
import os
from typing import Annotated, List, Optional
from beanie import PydanticObjectId

# LIBRARY IMPORTS
from fastapi import APIRouter, Depends, HTTPException, Request,status
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from starlette.responses import Response


# LOCAL IMPORTS
from api.routers.auth import CurrentUser
from common.models.workspace import Project
from common.rpc.workspace_pb2 import CreateProjectRequest, DeleteProjectRequest, ListProjectRequest, LoadProjectRequest, UpdateProjectRequest
from common.rpc.workspace_pb2_grpc import WorkspaceStub
from common.service import secure_channel_factory
from common.utils.conversions import Conversions


# INITIALIZATION
router = APIRouter()
log = logging.getLogger(__name__)



async def get_workspace(request: Request) -> WorkspaceStub:
    if not hasattr(request.app.state, "workspace"):
        config = request.app.state.config.workspace
        channel = secure_channel_factory(
            security_config=config.security, client_config=config
        )
        request.app.state.workspace = WorkspaceStub(channel)
    return request.app.state.workspace


Workspace = Annotated[WorkspaceStub, Depends(get_workspace)]



@router.post(
    "/project/create",
    
    description="Performs the creation of a project",
    response_model=Project,
)
async def create_project(
    user: CurrentUser, workspace: Workspace, name: str, description: Optional[str] = ""
):
    req = CreateProjectRequest(user=str(user.id),name=name,description=description)
    res = await workspace.createProject(req)
    if res.status == False:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=res.message
        )
    return Conversions.deserialize(res.project)



@router.delete(
    "/project/delete",
    description="Performs the removal of a project",
    response_model=bool,
)
async def delete_project(user: CurrentUser, workspace: Workspace, id: str):
    req = DeleteProjectRequest(user=str(user.id),id=id)
    res = await workspace.deleteProject(req)
    if res.status == False:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=res.message
        )
    return res.status


@router.put(
    "/project/update",
    
    description="Performs the update of a project",
    response_model=bool,
)
async def update_project(
    user: CurrentUser,
    workspace: Workspace,
    id: str,
    name: str,
    description: Optional[str] = "",
):
    req = UpdateProjectRequest(user=str(user.id),id=id,name=name,description=description)
    res = await workspace.updateProject(req)
    if res.status == False:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=res.message
        )
    return res.status



class ProjectListResponse(BaseModel):
    projects: List[Project]
    total: int
    

@router.get(
    "/project/list",
    
    response_model=ProjectListResponse,
)
async def list_project(
    user: CurrentUser,
    workspace: Workspace,
    skip: int = 0,
    limit: int = 10,
    search: str = None,
):
    req = ListProjectRequest(user=str(user.id),skip=skip,limit=limit,search=search)
    res = await workspace.listProject(req)
    if res.status == False:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=res.message
        )
    total = res.total
    projects = []
    for project in res.projects:
        projects.append(Conversions.deserialize(project))
    return ProjectListResponse(total=total,projects=projects)



@router.get(
    "/project/load",
    response_model=Project,
)
async def load_project(
    user: CurrentUser,
    workspace: Workspace,
    id: str
):
    req = LoadProjectRequest(user=str(user.id),id=id)
    res = await workspace.loadProject(req)
    if res.status == False:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=res.message
        )
    return Conversions.deserialize(res.project)

    