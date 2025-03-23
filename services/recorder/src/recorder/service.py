# PYTHON IMPORTS
import base64
import logging
import os

# LIBRARY IMPORTS
import aiofiles
from beanie import PydanticObjectId
from beanie.operators import In,And,Or,RegEx
import platform
import cv2
import grpc

# LOCAL IMPORTS
from common.models import MODELS
from common.models.defaults import utc_now
from common.models.recorder import OS, Event, Record
from common.rpc.recorder_pb2 import CountRecordEventRequest, CountRecordEventResponse, CountRecordFrameRequest, CountRecordFrameResponse, CountRecordRequest, CountRecordResponse, DeleteRecordRequest, DeleteRecordResponse, ListRecordEventRequest, ListRecordEventResponse, ListRecordRequest, ListRecordResponse, LoadRecordFrameBase64Request, LoadRecordFrameBase64Response, LoadRecordFrameRequest, LoadRecordFrameResponse, LoadRecordRequest, LoadRecordResponse, RunningRequest, RunningResponse, SizeRecordRequest, SizeRecordResponse, SizeRecordVideoRequest, SizeRecordVideoResponse, StartRecordRequest, StartRecordResponse, StopRecordRequest, StopRecordResponse, StreamRangeRecordVideoRequest, StreamRangeRecordVideoResponse, StreamRecordVideoRequest, StreamRecordVideoResponse, UpdateRecordRequest, UpdateRecordResponse
from common.rpc.recorder_pb2_grpc import RecorderServicer
from common.service import Service
from common.service import ServiceConfig
from common.utils.conversions import Conversions
from common.utils.mongodb import Mongodb, MongodbConfig
from recorder.constants import VIDEO_EXT
from recorder.mouse import MouseListener
from recorder.keyboard import KeyboardListener
from recorder.screen import ScreenListener

# INITIALIZATION
log = logging.getLogger(__name__)
RECORDS = {}

class RecorderServiceConfig(ServiceConfig):
    video: str
    fps:float = 20.0    
    database: MongodbConfig

