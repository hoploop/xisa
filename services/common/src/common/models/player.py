# PYTHON IMPORTS
from enum import Enum
from typing import List, Optional

# LIBRARY IMPORTS
from datetime import datetime

from beanie import Delete, Document, PydanticObjectId, before_event, Update,SaveChanges
from pydantic import Field

# LOCAL IMPORTS
from common.models.defaults import empty_list, utc_now

class Run(Document):
    detector: PydanticObjectId
    scenario: PydanticObjectId
    created: datetime = Field(default_factory=utc_now)
    updated: datetime = Field(default_factory=utc_now)
    start: Optional[datetime] = None
    end:Optional[datetime] = None
    user: PydanticObjectId
class StepResultStatus(str, Enum):
    UNKNOWN = 'unknown'
    RUNNING = 'running'
    SUCCESS = 'success'
    FAIL = 'fail'
    TRAINING_REQUIRED = 'training_required'
    
class StepResult(Document):
    scenario: PydanticObjectId
    step:PydanticObjectId
    start: Optional[datetime] = None
    end:Optional[datetime] = None
    status: StepResultStatus = StepResultStatus.UNKNOWN
    message: str = ''
    
class Step(Document):
    order: int
    scenario: PydanticObjectId
    by_label: Optional[str] = None
    by_text: Optional[str] = None
    by_regex: Optional[str] = None
    by_order: List[int] = Field(default_factory=empty_list)
    event:PydanticObjectId
    duration: float = 1.0
    retry: int = 10
    
    @before_event(Delete)
    async def remove_related(self):
        await StepResult.find_all(StepResult.step == self.id).delete()
        
class Scenario(Document):
    project: PydanticObjectId
    created: datetime = Field(default_factory=utc_now)
    updated: datetime = Field(default_factory=utc_now)
    groups: List[PydanticObjectId] = Field(default_factory=empty_list)
    users: List[PydanticObjectId] = Field(default_factory=empty_list)

    @before_event(Update, SaveChanges)
    async def update_last(self):
        self.updated = utc_now()
        
    @before_event(Delete)
    async def remove_related(self):
        await Step.find_all(Step.scenario == self.id).delete()
        await StepResult.find_all(StepResult.scenario == self.id).delete()
        await Run.find_all(Run.scenario == self.id).delete()
        
class Replay(Document):
    project: PydanticObjectId
    script: str = Field(default='')
    created: datetime = Field(default_factory=utc_now)
    updated: datetime = Field(default_factory=utc_now)    
    
    @before_event(Update, SaveChanges)
    async def update_last(self):
        self.updated = utc_now()
      
