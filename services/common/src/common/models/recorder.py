# PYTHON IMPORTS
from datetime import datetime
from typing import Annotated, List, Literal, Union


# LIBRARY IMPORTS
from beanie import Delete, Document, PydanticObjectId, SaveChanges, Update, before_event
from pydantic import Field

# LOCAL IMPORTS
from common.models.defaults import empty_list, utc_now


class OS(Document):
    name: str
    version: str


class Event(Document):
    type: str
    record: PydanticObjectId
    frame: int
    timestamp: datetime = Field(default_factory=utc_now)

    class Settings:
        is_root = True


class MouseClickLeftEvent(Event):
    type: Literal["mouse.click.left"] = "mouse.click.left"
    position: tuple[float, float] | None = None  # For mouse events


class MouseClickRightEvent(Event):
    type: Literal["mouse.click.right"] = "mouse.click.right"
    position: tuple[float, float] | None = None  # For mouse events


class MousePressLeftEvent(Event):
    type: Literal["mouse.press.left"] = "mouse.press.left"
    position: tuple[float, float] | None = None  # For mouse events


class MousePressRightEvent(Event):
    type: Literal["mouse.press.right"] = "mouse.press.right"
    position: tuple[float, float] | None = None  # For mouse events


class MousePressMiddleEvent(Event):
    type: Literal["mouse.press.middle"] = "mouse.press.middle"
    position: tuple[float, float] | None = None  # For mouse events


class MouseReleaseLeftEvent(Event):
    type: Literal["mouse.release.left"] = "mouse.release.left"
    position: tuple[float, float] | None = None  # For mouse events


class MouseReleaseMiddleEvent(Event):
    type: Literal["mouse.release.middle"] = "mouse.release.middle"
    position: tuple[float, float] | None = None  # For mouse events


class MouseReleaseRightEvent(Event):
    type: Literal["mouse.release.right"] = "mouse.release.right"
    position: tuple[float, float] | None = None  # For mouse events


class MouseScrollEvent(Event):
    type: Literal["mouse.scroll"] = "mouse.scroll"
    dx: int
    dy: int
    position: tuple[float, float] | None = None  # For mouse events


class MouseDoubleClickEvent(Event):
    type: Literal["mouse.double.click"] = "mouse.double.click"
    position: tuple[float, float] | None = None  # For mouse events


class KeyPressEvent(Event):
    type: Literal["key.press"] = "key.press"
    key: str


class KeyReleaseEvent(Event):
    type: Literal["key.release"] = "key.release"
    key: str


class KeyComboPressEvent(Event):
    type: Literal["key.combo.press"] = "key.combo.press"
    keys: List[str]


EVENT_TYPES = Union[
    MouseClickLeftEvent,
    MouseClickRightEvent,
    MouseDoubleClickEvent,
    MousePressLeftEvent,
    MousePressMiddleEvent,
    MousePressRightEvent,
    MouseReleaseLeftEvent,
    MouseReleaseMiddleEvent,
    MouseReleaseRightEvent,
    MouseScrollEvent,
    KeyComboPressEvent,
    KeyPressEvent,
    KeyReleaseEvent,
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
        await Event.find_many(Event.record == self.id, with_children=True).delete()

