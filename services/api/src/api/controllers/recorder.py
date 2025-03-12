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
from api.models.recorder import (
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
RECORDS = {}

class MouseListener:
    def __init__(self,record_id, event_callback=None):
        self._record_id = record_id
        self._recording: bool = False
        self._event_callback = event_callback
        self._listener = None
        self._listener_thread = None
        self._cx = 0
        self._cy = 0
        self._frame = 0
        
    def set_frame(self,value:int):
        self._frame = value

    def on_event(self, evt: Event):
        if self._event_callback:
            self._event_callback(evt)

    def start(self):
        if self._recording: return
        self._recording = True
        log.info('Start recording mouse events')
        self._events = []
        self._listener = py_mouse.Listener(
            on_move=self.record_move,
            on_click=self.record_click,
            on_scroll=self.record_scroll)

        self._listener_thread = threading.Thread(target=self._listener.start)
        self._listener_thread.daemon = True
        self._listener_thread.start()

    def record_move(self, x, y):
        pass
        # print('Pointer moved to {0}'.format(
        #    (x, y)))
        # self._events.append(Move(Position(x, y)))


    def record_click(self, x, y, button, pressed):
        print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
        if x!= self._cx or y!= self._cy:
            #evt = Move(x=x, y=y)
            #self.on_event(evt)
            self._cx = x
            self._cy = y
            
        if button == Button.left:
            if pressed:
                evt = MousePressLeftEvent(record=self._record_id,position=(x,y),frame=self._frame)
                self.on_event(evt)
            else:
                evt = MouseReleaseLeftEvent(record=self._record_id,position=(x,y),frame=self._frame)
                self.on_event(evt)
        elif button == Button.middle:
            if pressed:
                evt = MousePressMiddleEvent(record=self._record_id,position=(x,y),frame=self._frame)
                self.on_event(evt)

            else:
                evt = MouseReleaseMiddleEvent(record=self._record_id,position=(x,y),frame=self._frame)
                self.on_event(evt)

        elif button == Button.right:
            if pressed:
                evt = MousePressRightEvent(record=self._record_id,position=(x,y),frame=self._frame)
                self.on_event(evt)

            else:
                evt = MouseReleaseRightEvent(record=self._record_id,position=(x,y),frame=self._frame)
                self.on_event(evt)

    def record_scroll(self, x, y, dx, dy):
        print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))
        self._events.append(MouseScrollEvent(record=self._record_id,dy=dy,dx=dx,position=(x,y),frame=self._frame))

    def stop(self):
        if not self._recording: return
        if not self._listener: return
        self._listener.stop()
        self._listener_thread.join()
        self._recording = False
        log.info('Stop recording mouse events')

class KeyboardListener:

    def __init__(self,record_id, event_callback=None):
        self._record_id = record_id
        self._event_callback = event_callback
        self._recording: bool = False
        self._listener = None
        self._listener_thread = None
        self._frame = 0
        
    def set_frame(self,value:int):
        self._frame = value

    def on_event(self, evt: Event):
        if self._event_callback:
            self._event_callback(evt)

    def on_press(self, key):
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
            evt = KeyPressEvent(key=str(key.char),record=self._record_id,frame=self._frame)
            self.on_event(evt)

        except AttributeError:
            print('special key {0} pressed'.format(
                key))
            evt = KeyPressEvent(key=str(key),record=self._record_id,frame=self._frame)
            self.on_event(evt)

    def on_release(self, key):
        print('{0} released'.format(
            key))
        try:
            print('alphanumeric key {0} released'.format(
                key.char))
            evt = KeyReleaseEvent(key=str(key.char),record=self._record_id,frame=self._frame)
            self.on_event(evt)

        except AttributeError:
            print('special key {0} released'.format(
                key))
            evt = KeyReleaseEvent(key=str(key),record=self._record_id,frame=self._frame)
            self.on_event(evt)

    def start(self):
        if self._recording: return
        log.info('Start recording keyboard events')
        self._recording = True
        self._listener = py_keyboard.Listener(on_press=self.on_press,
                                              on_release=self.on_release)
        self._listener_thread = threading.Thread(target=self._listener.start)
        self._listener_thread.daemon = True
        self._listener_thread.start()

    def stop(self):
        if not self._recording: return
        if not self._listener: return

        self._listener.stop()
        self._listener_thread.join()
        self._recording = False
        log.info('Stop recording keyboard events')
        


