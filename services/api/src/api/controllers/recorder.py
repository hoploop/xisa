# PYTHON IMPORTS
from datetime import datetime, time
import threading
from typing import Annotated, List, Tuple
import logging
import platform
import os
import time


# LIBRARY IMPORTS
from beanie import PydanticObjectId
from beanie.operators import And, Or, In, RegEx
from fastapi import Depends, Request
from pydantic import BaseModel
from pynput import keyboard as py_keyboard

from fastapi import BackgroundTasks
from pynput import mouse as py_mouse
from pynput.mouse import Button
import cv2
import numpy as np
import pyautogui

# LOCAL IMPORTS
from common.models.recorder import (
    EVENTS,
    OS,
    Event,
    KeyComboPressEvent,
    KeyPressEvent,
    KeyReleaseEvent,
    MouseDoubleClickEvent,
    MousePressLeftEvent,
    MousePressMiddleEvent,
    MousePressRightEvent,
    MouseReleaseLeftEvent,
    MouseReleaseMiddleEvent,
    MouseReleaseRightEvent,
    MouseScrollEvent,
    Record,
)
from api.models.defaults import utc_now


# INITIALIZATION
log = logging.getLogger(__name__)
VIDEO_EXT = '.mp4'
RECORDS = {}\


class RecorderControllerConfig(BaseModel):
    video: str
    fps:float = 20.0            

class RecorderController:
        

    
    async def start(
        self,
        name: str,
        user_id: PydanticObjectId,
        project_id: PydanticObjectId,
        description: str = "",
    ) -> Record:
        if self.is_running:
            return None
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
        return self.record
    
    def update_frame(self,value:int):
        self.keyboard_listener.set_frame(value)
        self.mouse_listener.set_frame(value)
    
    def collect_event(self,evt):
        self.events.append(evt)

    async def stop(self) -> bool:
        if not self.is_running:
            return False
        self.mouse_listener.stop()
        self.keyboard_listener.stop()
        self.screen_listener.stop()
        self.record.end = utc_now()
        await self.record.save()
        for evt in self.events:
            await evt.insert()
        self.is_running = False
        self.record = None
        return True
    
    
    async def count_record_events(self,user_id:PydanticObjectId,record_id:PydanticObjectId) -> int:
         #results = await Event.find({"is_root": True, "_type": {"$nin": ["ChildA", "ChildB"]}}).to_list()
        total = await Event.find_many(Event.record==record_id,with_children=True).count() 
        return total 
    
    async def size_of_record(self,user_id:PydanticObjectId,record_id:PydanticObjectId) -> int:
        record = await Record.find_many(Record.id == record_id).first_or_none()
        if record:
            filename = os.path.join(self.config.video,str(record.id)+VIDEO_EXT)
            file_stats = os.stat(filename)
            return file_stats.st_size
        return 0
    
    async def load_record_frame(self,user_id:PydanticObjectId,record_id:PydanticObjectId,frame_number:int) -> bytes:
        filename = os.path.join(self.config.video,str(record_id)+VIDEO_EXT)
        cap = cv2.VideoCapture(filename)

        if not cap.isOpened():
            raise("Error: Could not open video file.")
            
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
        return frame_bytes
    
    async def load_record_events(self,user_id:PydanticObjectId,record_id:PydanticObjectId) -> List[EVENTS]:
        found = await Record.find_many(Record.id == record_id).first_or_none()
        if not found:
            raise Exception("Record not found")
        return await Event.find_many(Event.record == record_id,with_children=True).sort(Event.frame).to_list()

    
    async def count_record_frames(self,user_id:PydanticObjectId,record_id:PydanticObjectId) -> int:
        filename = os.path.join(self.config.video,str(record_id)+VIDEO_EXT)
        cap = cv2.VideoCapture(filename)
        length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        return length
   


async def get_recorder_controller(
    request: Request
) -> RecorderController:
    if not hasattr(request.app.state, "recorder"):
        request.app.state.recorder = RecorderController(
            request.app.state.config.recorder
        )
    return request.app.state.recorder


GetRecorderController = Annotated[RecorderController, Depends(get_recorder_controller)]
