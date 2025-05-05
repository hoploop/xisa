
from typing import Union
from common.models.detector import DetectorTrainingSession
from common.models.player import PlayerStepSession


WS_MESSAGES = Union[None,DetectorTrainingSession,PlayerStepSession]