# LOCAL IMPORTS
from api.models.auth import Group, Token, User, UserGroup
from api.models.workspace import Project
from api.models.recorder import OS, Event, KeyComboPressEvent, KeyPressEvent, KeyReleaseEvent, MouseClickLeftEvent, MouseClickRightEvent, MouseDoubleClickEvent, MousePressLeftEvent, MousePressMiddleEvent, MousePressRightEvent, MouseReleaseLeftEvent, MouseReleaseMiddleEvent, MouseReleaseRightEvent, MouseScrollEvent, Record
from api.models.detector import Detector, DetectorClass, DetectorImage, DetectorImageLabel


MODELS = [
    Group,
    UserGroup,
    User, 
    Token,
    Project,
    OS,
    Record,
    Event,
    MouseClickLeftEvent,
    MousePressLeftEvent,
    MouseReleaseLeftEvent,
    MousePressRightEvent,
    MouseReleaseRightEvent,
    MouseClickRightEvent,
    MousePressMiddleEvent,
    MouseReleaseMiddleEvent,
    MouseScrollEvent,
    MouseDoubleClickEvent,
    KeyPressEvent,
    KeyReleaseEvent,
    KeyComboPressEvent,
    Detector,
    DetectorImage,
    DetectorClass, 
    DetectorImageLabel
]