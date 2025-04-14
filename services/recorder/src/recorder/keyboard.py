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
    KeyTypeEvent,
)

# INITIALIZATION
log = logging.getLogger(__name__)


class KeyboardListener:

    def __init__(self, record_id, event_callback=None):
        self._record_id = record_id
        self._event_callback = event_callback
        self._recording: bool = False
        self._listener = None
        self._listener_thread = None
        self._frame = 0
        self._mouse_x = 0
        self._mouse_y = 0
        self.pressed_keys = set()
        self.active_combos = set()

    def set_frame(self, value: int):
        self._frame = value

    def set_mouse_position(self, x: int, y: int):
        self._mouse_x = x
        self._mouse_y = y

    def on_event(self, evt: Event):
        if self._event_callback:
            self._event_callback(evt)

    def format_combo(self, combo):
        return "+".join(sorted(str(k) for k in combo))

    def on_press(self, key):
        try:
            log.debug("alphanumeric key {0} pressed".format(key.char))
            evt = KeyPressEvent(
                key=str(key.char),
                record=self._record_id,
                frame=self._frame,
                position=(self._mouse_x, self._mouse_y),
            )
            self.on_event(evt)

            if hasattr(key, "char") and key.char is not None:
                log.debug(f"Key typed: {key.char}")
                evt = KeyTypeEvent(
                    key=str(key.char),
                    record=self._record_id,
                    frame=self._frame,
                    synthetic=True,
                    position=(self._mouse_x, self._mouse_y),
                )
                self.on_event(evt)

            # COMBO HOTKEYS
            if key not in self.pressed_keys:
                self.pressed_keys.add(key)
                combo = frozenset(self.pressed_keys)
                if combo not in self.active_combos and len(combo) > 1:
                    self.active_combos.add(combo)
                    log.debug(f"Combo pressed: {self.format_combo(combo)}")
                    evt = KeyComboPressEvent(
                        record=self._record_id,
                        frame=self._frame,
                        synthetic=True,
                        keys=list(combo),
                        position=(self._mouse_x, self._mouse_y),
                    )
                    self.on_event(evt)

        except AttributeError:
            log.debug("special key {0} pressed".format(key))
            evt = KeyPressEvent(
                key=str(key),
                record=self._record_id,
                frame=self._frame,
                position=(self._mouse_x, self._mouse_y),
            )
            self.on_event(evt)

    def on_release(self, key):
        log.debug("{0} released".format(key))
        try:
            log.debug("alphanumeric key {0} released".format(key.char))
            evt = KeyReleaseEvent(
                key=str(key.char),
                record=self._record_id,
                frame=self._frame,
                position=(self._mouse_x, self._mouse_y),
            )
            self.on_event(evt)

            if key in self.pressed_keys:
                self.pressed_keys.remove(key)

            # Clean up any combo that involved the released key
            combos_to_remove = [c for c in self.active_combos if key in c]

            for combo in combos_to_remove:
                self.active_combos.remove(combo)
                log.debug(f"Combo released: {self.format_combo(combo)}")

        except AttributeError:
            log.debug("special key {0} released".format(key))
            evt = KeyReleaseEvent(
                key=str(key),
                record=self._record_id,
                frame=self._frame,
                position=(self._mouse_x, self._mouse_y),
            )
            self.on_event(evt)

    def start(self):
        if self._recording:
            return
        log.info("Start recording keyboard events")
        self._recording = True
        self._listener = keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release
        )
        self._listener_thread = threading.Thread(target=self._listener.start)
        self._listener_thread.daemon = True
        self._listener_thread.start()

    def stop(self):
        if not self._recording:
            return
        if not self._listener:
            return

        self._listener.stop()
        self._listener_thread.join()
        self._recording = False
        log.info("Stop recording keyboard events")
