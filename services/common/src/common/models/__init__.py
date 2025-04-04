from common.models.auth import Group, Token, User, UserGroup
from common.models.detector import Detector, DetectorLabel, DetectorImage, DetectorImageLabel, DetectorSuggestion
from common.models.player import Replay
from common.models.recorder import OS, Action, Event, KeyComboPressEvent, KeyPressEvent, KeyReleaseEvent, MouseClickLeftEvent, MouseClickRightEvent, MouseDoubleClickEvent, MousePressLeftEvent, MousePressMiddleEvent, MousePressRightEvent, MouseReleaseLeftEvent, MouseReleaseMiddleEvent, MouseReleaseRightEvent, MouseScrollEvent, Record
from common.models.trainer import TrainImageObject, TrainLesson
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
    DetectorLabel, 
    DetectorImageLabel,
    DetectorSuggestion,
    TrainLesson,
    TrainImageObject,
    Replay,
    Action
]