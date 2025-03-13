
# PYTHON IMPORTS
import logging
from typing import Annotated, List, Tuple

# LIBRARY IMPORTS
from beanie import PydanticObjectId
from beanie.operators import And,Or,In,RegEx
from fastapi import Depends, HTTPException, Request, status
from pydantic import BaseModel

# LOCAL IMPORTS
from common.models.workspace import Project
from common.models.auth import Group

# INITIALIZATION
log = logging.getLogger(__name__)

class ProjectControllerConfig(BaseModel):
    pass

class ProjectController:
    
    def __init__(self,config:ProjectControllerConfig):
        self.config: ProjectControllerConfig = config
        
    async def create(self,user_id:PydanticObjectId,name:str,description:str='') -> Project:
        project = await Project(name=name,description=description,users=[user_id]).create()
        return project
    
    async def update(self,project_id:PydanticObjectId,name:str,description:str='') -> Project:
        project = await Project.find_many(Project.id ==  project_id).first_or_none()
        if project is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Project not found",
                headers={"WWW-Authenticate": "Bearer"},)
        project.name = name
        project.description = description
        await project.save()
        return project
    
    
    async def remove(self,project_id:PydanticObjectId) -> bool:
        project = await Project.find_many(Project.id ==  project_id).first_or_none()
        if project is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Project not found",
                headers={"WWW-Authenticate": "Bearer"},)
        
        await project.delete()
        return True
    
    async def assign_to_group(self,group_id:PydanticObjectId,project_id:PydanticObjectId) -> bool:
        project = await Project.find_many(Project.id ==  project_id).first_or_none()
        group = await Group.find_many(Group.id ==  group_id).first_or_none()
        if project is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Project not found",
                headers={"WWW-Authenticate": "Bearer"},
            )
        if group is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Group not found",
                headers={"WWW-Authenticate": "Bearer"},
            )
        if group.id not in project.groups:
            project.groups.append(group.id)
            await project.save()
            return True
        return False
    
    async def load(self,project_id: PydanticObjectId) -> Project:
        project = await Project.find_many(Project.id ==  project_id).first_or_none()
        if project is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Project not found",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return project

    async def list_by_user(self,user_id: PydanticObjectId, skip:int=0, limit:int=10, search:str=None) -> Tuple[int,List[Project]]:
        qry = And(In(Project.users,[user_id]))
        if search is not None:
            qry = And(In(Project.users,[user_id]),Or(RegEx(Project.name,search,options="i"),RegEx(Project.description,search,options="i")))
        total = await Project.find(qry).count()
        projects = await Project.find(qry).skip(skip).limit(limit).to_list()
        return [total,projects]
    


async def get_project_controller(request: Request) ->  ProjectController:
    if not hasattr(request.app.state,'project'):
        request.app.state.project = ProjectController(request.app.state.config.project)
    return request.app.state.project

GetProjectController = Annotated[ProjectController,Depends(get_project_controller)]    