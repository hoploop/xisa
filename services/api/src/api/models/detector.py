# PYTHON IMPORTS
from datetime import datetime
from enum import Enum
import logging
from typing import List, Literal


# LIBRARY IMPORTS
from beanie import PydanticObjectId
from pydantic import BaseModel, Field

# LOCAL IMPORTS
from api.models.defaults import utc_now
from common.models.detector import Detector, DetectorClass, DetectorImage, DetectorImageLabel

# INITIALIZATION
log = logging.getLogger(__name__)


class DetectorListResponse(BaseModel):
    detectors: List[Detector]
    total: int
                

class DetectorImageListResponse(BaseModel):
    images: List[DetectorImage]
    total: int
                          


class DetectorImageLabelListResponse(BaseModel):
    images: List[DetectorImageLabel]
    total: int
                                                            
                                                            
class DetectorClassListResponse(BaseModel):
    classes: List[DetectorClass]
    total: int
                            
                            
class DetectorImageLabelAdd(BaseModel):
    image_id:PydanticObjectId
    xstart:float
    xend:float
    ystart:float
    yend:float
    classes:List[str]                                                         
    
class DetectorTrainingSession(BaseModel):
    type:Literal['detector.training.session'] = 'detector.training.session'
    detector: PydanticObjectId
    epoch_progress: int
    epoch_total: int
    box_loss: float
    class_loss: float
    object_loss: float 
    created: datetime = Field(default_factory=utc_now)
    updated: datetime = Field(default_factory=utc_now)
    user: PydanticObjectId
    