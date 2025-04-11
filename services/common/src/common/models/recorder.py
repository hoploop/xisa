# PYTHON IMPORTS
from datetime import datetime
from enum import Enum
from typing import Annotated, List, Literal, Optional, Union


# LIBRARY IMPORTS
from beanie import Delete, Document, PydanticObjectId, SaveChanges, Update, before_event
from pydantic import Field

# LOCAL IMPORTS
from common.models.base import Position
from common.models.defaults import empty_list, utc_now
from common.models.player import Replay
from common.models.trainer import TrainLesson


class OS(Document):
    name: str
    version: str


class Action(Document):
    record: PydanticObjectId
    event: PydanticObjectId
    by_label: Optional[str] = None
    by_text: Optional[str] = None
    by_regex: Optional[str] = None
    by_position: Optional[Position] = None
    by_order: List[int] = Field(default_factory=empty_list)
    confidence:float
    image: Optional[str] = None
    created: datetime = Field(default_factory=utc_now)
    updated: datetime = Field(default_factory=utc_now)    
    
    @before_event(Update, SaveChanges)
    async def update_last(self):
        self.updated = utc_now()    

class Event(Document):
    type: str
    record: PydanticObjectId
    frame: int
    synthetic: bool = Field(default=False)
    timestamp: datetime = Field(default_factory=utc_now)

    class Settings:
        is_root = True
        
    
    @before_event(Delete)
    async def remove_related(self):
        await Action.find_many(Action.event == self.id).delete()


class MouseButton(str, Enum):
    left = 'left'
    middle = 'middle'
    right = 'right'


class MouseClickEvent(Event):
    type: Literal["mouse.click"] = "mouse.click"
    button: MouseButton = Field(default=MouseButton.left)
    position: tuple[float, float] | None = None  # For mouse events


class MousePressEvent(Event):
    type: Literal["mouse.press"] = "mouse.press"
    button: MouseButton = Field(default=MouseButton.left)
    position: tuple[float, float] | None = None  # For mouse events


class MouseReleaseEvent(Event):
    type: Literal["mouse.release"] = "mouse.release"
    button: MouseButton = Field(default=MouseButton.left)
    position: tuple[float, float] | None = None  # For mouse events


class MouseScrollEvent(Event):
    type: Literal["mouse.scroll"] = "mouse.scroll"
    dx: int
    dy: int
    position: tuple[float, float] | None = None  # For mouse events


class MouseDoubleClickEvent(Event):
    type: Literal["mouse.double.click"] = "mouse.double.click"
    button: MouseButton = Field(default=MouseButton.left)
    position: tuple[float, float] | None = None  # For mouse events


class MouseDropEvent(Event):
    type: Literal["mouse.drop"] = "mouse.drop"
    button: MouseButton = Field(default=MouseButton.left)
    position: tuple[float, float] | None = None  # For mouse events
    origin: tuple[float, float] | None = None  # For mouse events


class KeyPressEvent(Event):
    type: Literal["key.press"] = "key.press"
    key: str

class KeyTypeEvent(Event):
    type: Literal["key.type"] = "key.type"
    key: str

class KeyReleaseEvent(Event):
    type: Literal["key.release"] = "key.release"
    key: str


class KeyComboPressEvent(Event):
    type: Literal["key.combo.press"] = "key.combo.press"
    keys: List[str]


EVENT_TYPES = Union[
    MouseClickEvent,
    MouseDoubleClickEvent,
    MousePressEvent,
    MouseReleaseEvent,
    MouseScrollEvent,
    MouseDropEvent, 
    MouseDoubleClickEvent,
    KeyComboPressEvent,
    KeyPressEvent,
    KeyReleaseEvent,
    KeyTypeEvent
    
]

EVENTS = Annotated[EVENT_TYPES, Field(discriminator="type")]


class Record(Document):
    project: PydanticObjectId
    name: str
    os: OS
    description: str = Field(default="")
    created: datetime = Field(default_factory=utc_now)
    updated: datetime = Field(default_factory=utc_now)
    start: datetime = Field(default_factory=utc_now)
    end: datetime = Field(default_factory=utc_now)
    groups: List[PydanticObjectId] = Field(default_factory=empty_list)
    users: List[PydanticObjectId] = Field(default_factory=empty_list)

    @before_event(Update, SaveChanges)
    async def update_last(self):
        self.updated = utc_now()

    @before_event(Delete)
    async def remove_related(self):
        await TrainLesson.find_all(TrainLesson.record == self.id).delete()
        await Event.find_many(Event.record == self.id, with_children=True).delete()
        await Action.find_many(Action.record == self.id, with_children=True).delete()
        await Replay.find_many(Replay.record == self.id).delete()

