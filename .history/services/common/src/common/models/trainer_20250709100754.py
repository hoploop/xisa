# PYTHON IMPORTS
from datetime import datetime
from enum import IntEnum
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


class TrainSessionStatus(IntEnum):
    IDLE = 0
    RUNNING = 1
    COMPLETED = 2
    ERROR = 3

class TrainSession(Document):
    detector: PydanticObjectId
    user: PydanticObjectId
    status: TrainSessionStatus = TrainSessionStatus.IDLE
    created: datetime = Field(default_factory=utc_now)
    updated: datetime = Field(default_factory=utc_now)
    errors: List[str] = Field(default_factory=empty_list)
    