
# PYTHON IMPORTS
import logging
import threading

# LIBRARY IMPORTS
from pynput import keyboard

# LOCAL IMPORTS
from common.models.recorder import (
    EVENTS,
    OS,
    Event,
    KeyComboPressEvent,
    KeyPressEvent,
    KeyReleaseEvent,
)

# INITIALIZATION
log = logging.getLogger(__name__)

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
        self._listener = keyboard.Listener(on_press=self.on_press,
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
        

