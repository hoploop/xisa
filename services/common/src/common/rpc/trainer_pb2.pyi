from common.rpc import base_pb2 as _base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TrainImageObjectRequest(_message.Message):
    __slots__ = ("user", "lesson", "frame", "label", "xstart", "xend", "ystart", "yend")
    USER_FIELD_NUMBER: _ClassVar[int]
    LESSON_FIELD_NUMBER: _ClassVar[int]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    XSTART_FIELD_NUMBER: _ClassVar[int]
    XEND_FIELD_NUMBER: _ClassVar[int]
    YSTART_FIELD_NUMBER: _ClassVar[int]
    YEND_FIELD_NUMBER: _ClassVar[int]
    user: str
    lesson: str
    frame: int
    label: str
    xstart: float
    xend: float
    ystart: float
    yend: float
    def __init__(self, user: _Optional[str] = ..., lesson: _Optional[str] = ..., frame: _Optional[int] = ..., label: _Optional[str] = ..., xstart: _Optional[float] = ..., xend: _Optional[float] = ..., ystart: _Optional[float] = ..., yend: _Optional[float] = ...) -> None: ...

class TrainImageObjectResponse(_message.Message):
    __slots__ = ("status", "message", "id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    id: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class LessonSetDetectorRequest(_message.Message):
    __slots__ = ("user", "detector", "lesson")
    USER_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_FIELD_NUMBER: _ClassVar[int]
    LESSON_FIELD_NUMBER: _ClassVar[int]
    user: str
    detector: str
    lesson: str
    def __init__(self, user: _Optional[str] = ..., detector: _Optional[str] = ..., lesson: _Optional[str] = ...) -> None: ...

class LessonSetDetectorResponse(_message.Message):
    __slots__ = ("status", "message", "lesson")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LESSON_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    lesson: _base_pb2.Serialized
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., lesson: _Optional[_Union[_base_pb2.Serialized, _Mapping]] = ...) -> None: ...

class RecordHasLessonRequest(_message.Message):
    __slots__ = ("user", "record")
    USER_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    user: str
    record: str
    def __init__(self, user: _Optional[str] = ..., record: _Optional[str] = ...) -> None: ...

class RecordHasLessonResponse(_message.Message):
    __slots__ = ("status", "message", "lesson")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LESSON_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    lesson: _base_pb2.Serialized
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., lesson: _Optional[_Union[_base_pb2.Serialized, _Mapping]] = ...) -> None: ...

class RecordCreateLessonRequest(_message.Message):
    __slots__ = ("user", "record")
    USER_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    user: str
    record: str
    def __init__(self, user: _Optional[str] = ..., record: _Optional[str] = ...) -> None: ...

class RecordCreateLessonResponse(_message.Message):
    __slots__ = ("status", "message", "lesson")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LESSON_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    lesson: _base_pb2.Serialized
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., lesson: _Optional[_Union[_base_pb2.Serialized, _Mapping]] = ...) -> None: ...
