# PYTHON IMPORTS
from enum import Enum
from typing import List, Literal, Optional, Union

# LIBRARY IMPORTS
from datetime import datetime

from beanie import Delete, Document, PydanticObjectId, before_event, Update,SaveChanges
from pydantic import BaseModel, Field

# LOCAL IMPORTS
from common.models.base import Position
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
    by_position: Optional[Position] = None
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
    record: PydanticObjectId
    script: str = Field(default='')
    created: datetime = Field(default_factory=utc_now)
    updated: datetime = Field(default_factory=utc_now)    
    
    @before_event(Update, SaveChanges)
    async def update_last(self):
        self.updated = utc_now()
      

class Selector(BaseModel):
    type:str  
    
    def render(self)->str:
        return ''
    
    
class SelectorReference(Selector):
    type: Literal['selector.reference'] = 'selector.reference'    
    reference: str
    
    def render(self):
        return self.reference
class LabelSelector(Selector):
    type: Literal['selector.label'] = 'selector.label'
    value: str
    order: List[int] = Field(default_factory=empty_list)
    
    def render(self)->str:
        torder = ''
        for el in self.order:
            torder += ',{0}'.format(el)
        return 'label("{0},{1}")'.format(self.value,torder)
    
class TextSelector(Selector):
    type: Literal['selector.text'] = 'selector.text'
    value: str
    order: List[int] = Field(default_factory=empty_list)
    
    def render(self)->str:
        torder = ''
        for el in self.order:
            torder += ',{0}'.format(el)
        return 'text("{0},{1}")'.format(self.value,torder)

class PositionSelector(Selector):
    type: Literal['selector.position'] = 'selector.position'
    x: float
    y: float
    
    def render(self)->str:
        tx = "{:.2f}".format(self.x)
        ty = "{:.2f}".format(self.y)
        return 'position({0},{1})'.format(tx,ty)
    
    
class RegexSelector(Selector):
    type: Literal['selector.regex'] = 'selector.regex'
    value: str
    order: List[int] = Field(default_factory=empty_list)
    
    def render(self)->str:
        torder = ''
        for el in self.order:
            torder += ',{0}'.format(el)
        return 'regex("{0},{1}")'.format(self.value,torder)
    
class Operation(BaseModel):
    type: str
    
    def render(self)->str:
        return ''
    
    
class OperationReference(Operation):
    type: Literal['operation.reference'] = 'operation.reference'
    reference: str
    
    def render(self):
        return self.reference
    
class WaitOperation(Operation):
    type: Literal['operation.wait'] = 'operation.wait'
    value: int = 1000
    selector: Selector
    
    def render(self):
        return 'wait({0},{1})'.format(self.selector.render(),self.value)



class MouseOperationButton(Enum,str):
    LEFT = 'left'
    MIDDLE = 'middle'
    RIGHT = 'right'
class MousePressOperation(Operation):
    type: Literal['operation.mouse.press'] = 'operation.mouse.press'
    selector: Selector
    button: MouseOperationButton = Field(default=MouseOperationButton.LEFT)
    
    
    def render(self):
        but = 'left'
        if self.button == MouseOperationButton.MIDDLE:
            but = 'middle'
        elif self.button == MouseOperationButton.RIGHT:
            but = 'right'
        return 'mousePress({0},{1})'.format(self.selector.render(),but)


    
class MouseReleaseOperation(Operation):
    type: Literal['operation.mouse.release'] = 'operation.mouse.release'
    selector: Selector
    button: MouseOperationButton = Field(default=MouseOperationButton.LEFT)
    
    def render(self):
        but = 'left'
        if self.button == MouseOperationButton.MIDDLE:
            but = 'middle'
        elif self.button == MouseOperationButton.RIGHT:
            but = 'right'
        return 'mouseRelease({0},{1})'.format(self.selector.render(),but)


    
class MouseClickOperation(Operation):
    type: Literal['operation.mouse.click'] = 'operation.mouse.click'
    selector: Selector
    button: MouseOperationButton = Field(default=MouseOperationButton.LEFT)
    
    
    def render(self):
        but = 'left'
        if self.button == MouseOperationButton.MIDDLE:
            but = 'middle'
        elif self.button == MouseOperationButton.RIGHT:
            but = 'right'
        return 'mouseClick({0},{1})'.format(self.selector.render(),but)


        
class MouseDoubleClickOperation(Operation):
    type: Literal['operation.mouse.double.click'] = 'operation.mouse.double.click'
    selector: Selector
    button: MouseOperationButton = Field(default=MouseOperationButton.LEFT)
    
    def render(self):
        but = 'left'
        if self.button == MouseOperationButton.MIDDLE:
            but = 'middle'
        elif self.button == MouseOperationButton.RIGHT:
            but = 'right'
        return 'mouseDoubleClick({0},{1})'.format(self.selector.render(),but)

class MouseScrollOperation(Operation):
    type: Literal['operation.mouse.scroll'] = 'operation.mouse.scroll'
    dx: int
    dy: int
    
    def render(self):
        return 'mouseScroll({0},{1})'.format(self.dx,self.dy)
    
class KeyPressOperation(Operation):
    type: Literal['operation.key.press'] = 'operation.key.press'
    value: str    
    
    def render(self):
        return 'keyPress("{0}")'.format(self.value)

class KeyReleaseOperation(Operation):
    type: Literal['operation.key.release'] = 'operation.key.release'
    value: str
    
    def render(self):
        return 'keyRelease("{0}")'.format(self.value)
        
class Statement(BaseModel):
    type: str
    
    def render(self) -> str:
        return ''
    
class CreateDetectorStatement(Statement):
    type: Literal['statement.create.detector'] = 'statement.create.detector'
    id: str
    value: str
    
    def render(self):
        return '{0} = detector("{1}")'.format(self.id,self.value)
    
class UseDetectorStatement(Statement):
    type: Literal['statement.use.detector'] = 'statement.use.detector'
    id: str
    confidence: float = Field(default=0.1)
    
    def render(self):
        tconf = "{:.2f}".format(self.confidence)
        return '{0} = use({1},{2})'.format(self.id,self.value,tconf)
    
class CreateSelectorStatement(Statement):
    type: Literal['statement.create.selector'] = 'statement.create.selector'
    id: str
    selector: Selector
    
    def render(self):
        return '{0} = {1}'.format(self.id,self.selector.render())
    
class CreateOperationStatement(Statement):    
    type: Literal['statement.create.operation'] = 'statement.create.operation'
    id: str
    operation: Operation
    
    def render(self):
        return '{0} = {1}'.format(self.id,self.operation.render())
    
    
class CreateSequenceStatement(Statement):    
    type: Literal['statement.create.sequence'] = 'statement.create.sequence'
    id: str
    operations: List[Operation] = Field(default=empty_list)
    
    def render(self):
        content = ''
        for op in self.operations:
            content += '\r\n{0}'.format(op.render())
        return '{0} = SEQUENCE { {1} }'.format(self.id,content)
    
    
class RunOperationStatement(Statement):
    type: Literal['statement.run.operation'] = 'statement.run.operation'
    operation: Operation
    
    def render(self):
        return self.operation.render()