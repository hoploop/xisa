
# PYTHON IMPORTS
import logging
import threading

# LIBRARY IMPORTS
from pynput import mouse
from pynput.mouse import Button

# LOCAL IMPORTS
from common.models.recorder import (
    EVENTS,
    OS,
    Event,
    
    MousePressLeftEvent,
    MousePressMiddleEvent,
    MousePressRightEvent,
    MouseReleaseLeftEvent,
    MouseReleaseMiddleEvent,
    MouseReleaseRightEvent,
    MouseScrollEvent,
)

# INITIALIZATION
log = logging.getLogger(__name__)


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
        self._listener = mouse.Listener(
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
