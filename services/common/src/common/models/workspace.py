# PYTHON IMPORTS
from datetime import datetime
from typing import List, Optional


# LIBRARY IMPORTS
from beanie import (
    Delete,
    Document,
    PydanticObjectId,
    SaveChanges,
    Update,
    before_event,
)
from pydantic import Field

# LOCAL IMPORTS
from common.models.defaults import empty_list, utc_now
from common.models.recorder import Record
from common.models.detector import Detector



class Project(Document):
    name: str
    description: str = Field(default="")
    created: datetime = Field(default_factory=utc_now)
    updated: datetime = Field(default_factory=utc_now)
    groups: List[PydanticObjectId] = Field(default_factory=empty_list)
    users: List[PydanticObjectId] = Field(default_factory=empty_list)

    @before_event(Update, SaveChanges)
    async def update_last(self):
        self.updated = utc_now()
        
    @before_event(Delete)
    async def remove_related(self):
        await Record.find_all(Record.project == self.id).delete()
        await Detector.find_all(Detector.project == self.id).delete()

