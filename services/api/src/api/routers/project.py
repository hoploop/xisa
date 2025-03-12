# PYTHON IMPORTS
import logging
from typing import Optional
from beanie import PydanticObjectId

# LIBRARY IMPORTS
from fastapi import APIRouter

# LOCAL IMPORTS
from api.models.workspace import Project, ProjectListResponse
from api.routers.auth import CurrentUser
from api.controllers.recorder import GetRecorderController
from api.controllers.project import GetProjectController


# INITIALIZATION
router = APIRouter()
log = logging.getLogger(__name__)


@router.post(
    "/create",
    
    description="Performs the creation of a project",
    response_model=Project,
)
async def create(
    user: CurrentUser, projectController: GetProjectController, name: str, description: Optional[str] = ""
):
    return await projectController.create(user.id, name, description)


@router.delete(
    "/delete",
    
    description="Performs the creation of a project",
    response_model=bool,
)
async def delete(user: CurrentUser, projectController: GetProjectController, id: str):
    return await projectController.remove(PydanticObjectId(id))


@router.put(
    "/update",
    
    description="Performs the creation of a project",
    response_model=Project,
)
async def update(
    user: CurrentUser,
    projectController: GetProjectController,
    id: str,
    name: str,
    description: Optional[str] = "",
):
    return await projectController.update(PydanticObjectId(id), name, description)


@router.get(
    "/list/user",
    
    response_model=ProjectListResponse,
)
async def list_by_user(
    user: CurrentUser,
    projectController: GetProjectController,
    skip: int = 0,
    limit: int = 10,
    search: str = None,
):
    total, projects = await projectController.list_by_user(
        user.id, skip, limit, search
    )
    return ProjectListResponse(total=total, projects=projects)


@router.get(
    "/record/count/{project_id}",
    
    response_model=int,
)
async def record_count(
    project_id: str,
    user: CurrentUser,
    projectController: GetProjectController,
    recorderController: GetRecorderController,
):
    return await recorderController.count_records(user.id, PydanticObjectId(project_id))


@router.get("/load",  response_model=Project)
async def load(user: CurrentUser, projectController: GetProjectController, id: str):
    return await projectController.load(PydanticObjectId(id))
