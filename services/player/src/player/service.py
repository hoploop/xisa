# PYTHON IMPORTS
import logging

from beanie import PydanticObjectId

# LIBRARY IMPORTS

# LOCAL IMPORTS
from common.models import MODELS
from common.models.player import Replay
from common.models.recorder import Action, Event, Record
from common.rpc.player_pb2 import PlayerScriptExistRequest, PlayerScriptExistResponse, PlayerScriptGenerateRequest, PlayerScriptGenerateResponse, PlayerScriptLoadRequest, PlayerScriptLoadResponse
from common.rpc.player_pb2_grpc import PlayerServicer
from common.service import Service
from common.service import ServiceConfig
from common.utils.mongodb import Mongodb, MongodbConfig
from player.grammar.generator import GrammarGenerator

# INITIALIZATION
log = logging.getLogger(__name__)

class PlayerServiceConfig(ServiceConfig):
    database: MongodbConfig
    detectors: str

class PlayerService(Service, PlayerServicer):

    def __init__(self, config: PlayerServiceConfig):
        PlayerServicer.__init__(self)
        Service.__init__(self)
        self.config:PlayerServiceConfig = config
        self.grammar_generator: GrammarGenerator = GrammarGenerator()
        
    async def start(self):
         await Mongodb.initialize(self.config.database,MODELS)
         
    async def playerScriptExist(self, request:PlayerScriptExistRequest, context) -> PlayerScriptExistResponse:
        try:
            found = await Replay.find_many(Replay.record == PydanticObjectId(request.record)).first_or_none()
            return PlayerScriptExistResponse(status=True,found=found is not None)
        except Exception as e:
            log.warning(str(e))
            return PlayerScriptExistResponse(status=False,message=str(e))
    
    async def playerScriptLoad(self, request:PlayerScriptLoadRequest, context) -> PlayerScriptLoadResponse:
        try:
            found = await Replay.find_many(Replay.record == PydanticObjectId(request.record)).first_or_none()
            if found is None:
                return PlayerScriptLoadResponse(status=False,message="player.errors.replay_not_found")
            return PlayerScriptLoadResponse(status=True,script=found.script)
        except Exception as e:
            log.warning(str(e))
            return PlayerScriptLoadResponse(status=False,message=str(e))
        
    async def playerScriptGenerate(self, request:PlayerScriptGenerateRequest, context) -> PlayerScriptGenerateResponse:
        try:
            record = await Record.find_many(Record.id == PydanticObjectId(request.record)).first_or_none()
            if record is None:
                return PlayerScriptGenerateResponse(status=False,message='player.errors.record_not_found')
            actions = await Action.find(Action.record == PydanticObjectId(request.record)).to_list()
            
            dec = ''
            ex = ''
            
            starterId = 0
            for action in actions:
                event = None
                if action.event:
                    event = await Event.find(Event.id == action.event,with_children=True).first_or_none()
                    if event.synthetic == request.synthetic:
                        frameCount = event.frame
                        decs, exs, starterId = self.grammar_generator.generateFromAction(action,event,request.declarative,starterId)
                    
                        for cdec in decs:
                            dec += '\r\n{0}'.format(cdec)
                        
                        for cex in exs:
                            ex += '\r\n{0}'.format(cex)
            
            script = '{0}\r\n\r\n{1}'.format(dec,ex)
            return PlayerScriptGenerateResponse(status=True,script=script)
                    
                    
        except Exception as e:
            log.warning(str(e))
            return PlayerScriptGenerateResponse(status=False,message=str(e))
        