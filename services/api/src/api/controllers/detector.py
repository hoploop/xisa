# PYTHON IMPORTS
import asyncio
import base64
from io import BytesIO
import json
import logging
import os
import shutil
import threading
from typing import Annotated, List, Optional, Tuple

# LIBRARY IMPORTS
from beanie import PydanticObjectId
from beanie.operators import And, Or, In, RegEx
import cv2
from fastapi import Depends, Request
from pydantic import BaseModel
import pytesseract
from pytesseract import Output
from ultralytics import YOLO
import yaml
from PIL import Image

# LOCAL IMPORTS
from api.models.detector import (
    Detector,
    DetectorClass,
    DetectorImage,
    DetectorImageLabel,
    DetectorImageMode,
    DetectorTrainingSession,
)
from api.routers.ws import Websocket, WsManager
from api.models.recorder import Record
from common.utils.imaging import ImageGrid

# INITIALIZATION
log = logging.getLogger(__name__)
VIDEO_EXT = '.mp4'


class DetectorControllerConfig(BaseModel):
    path: str
    original: str
    name: str
    data: str
    runs: str
    classes: str
    video:str


class DetectorController:

    def __init__(self, config: DetectorControllerConfig,wsManager:WsManager):
        self.config: DetectorControllerConfig = config
        self.wsManager:WsManager = wsManager


    
    async def objects_from_record_frame(self,user_id:PydanticObjectId,detector_id:PydanticObjectId, record_id:PydanticObjectId, frame:int,confidence:float=0.1):
        detector = Detector.find_many(Detector.id == detector_id).first_or_none()
        if detector is None:
            raise Exception("workspace.detector.errors.not_found")
        
        filename = os.path.join(self.config.video,str(record_id)+VIDEO_EXT)
        cap = cv2.VideoCapture(filename)

        if not cap.isOpened():
            raise("Error: Could not open video file.")
            
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame)
        
        # Read the specific frame
        ret, frame = cap.read()
        
        if not ret:
            raise Exception(f"Error: Could not read frame {frame}.")
        
        # Check if frame was successfully read
        # Convert BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)
        cap.release()
        
        log.debug("Loading model")
        model_path = os.path.join(self.config.path, detector.best)
        model = YOLO(model_path)
        
        log.debug("Detecting visual elements for frame: {0}".format(frame))
        visual_results = model(img, conf=confidence)  # predict on an image
        grid = ImageGrid(img.size[0], img.size[1])
        
        boxes = []
            

        

        # Access the results
        for result in visual_results:
            detections = json.loads(result.to_json())
            for detection in detections:
                x = detection["box"]["x1"]
                y = detection["box"]["y1"]
                w = detection["box"]["x2"] - detection["box"]["x1"]
                h = detection["box"]["y2"] - detection["box"]["y1"]
                boxes.append((x, y, w, h))
            # {'name': 'remote', 'class': 65, 'confidence': 0.63305, 'box': {'x1': 1.52126, 'y1': 49.41976, 'x2': 115.40047, 'y2': 946.6156}}
        
        best_rows, best_cols = grid.optimal_grid_size(boxes)      
        
        for result in visual_results:
            detections = json.loads(result.to_json())
            for detection in detections:
                c = detection['name']
                x = detection["box"]["x1"]
                y = detection["box"]["y1"]
                w = detection["box"]["x2"] - detection["box"]["x1"]
                h = detection["box"]["y2"] - detection["box"]["y1"]
                row, col = grid.classify_box(best_rows, best_cols, x, y, w, h)

        
        log.debug("Detecting text elements for frame: {0}".format(frame))
        # Get verbose data including boxes, confidences, line and page numbers
        text_results = pytesseract.image_to_data(img, output_type=Output.DICT)
        text_matches = []
        n_boxes = len(text_results["text"])
        for i in range(n_boxes):
            conf = int(text_results["conf"][i])
            text = text_results["text"][i]
            if conf > 60:
                x = text_results["left"][i]
                y = text_results["top"][i]
                w = text_results["width"][i]
                h = text_results["height"][i]
                page = text_results["page_num"][i]
                block = text_results["block_num"][i]
                par = text_results["par_num"][i]
                line = text_results["line_num"][i]
                word = text_results["word_num"][i]
        
        
   
   
   

async def get_detector_controller(request: Request, wsManager: Websocket) -> DetectorController:
    if not hasattr(request.app.state, "detector"):
        request.app.state.detector = DetectorController(
            request.app.state.config.detector, wsManager
        )
    return request.app.state.detector


GetDetectorController = Annotated[DetectorController, Depends(get_detector_controller)]
