from common.rpc import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TrainImageObjectToDetectorRequest(_message.Message):
    __slots__ = ("user", "detector", "record")
    USER_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    user: str
    detector: str
    record: str
    def __init__(self, user: _Optional[str] = ..., detector: _Optional[str] = ..., record: _Optional[str] = ...) -> None: ...

class TrainImageObjectToDetectorResponse(_message.Message):
    __slots__ = ("status", "message", "total")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    total: int
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., total: _Optional[int] = ...) -> None: ...

class TrainImageObjectRemoveRequest(_message.Message):
    __slots__ = ("user", "id")
    USER_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    user: str
    id: str
    def __init__(self, user: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class TrainImageObjectRemoveResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ...) -> None: ...

class TrainImageObjectUpdateRequest(_message.Message):
    __slots__ = ("user", "labels", "id", "train", "test", "val", "xstart", "xend", "ystart", "yend")
    USER_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TRAIN_FIELD_NUMBER: _ClassVar[int]
    TEST_FIELD_NUMBER: _ClassVar[int]
    VAL_FIELD_NUMBER: _ClassVar[int]
    XSTART_FIELD_NUMBER: _ClassVar[int]
    XEND_FIELD_NUMBER: _ClassVar[int]
    YSTART_FIELD_NUMBER: _ClassVar[int]
    YEND_FIELD_NUMBER: _ClassVar[int]
    user: str
    labels: _containers.RepeatedScalarFieldContainer[str]
    id: str
    train: bool
    test: bool
    val: bool
    xstart: float
    xend: float
    ystart: float
    yend: float
    def __init__(self, user: _Optional[str] = ..., labels: _Optional[_Iterable[str]] = ..., id: _Optional[str] = ..., train: bool = ..., test: bool = ..., val: bool = ..., xstart: _Optional[float] = ..., xend: _Optional[float] = ..., ystart: _Optional[float] = ..., yend: _Optional[float] = ...) -> None: ...

class TrainImageObjectUpdateResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ...) -> None: ...

class TrainImageObjectRequest(_message.Message):
    __slots__ = ("user", "detector", "frame", "labels", "xstart", "xend", "ystart", "yend", "train", "test", "val", "record")
    USER_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_FIELD_NUMBER: _ClassVar[int]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    XSTART_FIELD_NUMBER: _ClassVar[int]
    XEND_FIELD_NUMBER: _ClassVar[int]
    YSTART_FIELD_NUMBER: _ClassVar[int]
    YEND_FIELD_NUMBER: _ClassVar[int]
    TRAIN_FIELD_NUMBER: _ClassVar[int]
    TEST_FIELD_NUMBER: _ClassVar[int]
    VAL_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    user: str
    detector: str
    frame: int
    labels: _containers.RepeatedScalarFieldContainer[str]
    xstart: float
    xend: float
    ystart: float
    yend: float
    train: bool
    test: bool
    val: bool
    record: str
    def __init__(self, user: _Optional[str] = ..., detector: _Optional[str] = ..., frame: _Optional[int] = ..., labels: _Optional[_Iterable[str]] = ..., xstart: _Optional[float] = ..., xend: _Optional[float] = ..., ystart: _Optional[float] = ..., yend: _Optional[float] = ..., train: bool = ..., test: bool = ..., val: bool = ..., record: _Optional[str] = ...) -> None: ...

class TrainImageObjectResponse(_message.Message):
    __slots__ = ("status", "message", "object")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    object: _base_pb2.Serialized
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., object: _Optional[_Union[_base_pb2.Serialized, _Mapping]] = ...) -> None: ...

class TrainImageObjectListRequest(_message.Message):
    __slots__ = ("user", "detector", "record", "frame")
    USER_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    user: str
    detector: str
    record: str
    frame: int
    def __init__(self, user: _Optional[str] = ..., detector: _Optional[str] = ..., record: _Optional[str] = ..., frame: _Optional[int] = ...) -> None: ...

class TrainImageObjectListResponse(_message.Message):
    __slots__ = ("status", "message", "total", "objects")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    total: int
    objects: _containers.RepeatedCompositeFieldContainer[_base_pb2.Serialized]
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., total: _Optional[int] = ..., objects: _Optional[_Iterable[_Union[_base_pb2.Serialized, _Mapping]]] = ...) -> None: ...

class TrainImageObjectCountByDetectorRequest(_message.Message):
    __slots__ = ("user", "detector")
    USER_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_FIELD_NUMBER: _ClassVar[int]
    user: str
    detector: str
    def __init__(self, user: _Optional[str] = ..., detector: _Optional[str] = ...) -> None: ...

class TrainImageObjectCountByDetectorResponse(_message.Message):
    __slots__ = ("status", "message", "total")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    total: int
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., total: _Optional[int] = ...) -> None: ...
