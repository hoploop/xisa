# PYTHON IMPORTS
from datetime import datetime
import logging

from beanie import PydanticObjectId

# LIBRARY IMPORTS

# LOCAL IMPORTS
from common.clients.api import ApiClient
from common.clients.language import LanguageClient
from common.models import MODELS
from player.models import (
    CreateSequenceStatement,
    OperationReference,
    RunOperationStatement,
)
from common.models.player import PlayerStepSession, Replay
from common.models.recorder import Action, Event, Record
from common.rpc.player_pb2 import (
    PlayerRawScriptExecuteRequest,
    PlayerRawScriptExecuteResponse,
    PlayerScriptExecuteRequest,
    PlayerScriptExecuteResponse,
    PlayerScriptExistRequest,
    PlayerScriptExistResponse,
    PlayerScriptGenerateRequest,
    PlayerScriptGenerateResponse,
    PlayerScriptLoadRequest,
    PlayerScriptLoadResponse,
    PlayerScriptUpdateRequest,
    PlayerScriptUpdateResponse,
)
from common.rpc.player_pb2_grpc import PlayerServicer
from common.service import ClientConfig, Service
from common.service import ServiceConfig
from common.utils.mongodb import Mongodb, MongodbConfig
from player.grammar.generator import GrammarGenerator
from player.models import Runtime
from player.grammar.executor import Executor

# INITIALIZATION
log = logging.getLogger(__name__)


class PlayerServiceConfig(ServiceConfig):
    database: MongodbConfig
    detectors: str
    api: ClientConfig
    language: ClientConfig


