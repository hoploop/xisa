# PYTHON IMPORTS
import base64
from io import BytesIO
import os
import shutil
import threading
from typing import Annotated, List, Optional, Tuple
import logging
import cv2
import yaml

# LIBRARY IMPORTS
from beanie import PydanticObjectId
from beanie.operators import And, Or, RegEx, In
from fastapi import Depends, Request
from PIL import Image
from ultralytics import YOLO

# LOCAL IMPORTS
from api.models.detector import Detector, DetectorClass, DetectorConfig, DetectorImage, DetectorImageLabel, DetectorImageMode
from api.controllers.recorder import VIDEO_EXT

# INITIALIZATION
log = logging.getLogger(__name__)


class StudioController:

    def __init__(self, detector_config: DetectorConfig):
        self.detector_config: DetectorConfig = detector_config
        
   


async def get_studio(request: Request) -> StudioController:
    if not hasattr(request.app.state, "studio"):
        request.app.state.studio = StudioController(request.app.state.config.detector)
    return request.app.state.studio


Studio = Annotated[StudioController, Depends(get_studio)]
