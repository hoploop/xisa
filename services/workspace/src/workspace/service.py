# PYTHON IMPORTS
import logging
import traceback

# LIBRARY IMPORTS
from beanie import PydanticObjectId
from beanie.operators import And, Or, In, RegEx

# LOCAL IMPORTS
from common.models import MODELS
from common.models.workspace import Project
from common.rpc.workspace_pb2 import (
    CreateProjectRequest,
    CreateProjectResponse,
    DeleteProjectRequest,
    DeleteProjectResponse,
    ListProjectRequest,
    ListProjectResponse,
    LoadProjectRequest,
    LoadProjectResponse,
    UpdateProjectRequest,
    UpdateProjectResponse,
)
from common.rpc.workspace_pb2_grpc import WorkspaceServicer
from common.service import Service
from common.service import ServiceConfig
from common.utils.conversions import Conversions
from common.utils.mongodb import Mongodb, MongodbConfig

# INITIALIZATION
log = logging.getLogger(__name__)


class WorkspaceServiceConfig(ServiceConfig):
    database: MongodbConfig


class WorkspaceService(Service, WorkspaceServicer):

    def __init__(self, config: WorkspaceServiceConfig):
        WorkspaceServicer.__init__(self)
        Service.__init__(self)
        self.config: WorkspaceServiceConfig = config

    async def start(self):
        await Mongodb.initialize(self.config.database, MODELS)

    async def loadProject(
        self, request: LoadProjectRequest, context
    ) -> LoadProjectResponse:
        try:
            user_id = PydanticObjectId(request.user)
            found = await Project.find_many(
                Project.id == PydanticObjectId(request.id)
            ).first_or_none()
            if found is None:
                return LoadProjectResponse(
                    status=False, message="workspace.project.errors.not_found"
                )

            if user_id not in found.users:
                return LoadProjectResponse(
                    status=False, message="workspace.project.errors.delete_not_allowed"
                )

            return LoadProjectResponse(
                status=True, project=Conversions.serialize(found)
            )
        except Exception as e:
            log.warning(str(e))
            return LoadProjectResponse(status=False, message=str(e))

    async def createProject(
        self, request: CreateProjectRequest, context
    ) -> CreateProjectResponse:
        try:
            found = await Project.find_many(
                Project.name == request.name
            ).first_or_none()
            if found is not None:
                return CreateProjectResponse(
                    status=False, message="workspace.project.errors.already_existing"
                )
            project = await Project(
                name=request.name, description=request.description, users=[request.user]
            ).create()
            return CreateProjectResponse(
                status=True, project=Conversions.serialize(project)
            )
        except Exception as e:
            log.warning(str(e))
            return CreateProjectResponse(status=False, message=str(e))

    async def updateProject(
        self, request: UpdateProjectRequest, context
    ) -> UpdateProjectResponse:
        try:
            user_id = PydanticObjectId(request.user)
            found = await Project.find_many(
                Project.id == PydanticObjectId(request.id)
            ).first_or_none()
            if found is None:
                return UpdateProjectResponse(
                    status=False, message="workspace.project.errors.not_found"
                )

            others = await Project.find(
                Project.name == request.name, Project.id != PydanticObjectId(request.id)
            ).count()
            if others > 0:
                return UpdateProjectResponse(
                    status=False, message="workspace.project.errors.already_existing"
                )
            if user_id not in found.users:
                return UpdateProjectResponse(
                    status=False, message="workspace.project.errors.delete_not_allowed"
                )

            found.name = request.name
            found.description = request.description
            await found.save()
            return UpdateProjectResponse(status=True)
        except Exception as e:
            log.warning(str(e))
            return CreateProjectResponse(status=False, message=str(e))

    async def deleteProject(
        self, request: DeleteProjectRequest, context
    ) -> DeleteProjectResponse:
        try:
            found = await Project.find_many(
                Project.id == PydanticObjectId(request.id)
            ).first_or_none()
            if not found:
                return DeleteProjectResponse(
                    status=False, message="workspace.project.errors.not_found"
                )
            user_id = PydanticObjectId(request.user)
            if user_id not in found.users:
                return DeleteProjectResponse(
                    status=False, message="workspace.project.errors.delete_not_allowed"
                )
            await found.delete()
            return DeleteProjectResponse(status=True)
        except Exception as e:
            log.warning(str(e))
            return DeleteProjectResponse(status=False, message=str(e))

    async def listProject(
        self, request: ListProjectRequest, context
    ) -> ListProjectResponse:
        try:
            user_id = PydanticObjectId(request.user)
            qry = And(In(Project.users, [user_id]))
            if request.search is not None and request.search.strip() != "":
                qry = And(
                    In(Project.users, [user_id]),
                    Or(
                        RegEx(Project.name, request.search.strip(), options="i"),
                        RegEx(Project.description, request.search.strip(), options="i"),
                    ),
                )
            total = await Project.find(qry).count()
            projects = (
                await Project.find(qry)
                .skip(request.skip)
                .limit(request.limit)
                .sort(-Project.updated)
                .to_list()
            )
            ret = []
            for project in projects:
                ret.append(Conversions.serialize(project))
            return ListProjectResponse(status=True, total=total, projects=ret)
        except Exception as e:
            log.warning(str(e))
            print(traceback.format_exc())
            return ListProjectResponse(status=False, message=str(e))
