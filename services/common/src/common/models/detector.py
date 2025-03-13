# PYTHON IMPORTS
from datetime import datetime
from enum import Enum
import logging
from typing import Annotated, List, Literal, Optional


# LIBRARY IMPORTS
from beanie import Delete, Document, Insert, PydanticObjectId, SaveChanges, Update, before_event
from pydantic import BaseModel, Field

# LOCAL IMPORTS
from common.models.defaults import empty_list, utc_now

# INITIALIZATION
log = logging.getLogger(__name__)

class DetectorClass(Document):
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
    classes: List[PydanticObjectId] = Field(default_factory=empty_list)
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
        await DetectorImageLabel.find_all(DetectorImageLabel.image == self.id).delete()
      


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
        await DetectorImage.find_all(DetectorImage.detector == self.id).delete()
        await DetectorClass.find_all(DetectorClass.detector == self.id).delete()
     