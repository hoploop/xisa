
# PYTHON IMPORTS
import logging
import os
from datetime import datetime
import threading

# LIBRARY IMPORTS
import numpy as np
import cv2
import pyautogui

# LOCAL IMPORTS

from recorder.constants import VIDEO_EXT



# INITIALIZATION
log = logging.getLogger(__name__)

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

