# PYTHON IMPORTS
from datetime import datetime
from enum import Enum
import logging
from typing import Annotated, List, Literal, Optional


# LIBRARY IMPORTS
from beanie import Delete, Document, Insert, PydanticObjectId, SaveChanges, Update, before_event
from pydantic import BaseModel, Field

# LOCAL IMPORTS
from common.models.base import Position
from common.models.defaults import empty_list, utc_now
from common.models.trainer import TrainImageObject, TrainSession 

# INITIALIZATION
log = logging.getLogger(__name__)

class DetectorSuggestion(Document):
    by_label: Optional[str] = None
    by_text: Optional[str] = None
    by_regex: Optional[str] = None
    by_order: List[int] = Field(default_factory=empty_list)
    by_position: Optional[Position] = None
    event:PydanticObjectId
    confidence:float
    x:float
    y:float
    w:float
    h: float
    

class DetectorLabel(Document):
    detector: PydanticObjectId
    name: str
    created: datetime = Field(default_factory=utc_now)
    updated: datetime = Field(default_factory=utc_now)
    
    @before_event(Update, SaveChanges, Insert) 
    async def update_last(self):
        self.updated = utc_now()

class DetectorImageLabel(Document):
    image: PydanticObjectId
    created: datetime = Field(default_factory=utc_now)
    updated: datetime = Field(default_factory=utc_now)
    label: PydanticObjectId
    xstart:float
    xend:float
    ystart:float
    yend:float
    
    
    @before_event(Update, SaveChanges, Insert)
    async def update_last(self):
        self.updated = utc_now()
        
class DetectorImageMode(str, Enum):
    train = 'train'
    val = 'val'
    test = 'test'


class DetectorImage(Document):
    detector: PydanticObjectId
    data:str
    width:int
    height:int
    mode: DetectorImageMode = Field(default=DetectorImageMode.train)
    created: datetime = Field(default_factory=utc_now)
    updated: datetime = Field(default_factory=utc_now)
    
    @before_event(Update, SaveChanges, Insert)
    async def update_last(self):
        self.updated = utc_now()
        
    @before_event(Delete)
    async def remove_related(self):
        await DetectorImageLabel.find(DetectorImageLabel.image == self.id).delete()
      


class Detector(Document):
    project: PydanticObjectId
    name:str
    running: bool = Field(default=False)
    failed: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default="")
    created: datetime = Field(default_factory=utc_now)
    updated: datetime = Field(default_factory=utc_now)
    groups: List[PydanticObjectId] = Field(default_factory=empty_list)
    users: List[PydanticObjectId] = Field(default_factory=empty_list)
    best: Optional[str] = Field(default=None)
    last: Optional[str] = Field(default=None) 

    
    @before_event(Update, SaveChanges, Insert)
    async def update_last(self):
        self.updated = utc_now()
        
    @before_event(Delete)
    async def remove_related(self):
        await TrainImageObject.find(TrainImageObject.detector == self.id).delete()
        await DetectorImage.find(DetectorImage.detector == self.id).delete()
        await DetectorLabel.find(DetectorLabel.detector == self.id).delete()
        await TrainSession.find(TrainSession.detector == self.id).delete()
     
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
    
    
class DetectObject(BaseModel):
    x: float
    y: float
    w: float
    h: float
    confidence:float
    code: int
    name: str
    row: int
    col: int
    
class DetectText(BaseModel):
    x: float
    y: float
    h: float
    w: float
    page: int
    block: int
    par: int
    line: int
    word: int
    value: str
    confidence: float
     
            