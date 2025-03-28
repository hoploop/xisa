# PYTHON IMPORTS
import logging
from typing import Annotated, List, Optional
from beanie import PydanticObjectId

# LIBRARY IMPORTS
from fastapi import APIRouter, Depends, HTTPException, Request,status
from pydantic import BaseModel


# LOCAL IMPORTS
from api.routers.auth import CurrentUser
from common.clients.workspace import WorkspaceClient
from common.models.workspace import Project


# INITIALIZATION
router = APIRouter()
log = logging.getLogger(__name__)



async def get_workspace(request: Request) -> WorkspaceClient:
    if not hasattr(request.app.state, "workspace"):
        config = request.app.state.config.workspace
        request.app.state.workspace = WorkspaceClient(config)
        await request.app.state.workspace.startup()
    return request.app.state.workspace


Workspace = Annotated[WorkspaceClient, Depends(get_workspace)]



@router.post(
    "/project/create",
    operation_id="workspaceProjectCreate",
    description="Performs the creation of a project",
    response_model=Project,
)
async def project_create(
    user: CurrentUser, workspace: Workspace, name: str, description: Optional[str] = ""
):
    try:
        return await workspace.createProject(user,name,description)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=str(e)
        )



@router.delete(
    "/project/delete",
    operation_id="workspaceProjectDelete",
    description="Performs the removal of a project",
    response_model=bool,
)
async def project_delete(user: CurrentUser, workspace: Workspace, projectId: PydanticObjectId):
    try:
        return await workspace.deleteProject(user,projectId)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=str(e)
        )


@router.put(
    "/project/update",
    operation_id="workspaceProjectUpdate",
    description="Performs the update of a project",
    response_model=bool,
)
async def project_update(
    user: CurrentUser,
    workspace: Workspace,
    projectId: PydanticObjectId,
    name: str,
    description: Optional[str] = "",
):
    try:
        return await workspace.updateProject(user,projectId,name,description)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=str(e)
        )


class ProjectListResponse(BaseModel):
    projects: List[Project]
    total: int
    

@router.get(
    "/project/list",
    operation_id="workspaceProjectList",
    response_model=ProjectListResponse,
)
async def project_list(
    user: CurrentUser,
    workspace: Workspace,
    skip: int = 0,
    limit: int = 10,
    search: str = None,
):
    try:
        total, projects = await workspace.listProject(user,skip,limit,search)
        return ProjectListResponse(total=total,projects=projects)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=str(e)
        )



@router.get(
    "/project/load",
    operation_id="workspaceProjectLoad",
    response_model=Project,
)
async def project_load(
    user: CurrentUser,
    workspace: Workspace,
    projectId: PydanticObjectId
):
    try:
        return await workspace.loadProject(user,projectId)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=str(e)
        )

    