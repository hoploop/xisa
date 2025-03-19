# PYTHON IMPORTS
import logging
from typing import List, Optional, Tuple
from beanie import PydanticObjectId

# LOCAL IMPORTS
from common.models.auth import User
from common.models.workspace import Project
from common.rpc.base_pb2 import Ping, Pong
from common.rpc.workspace_pb2 import CreateProjectRequest, DeleteProjectRequest, ListProjectRequest, LoadProjectRequest, UpdateProjectRequest
from common.rpc.workspace_pb2_grpc import WorkspaceStub
from common.service import Client
from common.utils.conversions import Conversions

# INITIALIZATION
log = logging.getLogger(__name__)

class WorkspaceClient(Client):
    
    def __init__(self, client_config):
        super().__init__(client_config)
        
            
    async def startup(self):
        await super().startup()
        self.client = WorkspaceStub(self.channel)
        
    async def ping(self) -> Pong:
        req = Ping()
        res = await self.client.ping(req)
        return res
    
    async def createProject(self,user:User,name:str,description:str) -> Project:
        req = CreateProjectRequest(user=str(user.id),name=name,description=description)
        res = await self.client.createProject(req)
        if res.status == False:
            raise Exception(res.message)
        return Conversions.deserialize(res.project)
    
    async def deleteProject(self,user:User,projectId: PydanticObjectId) -> bool:
        req = DeleteProjectRequest(user=str(user.id),id=str(projectId))
        res = await self.client.deleteProject(req)
        if res.status == False:
            raise Exception(res.message)
        return res.status
    
    async def updateProject(self,user:User,projectId: PydanticObjectId,name:str,description:str) -> bool:
        req = UpdateProjectRequest(user=str(user.id),id=str(projectId),name=name,description=description)
        res = await self.client.updateProject(req)
        if res.status == False:
            raise Exception(res.message)
        return res.status

    async def listProject(self,user:User,skip:int,limit:int,search:str) -> Tuple[int,List[Project]]:
        req = ListProjectRequest(user=str(user.id),skip=skip,limit=limit,search=search)
        res = await self.client.listProject(req)
        if res.status == False:
            raise Exception(res.message)
        total = res.total
        projects = []
        for project in res.projects:
            projects.append(Conversions.deserialize(project))
        return total,projects
    
    
    async def loadProject(self,user:User,projectId:PydanticObjectId) -> Optional[Project]:
        req = LoadProjectRequest(user=str(user.id),id=str(projectId))
        res = await self.client.loadProject(req)
        if res.status == False:
            raise Exception(res.message)
        return Conversions.deserialize(res.project)