class PlayerService(Service, PlayerServicer):

    def __init__(self, config: PlayerServiceConfig):
        PlayerServicer.__init__(self)
        Service.__init__(self)
        self.config: PlayerServiceConfig = config
        self.grammar_generator: GrammarGenerator = GrammarGenerator()
        self.api: ApiClient = ApiClient(self.config.api)
        self.language: LanguageClient = LanguageClient(self.config.language)

    async def start(self):
        await Mongodb.initialize(self.config.database, MODELS)
        await self.api.startup()

    async def playerScriptExist(
        self, request: PlayerScriptExistRequest, context
    ) -> PlayerScriptExistResponse:
        try:
            found = await Replay.find_many(
                Replay.record == PydanticObjectId(request.record)
            ).first_or_none()
            return PlayerScriptExistResponse(status=True, found=found is not None)
        except Exception as e:
            log.warning(str(e))
            return PlayerScriptExistResponse(status=False, message=str(e))

    async def playerScriptUpdate(
        self, request: PlayerScriptUpdateRequest, context
    ) -> PlayerScriptUpdateResponse:
        try:
            found = await Replay.find_many(
                Replay.record == PydanticObjectId(request.record)
            ).first_or_none()
            if found is None:
                found = await Replay(
                    record=PydanticObjectId(request.record), script=request.script
                ).insert()
            else:
                found.script = request.script
                await found.save()
            return PlayerScriptExistResponse(status=True)
        except Exception as e:
            log.warning(str(e))
            return PlayerScriptExistResponse(status=False, message=str(e))

    async def playerScriptLoad(
        self, request: PlayerScriptLoadRequest, context
    ) -> PlayerScriptLoadResponse:
        try:
            found = await Replay.find_many(
                Replay.record == PydanticObjectId(request.record)
            ).first_or_none()
            if found is None:
                return PlayerScriptLoadResponse(
                    status=False, message="player.errors.replay_not_found"
                )
            return PlayerScriptLoadResponse(status=True, script=found.script)
        except Exception as e:
            log.warning(str(e))
            return PlayerScriptLoadResponse(status=False, message=str(e))

    async def playerScriptExecute(
        self, request: PlayerScriptExecuteRequest, context
    ) -> PlayerScriptExecuteResponse:
        try:

            found = await Replay.find_many(
                Replay.record == PydanticObjectId(request.record)
            ).first_or_none()
            if found is None:
                return PlayerScriptLoadResponse(
                    status=False, message="player.errors.replay_not_found"
                )
            runtime = Runtime(self.config.detectors)
            executor = Executor()
            stmts = executor.loadScript(found.script)
            stmt_counter = 0
            for stmt in stmts:
                stmt_counter += 1

                current_line = stmt.ctx.line
                current_column = stmt.ctx.column

                log.debug("Executing: {0}".format(stmt))
                a = datetime.now()
                try:
                    stmt.execute(runtime)
                    b = datetime.now()
                    delta = b - a
                    duration = int(delta.total_seconds() * 1000)  # milliseconds
                    update = PlayerStepSession(
                        execution=request.execution,
                        total=len(stmts),
                        progress=stmt_counter,
                        message=stmt.render(),
                        line=current_line,
                        column=current_column,
                        status=True,
                        duration=duration,
                    )
                    await self.api.updateSession(request.session, update)
                except Exception as e:
                    log.warning(str(e))
                    b = datetime.now()
                    delta = b - a
                    duration = int(delta.total_seconds() * 1000)  # milliseconds
                    update = PlayerStepSession(
                        execution=request.execution,
                        total=len(stmts),
                        progress=stmt_counter,
                        message=str(e),
                        line=current_line,
                        column=current_column,
                        status=False,
                        duration=duration,
                    )
                    await self.api.updateSession(request.session, update)
            return PlayerScriptExecuteResponse(status=True)
        except Exception as e:
            log.warning(str(e))
            return PlayerScriptExecuteResponse(status=False, message=str(e))

    async def playerRawScriptExecute(
        self, request: PlayerRawScriptExecuteRequest, context
    ) -> PlayerRawScriptExecuteResponse:
        try:
            runtime = Runtime(self.config.detectors)
            executor = Executor()
            stmts = executor.loadScript(request.script)
            stmt_counter = 0
            for stmt in stmts:
                stmt_counter += 1

                current_line = stmt.ctx.line
                current_column = stmt.ctx.column

                log.debug("Executing: {0}".format(stmt))
                a = datetime.now()
                try:
                    stmt.execute(runtime)
                    b = datetime.now()
                    delta = b - a
                    duration = int(delta.total_seconds() * 1000)  # milliseconds
                    update = PlayerStepSession(
                        execution=request.execution,
                        total=len(stmts),
                        progress=stmt_counter,
                        message=stmt.render(),
                        line=current_line,
                        column=current_column,
                        status=True,
                        duration=duration,
                    )
                    await self.api.updateSession(request.session, update)
                except Exception as e:
                    log.warning(str(e))
                    b = datetime.now()
                    delta = b - a
                    duration = int(delta.total_seconds() * 1000)  # milliseconds
                    update = PlayerStepSession(
                        execution=request.execution,
                        total=len(stmts),
                        progress=stmt_counter,
                        message=str(e),
                        line=current_line,
                        column=current_column,
                        status=False,
                        duration=duration,
                    )
                    await self.api.updateSession(request.session, update)

            return PlayerRawScriptExecuteResponse(status=True)
        except Exception as e:
            log.warning(str(e))
            return PlayerRawScriptExecuteResponse(status=False, message=str(e))

    async def playerScriptGenerate(
        self, request: PlayerScriptGenerateRequest, context
    ) -> PlayerScriptGenerateResponse:
        try:
            record = await Record.find_many(
                Record.id == PydanticObjectId(request.record)
            ).first_or_none()
            if record is None:
                return PlayerScriptGenerateResponse(
                    status=False, message="player.errors.record_not_found"
                )
            actions = await Action.find(
                Action.record == PydanticObjectId(request.record)
            ).to_list()

            dec = ""
            ex = ""

            starterId = 0
            gdecs = []
            gexs = []

            currentDetector = None

            for action in actions:
                event = None
                if action.event:
                    event = await Event.find(
                        Event.id == action.event, with_children=True
                    ).first_or_none()

                    if (
                        action.detector
                        and currentDetector is not None
                        and currentDetector != action.detector
                    ):
                        decs, exs, starterId = (
                            self.grammar_generator.generateDetectorChange(
                                str(action.detector),
                                request.declarative,
                                starterId,
                                action.confidence,
                            )
                        )
                        gdecs.extend(decs)
                        gexs.extend(exs)
                        currentDetector = action.detector
                    if action.detector and currentDetector is None:
                        decs, exs, starterId = (
                            self.grammar_generator.generateDetectorChange(
                                str(action.detector),
                                request.declarative,
                                starterId,
                                action.confidence,
                            )
                        )
                        gdecs.extend(decs)
                        gexs.extend(exs)
                        currentDetector = action.detector
                    if event.synthetic == request.synthetic:
                        frameCount = event.frame
                        decs, exs, starterId = (
                            self.grammar_generator.generateFromAction(
                                action, event, request.declarative, starterId
                            )
                        )
                        gdecs.extend(decs)
                        gexs.extend(exs)
            counter = 0
            for cdec in gdecs:
                sp = ""
                if counter > 0:
                    sp = "\r\n"
                dec += "{0}{1}".format(sp, cdec.render())
                counter += 1

            if len(gexs) > 1 and request.declarative:
                starterId, sequenceId = self.grammar_generator.getNextId(starterId)
                statements = gexs
                seq = CreateSequenceStatement(id=sequenceId, statements=statements)
                dec += "\r\n" + seq.render()
                ex = RunOperationStatement(
                    operation=OperationReference(reference=sequenceId)
                ).render()
            else:

                for cex in gexs:
                    sp = ""
                    if counter > 0:
                        sp = "\r\n"
                    ex += "{0}{1}".format(sp, cex.render())
                    counter += 1

            sp = ""
            if len(gdecs) > 0:
                sp = "\r\n\r\n"
            script = "{0}{1}{2}".format(dec, sp, ex)
            return PlayerScriptGenerateResponse(status=True, script=script)

        except Exception as e:
            log.warning(str(e))
            return PlayerScriptGenerateResponse(status=False, message=str(e))
