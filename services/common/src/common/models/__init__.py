from common.models.auth import Group, Token, User, UserGroup
from common.models.detector import Detector, DetectorLabel, DetectorImage, DetectorImageLabel, DetectorSuggestion
from common.models.player import Replay
from common.models.recorder import OS, Action, Event, KeyComboPressEvent, KeyPressEvent, KeyReleaseEvent, KeyTypeEvent, MouseClickEvent,  MouseDoubleClickEvent, MouseDropEvent, MousePressEvent, MouseReleaseEvent,  MouseScrollEvent, Record
from common.models.trainer import TrainImageObject
from common.models.workspace import Project


MODELS = [
    Group,
    UserGroup,
    User, 
    Token,
    Project,
    OS,
    Record,
    Event,
    MouseClickEvent,
    MousePressEvent,
    MouseDropEvent,
    MouseReleaseEvent,
    MouseScrollEvent,
    MouseDoubleClickEvent,
    KeyPressEvent,
    KeyReleaseEvent,
    KeyTypeEvent,
    KeyComboPressEvent,
    Detector,
    DetectorImage,
    DetectorLabel, 
    DetectorImageLabel,
    DetectorSuggestion,
    TrainImageObject,
    Replay,
    Action
]