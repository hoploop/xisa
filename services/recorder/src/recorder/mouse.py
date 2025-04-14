
# PYTHON IMPORTS
import logging
import threading
import time

# Config
DOUBLE_CLICK_TIME = 0.3  # seconds

# LIBRARY IMPORTS
from pynput import mouse
from pynput.mouse import Button

# LOCAL IMPORTS
from common.models.recorder import (
    EVENTS,
    OS,
    Event,
    MousePressEvent,
    MouseReleaseEvent,
    MouseClickEvent,
    MouseDoubleClickEvent,
    MouseDropEvent,
    MouseScrollEvent,
    MouseButton
)

# INITIALIZATION
log = logging.getLogger(__name__)
DOUBLE_CLICK_TIME = 0.3  # seconds

# State

class MouseListener:
    def __init__(self,record_id, event_callback=None,mouse_move_callback=None):
        self._record_id = record_id
        self._recording: bool = False
        self._event_callback = event_callback
        self._listener = None
        self._listener_thread = None
        self._cx = 0
        self._cy = 0
        self._frame = 0
        
        self.last_click_time = 0
        self.click_count = 0
        self.is_dragging = False
        self.drag_start_pos = None
        self.pressed_button = None
        self.correlated_event_frame = 0
        self._mouse_move_callback = mouse_move_callback
        

        
    def set_frame(self,value:int):
        self._frame = value
        
    
    def on_event(self, evt: Event):
        if self._event_callback:
            self._event_callback(evt)
            
    def find_button(self,source:Button)->MouseButton:
        if source == Button.left:
            return MouseButton.left
        elif source == Button.middle:
            return MouseButton.middle
        elif source == Button.right:
            return MouseButton.right
        else:
            return MouseButton.left
        

    def start(self):
        if self._recording: return
        self._recording = True
        log.info('Start recording mouse events')
        self._events = []
        self._listener = mouse.Listener(
            on_move=self.record_move,
            on_click=self.record_button,
            on_scroll=self.record_scroll)

        self._listener_thread = threading.Thread(target=self._listener.start)
        self._listener_thread.daemon = True
        self._listener_thread.start()

    def record_move(self, x, y):
        if self._mouse_move_callback:
            self._mouse_move_callback(x,y)
        if self.pressed_button and self.drag_start_pos:
            if not self.is_dragging:
                log.info(f"[DRAG START] from {self.drag_start_pos}")
                self.is_dragging = True
            else:
                log.info(f"[DRAGGING] to ({x}, {y})")

    def record_pressed(self,x,y,button):
        
        self.drag_start_pos = (x, y)
        self.is_dragging = False
        self.pressed_button = button
        self.correlated_event_frame = self._frame
        evt = MousePressEvent(record=self._record_id,position=(x,y),frame=self._frame,button=self.find_button(button))
        self.on_event(evt)
        
    
    def record_released(self,x,y,button):
        
        evt = MouseReleaseEvent(record=self._record_id,position=(x,y),frame=self._frame,button=self.find_button(button))
        self.on_event(evt)
        if self.is_dragging:
            log.info(f"[DROP] from {self.drag_start_pos} to ({x}, {y}) with {button}")
            self.record_drop(x,y,button)
        else:
            current_time = time.time()
            if current_time - self.last_click_time <= DOUBLE_CLICK_TIME:
                self.click_count += 1
            else:
                self.click_count = 1

            self.last_click_time = current_time

            if self.click_count == 2:
                log.info(f"[DOUBLE CLICK] {button} at ({x}, {y})")
                self.record_double_click(x,y,button)
            else:
                log.info(f"[CLICK] {button} at ({x}, {y})")
                self.record_click(x,y,button)
                
    

    def record_button(self, x, y, button, pressed):
        
        log.debug('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
        
        if pressed:
            self.record_pressed(x,y,button)
        else:
            self.record_released(x,y,button)
        
        if x!= self._cx or y!= self._cy:
            self._cx = x
            self._cy = y
            

    def record_scroll(self, x, y, dx, dy):
        print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))
        self._events.append(MouseScrollEvent(record=self._record_id,dy=dy,dx=dx,position=(x,y),frame=self._frame))
        
    def record_click(self,x,y,button):
        evt = MouseClickEvent(record=self._record_id,position=(x,y),frame=self.correlated_event_frame,button=self.find_button(button),synthetic=True)
        self.on_event(evt)
    
    def record_double_click(self,x,y,button):
        evt = MouseDoubleClickEvent(record=self._record_id,position=(x,y),frame=self.correlated_event_frame,button=self.find_button(button),synthetic=True)
        self.on_event(evt)
    
    def record_drop(self,x,y,button):
        evt = MouseDropEvent(record=self._record_id,position=(x,y),frame=self.correlated_event_frame,button=self.find_button(button),origin=self.drag_start_pos,synthetic=True)
        self.on_event(evt)

    def stop(self):
        if not self._recording: return
        if not self._listener: return
        self._listener.stop()
        self._listener_thread.join()
        self._recording = False
        log.info('Stop recording mouse events')