class RecorderService(Service, RecorderServicer):

    def __init__(self, config: RecorderServiceConfig):
        RecorderServicer.__init__(self)
        Service.__init__(self)
        self.config:RecorderServiceConfig = config
        self.is_running = False
        self.record = None
        self.events = []
        self.CACHED_FRAMES = {}
        self.CACHED_FRAMES_BASE64 = {}

        
    async def start(self):
         await Mongodb.initialize(self.config.database,MODELS)
         
    async def running(self, request: RunningRequest, context) -> RunningResponse:
        return RunningResponse(status=self.is_running)
    
    async def loadRecord(self, request:LoadRecordRequest, context) -> LoadRecordResponse:
        try:
            user_id = PydanticObjectId(request.user)
            record_id = PydanticObjectId(request.id)
            found = await Record.find_many(Record.id == record_id,In(Record.users,[user_id])).first_or_none()
            if not found:
                raise LoadRecordResponse(status=False,message="workspace.record.errors.not_found")
            return LoadRecordResponse(status=True,record=Conversions.serialize(found))
        except Exception as e:
            log.warning(str(e))
            return LoadRecordResponse(status=False,message=str(e))
        
        
    async def updateRecord(self, request: UpdateRecordRequest, context) -> UpdateRecordResponse:
        try:
            user_id = PydanticObjectId(request.user)
            record_id = PydanticObjectId(request.id)
            name = request.name
            description = request.description
            found = await Record.find_many(Record.id == record_id,In(Record.users,[user_id])).first_or_none()
            if not found:
                return LoadRecordResponse(status=False,message="workspace.record.errors.not_found")
            others_found = await Record.find_many(Record.project == found.project,Record.name == name,Record.id != found.id).first_or_none()
            if others_found:
                raise LoadRecordResponse(status=False,message="workspace.record.errors.already_existing")
            found.name = name
            found.description= description
            await found.save()
            return LoadRecordResponse(status=1,record=Conversions.serialize(found))
        
        except Exception as e:
            log.warning(str(e))
            return UpdateRecordResponse(status=False,message=str(e))
    
    
    async def listRecord(self, request:ListRecordRequest, context) -> ListRecordResponse:
        try:
            project_id = PydanticObjectId(request.project)
            user_id = PydanticObjectId(request.user)
            search = request.search
            skip = request.skip
            limit = request.limit
            qry = And(Record.project == project_id,In(Record.users,[user_id]))
            if search is not None and search.strip()!='':
                qry = And(
                    Record.project == project_id,
                    In(Record.users,[user_id]),
                    Or(
                        RegEx(Record.name, search, options="i"),
                        RegEx(Record.description, search, options="i"),
                    ),
                )
            total = await Record.find(qry).count()
            records = await Record.find(qry).skip(skip).limit(limit).sort(-Record.created).to_list()
            ret = []
            for record in records:
                ret.append(Conversions.serialize(record))
            return ListRecordResponse(status=True,total=total,records=ret)
        except Exception as e:
            log.warning(str(e))
            return ListRecordResponse(status=False,message=str(e))
        
    async def countRecord(self, request:CountRecordRequest, context) -> CountRecordResponse:
        try:
            project_id = PydanticObjectId(request.project)
            user_id = PydanticObjectId(request.user)
            qry = And(Record.project == project_id,In(Record.users,[user_id]))
            total = await Record.find(qry).count()
            return CountRecordResponse(status=True,total=total)
        except Exception as e:
            log.warning(str(e))
            return CountRecordResponse(status=False,message=str(e))
        
    async def deleteRecord(self, request: DeleteRecordRequest, context) -> DeleteRecordResponse:
        try:
            user_id = PydanticObjectId(request.user)
            record_id = PydanticObjectId(request.record)
            record = await Record.find_many(Record.id == record_id,In(Record.users,[user_id])).first_or_none()
            if record:
                filename = os.path.join(self.config.video,str(record.id)+VIDEO_EXT)
                if os.path.exists(filename):
                    os.remove(filename)
                await record.delete()
                return DeleteRecordResponse(status=True)
            else:
                raise Exception("workspace.record.errors.not_found")
        except Exception as e:
            log.warning(str(e))
            return DeleteRecordResponse(status=False,message=str(e))
        
    
    
    def update_frame(self,value:int):
        self.keyboard_listener.set_frame(value)
        self.mouse_listener.set_frame(value)
    
    def collect_event(self,evt):
        self.events.append(evt)

        
    async def startRecord(self, request:StartRecordRequest, context) -> StartRecordResponse:
        try:
            user_id = PydanticObjectId(request.user)
            project_id = PydanticObjectId(request.project)
            name = request.name
            description = request.description
            if self.is_running:
                return StartRecordResponse(status=False,message="workspace.record.errors.already_running")
            self.is_running = True
            self.events = []
            os = OS(name=platform.system(), version=platform.release())
            self.record = Record(
                users=[user_id],
                name=name,
                description=description,
                start=utc_now(),
                project=project_id,
                os=os,
            )
            await self.record.insert()
            self.mouse_listener = MouseListener(self.record.id,self.collect_event)
            self.keyboard_listener = KeyboardListener(self.record.id,self.collect_event)
            self.screen_listener = ScreenListener(self.config, self.record.id,self.update_frame)
            self.mouse_listener.start()
            self.keyboard_listener.start()
            self.screen_listener.start()
            return StartRecordResponse(status=True,record=Conversions.serialize(self.record))
        except Exception as e:
            log.warning(str(e))
            return StartRecordResponse(status=False,message=str(e))
        
        
    async def stopRecord(self, request: StopRecordRequest, context) -> StopRecordResponse:
        try:
            if not self.is_running:
                return StopRecordResponse(status=False,message="workspace.record.errors.not_running")
            self.mouse_listener.stop()
            self.keyboard_listener.stop()
            self.screen_listener.stop()
            self.record.end = utc_now()
            await self.record.save()
            for evt in self.events:
                await evt.insert()
            self.is_running = False
            self.record = None
            return StopRecordResponse(status=True)
        except Exception as e:
            log.warning(str(e))
            return StopRecordResponse(status=False,message=str(e))
        
    async def countRecordEvent(self, request:CountRecordEventRequest, context) -> CountRecordEventResponse:
        try:
            record_id = PydanticObjectId(request.record)
            total = await Event.find_many(Event.record==record_id,with_children=True).count() 
            return CountRecordEventResponse(status=True,total=total) 
        except Exception as e:
            return CountRecordEventResponse(status=False,message=str(e))
        
    async def listRecordEvent(self, request:ListRecordEventRequest, context) -> ListRecordEventResponse:
        try:
            record_id = PydanticObjectId(request.record)
            found = await Record.find_many(Record.id == record_id).first_or_none()
            if not found:
                return ListRecordEventResponse(status=False,message="workspace.record.errors.not_found")
            events = await Event.find_many(Event.record == record_id,with_children=True).sort(Event.frame).to_list()
            ret = []
            for event in events:
                ret.append(Conversions.serialize(event))
            return ListRecordEventResponse(status=True,events=ret)
        except Exception as e:
            log.warning(str(e))
            return ListRecordEventResponse(status=False,message=str(e))
        
    async def countRecordFrame(self, request:CountRecordFrameRequest, context) -> CountRecordFrameResponse:
        try:
            record_id = PydanticObjectId(request.record)
            filename = os.path.join(self.config.video,str(record_id)+VIDEO_EXT)
            cap = cv2.VideoCapture(filename)
            length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            return CountRecordFrameResponse(status=True,total=length)
        except Exception as e:
            log.warning(str(e))
            return CountRecordFrameResponse(status=False,message=str(e))
        
    async def loadRecordFrame(self, request:LoadRecordFrameRequest, context) -> LoadRecordFrameResponse:
        try:
            record_id = PydanticObjectId(request.record)
            frame_number = request.frame
            filename = os.path.join(self.config.video,str(record_id)+VIDEO_EXT)
            
            if filename in self.CACHED_FRAMES and frame_number in self.CACHED_FRAMES[filename]:
                return LoadRecordFrameResponse(status=True,frame=self.CACHED_FRAMES[filename][frame_number])
            
            cap = cv2.VideoCapture(filename)

            if not cap.isOpened():
                return LoadRecordFrameResponse(status=False,message="Error: Could not open video file.")
                
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
            
            # Read the specific frame
            ret, frame = cap.read()
            
            if not ret:
                raise Exception(f"Error: Could not read frame {frame_number}.")
            
            # Check if frame was successfully read
            # Convert BGR to RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Encode the frame as PNG image in memory
            _, encoded_image = cv2.imencode(".png", frame_rgb)
            
            # Convert the image to bytes
            frame_bytes = encoded_image.tobytes()
            
            cap.release()
            
            if filename not in self.CACHED_FRAMES:
                self.CACHED_FRAMES[filename] = {}
            if frame_number not in self.CACHED_FRAMES[filename]:
                self.CACHED_FRAMES[filename][frame_number] = frame_bytes
            
            return LoadRecordFrameResponse(status=True,frame=frame_bytes)
        except Exception as e:
            log.warning(str(e))
            return LoadRecordFrameResponse(status=False,message=str(e))
        
    
    async def loadRecordFrameBase64(self, request:LoadRecordFrameBase64Request, context) -> LoadRecordFrameBase64Response:
        try:
            record_id = PydanticObjectId(request.record)
            frame_number = request.frame
            filename = os.path.join(self.config.video,str(record_id)+VIDEO_EXT)
            
            if filename in self.CACHED_FRAMES_BASE64 and frame_number in self.CACHED_FRAMES_BASE64[filename]:
                return LoadRecordFrameBase64Response(status=True,frame=self.CACHED_FRAMES_BASE64[filename][frame_number])
            
            cap = cv2.VideoCapture(filename)

            if not cap.isOpened():
                return LoadRecordFrameBase64Response(status=False,message="Error: Could not open video file.")
                
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
            
            # Read the specific frame
            ret, frame = cap.read()
            
            if not ret:
                return LoadRecordFrameBase64Response(status=True,message=f"Error: Could not read frame {frame_number}.")
            
            # Check if frame was successfully read
            # Convert BGR to RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Encode the frame as PNG image in memory
            _, encoded_image = cv2.imencode(".png", frame_rgb)
            
            # Convert the image to bytes
            frame_bytes = encoded_image.tobytes()
            
            png_as_text = 'data:image/png;base64,'+base64.b64encode(frame_bytes).decode()
            
            
            cap.release()
            
            if filename not in self.CACHED_FRAMES_BASE64:
                self.CACHED_FRAMES_BASE64[filename] = {}
            if frame_number not in self.CACHED_FRAMES_BASE64[filename]:
                self.CACHED_FRAMES_BASE64[filename][frame_number] = png_as_text
            
            return LoadRecordFrameBase64Response(status=True,frame=png_as_text)
        except Exception as e:
            log.warning(str(e))
            return LoadRecordFrameBase64Response(status=False,message=str(e))
        
    async def sizeRecord(self, request:SizeRecordRequest, context) -> SizeRecordResponse:
        try:
            record_id = PydanticObjectId(request.record)
            record = await Record.find_many(Record.id == record_id).first_or_none()
            if record:
                filename = os.path.join(self.config.video,str(record.id)+VIDEO_EXT)
                file_stats = os.stat(filename)
                return SizeRecordResponse(status=True,size=file_stats.st_size)
            return SizeRecordResponse(status=True,size=0)
        except Exception as e:
            log.warning(str(e))
            return SizeRecordResponse(status=False,message=str(e))
            
    async def sizeRecordVideo(self, request: SizeRecordVideoRequest, context) -> SizeRecordVideoResponse:
        try:
            record_id = PydanticObjectId(request.record)
            video_id = str(record_id)
            video_path = os.path.join(self.config.video, video_id + ".mp4")
            if not os.path.exists(video_path):
                return SizeRecordResponse(status=False,message="workspace.record.errors.video_not_found")
            file_size = os.path.getsize(video_path)
            return SizeRecordVideoResponse(status=True,size=file_size)
        except Exception as e:
            log.warning(str(e))
            return SizeRecordVideoResponse(status=False,message=str(e))
            
    async def streamRecordVideo(self, request: StreamRecordVideoRequest, context):
        try:
            record_id = PydanticObjectId(request.record)
            video_id = str(record_id)
            video_path = os.path.join(self.config.video, video_id + ".mp4")
            
            if not os.path.exists(video_path):
                context.abort(grpc.StatusCode.NOT_FOUND, "workspace.record.errors.video_not_found")


            """Async generator to read video in chunks."""
            async with aiofiles.open(video_path, "rb") as video_file:
                while chunk := await video_file.read(1024):  # Read 1MB chunks
                    yield StreamRecordVideoResponse(status=True,data=chunk)

        except Exception as e:
            log.warning(str(e))
            
    
    async def streamRangeRecordVideo(self, request: StreamRangeRecordVideoRequest, context) -> StreamRangeRecordVideoResponse:
        try:
            record_id = PydanticObjectId(request.record)
            video_id = str(record_id)
            video_path = os.path.join(self.config.video, video_id + ".mp4")
            start = request.start_byte
            end = request.end_byte

            
            if not os.path.exists(video_path):
                context.abort(grpc.StatusCode.NOT_FOUND, "workspace.record.errors.video_not_found")
                
            file_size = os.path.getsize(video_path)
            start = int(start)
            end = int(end) if end else file_size - 1
            chunk_size = end - start + 1

            """Async generator to read video in chunks."""
            async with aiofiles.open(video_path, "rb") as video_file:
                await video_file.seek(start)
                chunk = await video_file.read(chunk_size)
                return StreamRangeRecordVideoResponse(status=True,data=chunk)

        except Exception as e:
            log.warning(str(e))