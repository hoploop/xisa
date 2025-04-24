# PYTHON IMPORTS
from datetime import datetime
from typing import List, Optional

# LIBRARY IMPORTS
from beanie import Delete, Document, before_event, Update, SaveChanges, Insert
from beanie import PydanticObjectId
from pydantic import Field

# LOCAL IMPORTS
from common.models.defaults import empty_list, utc_now


class TrainImageObject(Document):
    record: PydanticObjectId
    detector: PydanticObjectId
    frame: int
    labels: List[str] = Field(default_factory=empty_list)
    xstart: float
    xend: float
    ystart: float
    yend: float
    test: bool = Field(default=False)
    train: bool = Field(default=True)
    val: bool = Field(default=True)
    created: datetime = Field(default_factory=utc_now)
    updated: datetime = Field(default_factory=utc_now)
    archived: bool = Field(default=False)

    @before_event(Update, SaveChanges, Insert)
    async def update_last(self):
        self.updated = utc_now()