class ScreenListener:

    def __init__(self,config,record_id,on_frame=None,on_start=None,on_end=None):
        self._folder = config.video
        self._record_id = record_id
        self._on_start = on_start
        self._on_end = on_end
        self._on_frame = on_frame
        self._fps = config.fps
        self._recording = False
        self._filename = None
        self._current = None
        self._current_img = None
        self._listener = None
        self._recorder = None

    def size(self):
        """
        Gets the primary screen size
        :return:
        """
        log.debug('Getting the primary screen size')
        screen_width, screen_height = pyautogui.size()
        return (screen_width, screen_height)


    def start(self):
        if self._recording: return
        self._recording = True
        self._listener = threading.Thread(target=self.listener_loop)
        self._recorder = threading.Thread(target=self.record_loop)
        self._listener.daemon = True
        self._recorder.daemon = True
        
        self._listener.start()
        self._recorder.start()

    def listener_loop(self):
        while self._recording:
            try:
                self._current = pyautogui.screenshot()
                self._current_img = cv2.cvtColor(np.array(self._current), cv2.COLOR_RGB2BGR)
            except KeyboardInterrupt:
                break

    def record_loop(self):
        output = os.path.join(self._folder,str(self._record_id)+VIDEO_EXT)
        buffer = []
        self._current = pyautogui.screenshot()
        img = cv2.cvtColor(np.array(self._current), cv2.COLOR_RGB2BGR)
        self._current_img = img
        # get info from img
        height, width, channels = img.shape
        if self._on_start: 
            self._on_start(datetime.utcnow())
        while self._recording:
            try:
                buffer.append(self._current_img)
                if self._on_frame:
                    self._on_frame(len(buffer)-1)
                time.sleep(1 / self._fps)
            except KeyboardInterrupt:
                break
        if self._on_end:
            self._on_end(datetime.utcnow())
        # Define the codec and create VideoWriter object
        
        fourcc = cv2.VideoWriter_fourcc(*'X264')
        out = cv2.VideoWriter(output, fourcc, self._fps, (width, height))

        # Write the frames to the file
        log.info("Write the frames to the file: {0}".format(output))
        for frame in buffer:
            out.write(frame)
        out.release()


    def stop(self):
        if not self._recording: return
        self._recording = False
        self._recorder.join()
        self._listener.join()

    def region_screenshot(self, x, y, w, h):
        """
        Performa a screenshot of a specific region of the
        screen
        :return:
        """
        im = pyautogui.screenshot(region=(x, y, w, h))
        # pic = Picture(region._w, region._h, im)


class RecorderControllerConfig(BaseModel):
    video: str
    fps:float = 20.0            

class RecorderController:
    def __init__(self, config: RecorderControllerConfig):
        self.is_running = False
        self.config:RecorderControllerConfig = config
        self.record = None
        self.events = []

    async def running(self) -> bool:
        return self.is_running

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
    
    async def count_records(self,user_id:PydanticObjectId,project_id:PydanticObjectId) -> int:
        return await Record.find_many(Record.project == project_id).count()
    
    async def delete_record(self,user_id:PydanticObjectId,record_id:PydanticObjectId):
        record = await Record.find_many(Record.id == record_id).first_or_none()
        if record:
            filename = os.path.join(self.config.video,str(record.id)+VIDEO_EXT)
            if os.path.exists(filename):
                os.remove(filename)
            await record.delete()
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
    
    async def load_record(self,user_id:PydanticObjectId,record_id) -> Record:
        found = await Record.find_many(Record.id == record_id).first_or_none()
        if not found:
            raise Exception("Record not found")
        return found
    
    async def update_record(self,user_id:PydanticObjectId,record_id:PydanticObjectId,name:str,description:str) -> Record:
        found = await Record.find_many(Record.id == record_id).first_or_none()
        if not found:
            raise Exception("Record not found")
        others_found = await Record.find_many(Record.project == found.project,Record.name == name,Record.id != found.id).first_or_none()
        if others_found:
            raise Exception("Another record with this username already found")
        found.name = name
        found.description= description
        await found.save()
        return found
    
    async def list_records(
        self,
        user_id: PydanticObjectId,
        project_id: PydanticObjectId,
        skip: int = 0,
        limit: int = 10,
        search: str = None,
    ) -> Tuple[int, List[Record]]:
        qry = And(Record.project == project_id)
        if search is not None:
            qry = And(
                Record.project == project_id,
                Or(
                    RegEx(Record.name, search, options="i"),
                    RegEx(Record.description, search, options="i"),
                ),
            )
        total = await Record.find(qry).count()
        records = await Record.find(qry).skip(skip).limit(limit).sort(-Record.created).to_list()
        return [total, records]


async def get_recorder_controller(
    request: Request
) -> RecorderController:
    if not hasattr(request.app.state, "recorder"):
        request.app.state.recorder = RecorderController(
            request.app.state.config.recorder
        )
    return request.app.state.recorder


GetRecorderController = Annotated[RecorderController, Depends(get_recorder_controller)]
