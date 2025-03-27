# PYTHON IMPORTS
from datetime import datetime
from typing import Optional

# LIBRARY IMPORTS
from beanie import Delete, Document, before_event, Update,SaveChanges,Insert
from beanie import PydanticObjectId
from pydantic import Field

# LOCAL IMPORTS
from common.models.defaults import utc_now


class TrainImageObject(Document):
    lesson: PydanticObjectId
    frame: int
    label: str
    xstart:float
    xend:float
    ystart:float
    yend:float
    created: datetime = Field(default_factory=utc_now)
    updated: datetime = Field(default_factory=utc_now)
    
    @before_event(Update, SaveChanges, Insert)
    async def update_last(self):
        self.updated = utc_now()
        
class TrainLesson(Document):
    record: PydanticObjectId
    detector: Optional[PydanticObjectId] = None
    created: datetime = Field(default_factory=utc_now)
    updated: datetime = Field(default_factory=utc_now)
    
    
    @before_event(Update, SaveChanges, Insert)
    async def update_last(self):
        self.updated = utc_now()
        
    @before_event(Delete)
    async def remove_related(self):
        await TrainImageObject.find_all(TrainImageObject.lesson == self.id).delete()
        

    
        