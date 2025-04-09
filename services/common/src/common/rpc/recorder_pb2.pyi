from common.rpc import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExistRecordEventActionRequest(_message.Message):
    __slots__ = ("user", "event")
    USER_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    user: str
    event: str
    def __init__(self, user: _Optional[str] = ..., event: _Optional[str] = ...) -> None: ...

class ExistRecordEventActionResponse(_message.Message):
    __slots__ = ("status", "message", "found")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FOUND_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    found: bool
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., found: bool = ...) -> None: ...

class UpdateRecordActionRequest(_message.Message):
    __slots__ = ("user", "id", "event", "byLabel", "byText", "byRegex", "byOrder", "byPosition", "confidence", "image")
    USER_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    BYLABEL_FIELD_NUMBER: _ClassVar[int]
    BYTEXT_FIELD_NUMBER: _ClassVar[int]
    BYREGEX_FIELD_NUMBER: _ClassVar[int]
    BYORDER_FIELD_NUMBER: _ClassVar[int]
    BYPOSITION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    user: str
    id: str
    event: str
    byLabel: str
    byText: str
    byRegex: str
    byOrder: _containers.RepeatedScalarFieldContainer[int]
    byPosition: _containers.RepeatedScalarFieldContainer[float]
    confidence: float
    image: str
    def __init__(self, user: _Optional[str] = ..., id: _Optional[str] = ..., event: _Optional[str] = ..., byLabel: _Optional[str] = ..., byText: _Optional[str] = ..., byRegex: _Optional[str] = ..., byOrder: _Optional[_Iterable[int]] = ..., byPosition: _Optional[_Iterable[float]] = ..., confidence: _Optional[float] = ..., image: _Optional[str] = ...) -> None: ...

class UpdateRecordActionResponse(_message.Message):
    __slots__ = ("status", "message", "action")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    action: _base_pb2.Serialized
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., action: _Optional[_Union[_base_pb2.Serialized, _Mapping]] = ...) -> None: ...

class CreateRecordActionRequest(_message.Message):
    __slots__ = ("user", "record", "event", "byLabel", "byText", "byRegex", "byOrder", "byPosition", "confidence", "image")
    USER_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    BYLABEL_FIELD_NUMBER: _ClassVar[int]
    BYTEXT_FIELD_NUMBER: _ClassVar[int]
    BYREGEX_FIELD_NUMBER: _ClassVar[int]
    BYORDER_FIELD_NUMBER: _ClassVar[int]
    BYPOSITION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    user: str
    record: str
    event: str
    byLabel: str
    byText: str
    byRegex: str
    byOrder: _containers.RepeatedScalarFieldContainer[int]
    byPosition: _containers.RepeatedScalarFieldContainer[float]
    confidence: float
    image: str
    def __init__(self, user: _Optional[str] = ..., record: _Optional[str] = ..., event: _Optional[str] = ..., byLabel: _Optional[str] = ..., byText: _Optional[str] = ..., byRegex: _Optional[str] = ..., byOrder: _Optional[_Iterable[int]] = ..., byPosition: _Optional[_Iterable[float]] = ..., confidence: _Optional[float] = ..., image: _Optional[str] = ...) -> None: ...

class CreateRecordActionResponse(_message.Message):
    __slots__ = ("status", "message", "action")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    action: _base_pb2.Serialized
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., action: _Optional[_Union[_base_pb2.Serialized, _Mapping]] = ...) -> None: ...

class RemoveRecordActionRequest(_message.Message):
    __slots__ = ("user", "id")
    USER_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    user: str
    id: str
    def __init__(self, user: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class RemoveRecordActionResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ...) -> None: ...

class LoadRecordActionByEventRequest(_message.Message):
    __slots__ = ("user", "event")
    USER_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    user: str
    event: str
    def __init__(self, user: _Optional[str] = ..., event: _Optional[str] = ...) -> None: ...

class LoadRecordActionByEventResponse(_message.Message):
    __slots__ = ("status", "message", "action")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    action: _base_pb2.Serialized
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., action: _Optional[_Union[_base_pb2.Serialized, _Mapping]] = ...) -> None: ...

class LoadRecordActionRequest(_message.Message):
    __slots__ = ("user", "id")
    USER_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    user: str
    id: str
    def __init__(self, user: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class LoadRecordActionResponse(_message.Message):
    __slots__ = ("status", "message", "action")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    action: _base_pb2.Serialized
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., action: _Optional[_Union[_base_pb2.Serialized, _Mapping]] = ...) -> None: ...

class ListRecordActionRequest(_message.Message):
    __slots__ = ("user", "record", "skip", "limit", "event", "search")
    USER_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    user: str
    record: str
    skip: int
    limit: int
    event: str
    search: str
    def __init__(self, user: _Optional[str] = ..., record: _Optional[str] = ..., skip: _Optional[int] = ..., limit: _Optional[int] = ..., event: _Optional[str] = ..., search: _Optional[str] = ...) -> None: ...

class ListRecordActionResponse(_message.Message):
    __slots__ = ("status", "message", "total", "actions")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    total: int
    actions: _containers.RepeatedCompositeFieldContainer[_base_pb2.Serialized]
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., total: _Optional[int] = ..., actions: _Optional[_Iterable[_Union[_base_pb2.Serialized, _Mapping]]] = ...) -> None: ...

class CountRecordActionRequest(_message.Message):
    __slots__ = ("user", "record", "event", "search")
    USER_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    user: str
    record: str
    event: str
    search: str
    def __init__(self, user: _Optional[str] = ..., record: _Optional[str] = ..., event: _Optional[str] = ..., search: _Optional[str] = ...) -> None: ...

class CountRecordActionResponse(_message.Message):
    __slots__ = ("status", "message", "total")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    total: int
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., total: _Optional[int] = ...) -> None: ...

class LoadEventRequest(_message.Message):
    __slots__ = ("user", "id")
    USER_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    user: str
    id: str
    def __init__(self, user: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class LoadEventResponse(_message.Message):
    __slots__ = ("status", "message", "event")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    event: _base_pb2.Serialized
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., event: _Optional[_Union[_base_pb2.Serialized, _Mapping]] = ...) -> None: ...

class SizeRecordVideoRequest(_message.Message):
    __slots__ = ("user", "record")
    USER_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    user: str
    record: str
    def __init__(self, user: _Optional[str] = ..., record: _Optional[str] = ...) -> None: ...

class SizeRecordVideoResponse(_message.Message):
    __slots__ = ("status", "message", "size")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    size: int
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., size: _Optional[int] = ...) -> None: ...

class StreamRangeRecordVideoRequest(_message.Message):
    __slots__ = ("user", "record", "start_byte", "end_byte")
    USER_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    START_BYTE_FIELD_NUMBER: _ClassVar[int]
    END_BYTE_FIELD_NUMBER: _ClassVar[int]
    user: str
    record: str
    start_byte: int
    end_byte: int
    def __init__(self, user: _Optional[str] = ..., record: _Optional[str] = ..., start_byte: _Optional[int] = ..., end_byte: _Optional[int] = ...) -> None: ...

class StreamRangeRecordVideoResponse(_message.Message):
    __slots__ = ("status", "message", "data")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    data: bytes
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class StreamRecordVideoRequest(_message.Message):
    __slots__ = ("user", "record")
    USER_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    user: str
    record: str
    def __init__(self, user: _Optional[str] = ..., record: _Optional[str] = ...) -> None: ...

class StreamRecordVideoResponse(_message.Message):
    __slots__ = ("status", "message", "data")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    data: bytes
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class SizeRecordRequest(_message.Message):
    __slots__ = ("user", "record")
    USER_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    user: str
    record: str
    def __init__(self, user: _Optional[str] = ..., record: _Optional[str] = ...) -> None: ...

class SizeRecordResponse(_message.Message):
    __slots__ = ("status", "message", "size")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    size: int
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., size: _Optional[int] = ...) -> None: ...

class LoadRecordFrameRequest(_message.Message):
    __slots__ = ("user", "record", "frame", "thumbnail")
    USER_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    user: str
    record: str
    frame: int
    thumbnail: bool
    def __init__(self, user: _Optional[str] = ..., record: _Optional[str] = ..., frame: _Optional[int] = ..., thumbnail: bool = ...) -> None: ...

class LoadRecordFrameResponse(_message.Message):
    __slots__ = ("status", "message", "frame")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    frame: bytes
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., frame: _Optional[bytes] = ...) -> None: ...

class LoadRecordFrameBase64Request(_message.Message):
    __slots__ = ("user", "record", "frame", "thumbnail")
    USER_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    user: str
    record: str
    frame: int
    thumbnail: bool
    def __init__(self, user: _Optional[str] = ..., record: _Optional[str] = ..., frame: _Optional[int] = ..., thumbnail: bool = ...) -> None: ...

class LoadRecordFrameBase64Response(_message.Message):
    __slots__ = ("status", "message", "frame")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FRAME_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    frame: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., frame: _Optional[str] = ...) -> None: ...

class CountRecordFrameRequest(_message.Message):
    __slots__ = ("user", "record")
    USER_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    user: str
    record: str
    def __init__(self, user: _Optional[str] = ..., record: _Optional[str] = ...) -> None: ...

class CountRecordFrameResponse(_message.Message):
    __slots__ = ("status", "message", "total")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    total: int
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., total: _Optional[int] = ...) -> None: ...

class ListRecordEventRequest(_message.Message):
    __slots__ = ("user", "record")
    USER_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    user: str
    record: str
    def __init__(self, user: _Optional[str] = ..., record: _Optional[str] = ...) -> None: ...

class ListRecordEventResponse(_message.Message):
    __slots__ = ("status", "message", "events")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    events: _containers.RepeatedCompositeFieldContainer[_base_pb2.Serialized]
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., events: _Optional[_Iterable[_Union[_base_pb2.Serialized, _Mapping]]] = ...) -> None: ...

class RunningRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RunningResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    def __init__(self, status: bool = ...) -> None: ...

class LoadRecordRequest(_message.Message):
    __slots__ = ("user", "id")
    USER_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    user: str
    id: str
    def __init__(self, user: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class LoadRecordResponse(_message.Message):
    __slots__ = ("status", "message", "record")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    record: _base_pb2.Serialized
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., record: _Optional[_Union[_base_pb2.Serialized, _Mapping]] = ...) -> None: ...

class UpdateRecordRequest(_message.Message):
    __slots__ = ("user", "id", "name", "description")
    USER_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    user: str
    id: str
    name: str
    description: str
    def __init__(self, user: _Optional[str] = ..., id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class UpdateRecordResponse(_message.Message):
    __slots__ = ("status", "message", "record")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    record: _base_pb2.Serialized
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., record: _Optional[_Union[_base_pb2.Serialized, _Mapping]] = ...) -> None: ...

class ListRecordRequest(_message.Message):
    __slots__ = ("user", "project", "skip", "limit", "search")
    USER_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    user: str
    project: str
    skip: int
    limit: int
    search: str
    def __init__(self, user: _Optional[str] = ..., project: _Optional[str] = ..., skip: _Optional[int] = ..., limit: _Optional[int] = ..., search: _Optional[str] = ...) -> None: ...

class ListRecordResponse(_message.Message):
    __slots__ = ("status", "message", "total", "records")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    total: int
    records: _containers.RepeatedCompositeFieldContainer[_base_pb2.Serialized]
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., total: _Optional[int] = ..., records: _Optional[_Iterable[_Union[_base_pb2.Serialized, _Mapping]]] = ...) -> None: ...

class CountRecordRequest(_message.Message):
    __slots__ = ("user", "project", "skip", "limit", "search")
    USER_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    user: str
    project: str
    skip: int
    limit: int
    search: str
    def __init__(self, user: _Optional[str] = ..., project: _Optional[str] = ..., skip: _Optional[int] = ..., limit: _Optional[int] = ..., search: _Optional[str] = ...) -> None: ...

class CountRecordResponse(_message.Message):
    __slots__ = ("status", "message", "total")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    total: int
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., total: _Optional[int] = ...) -> None: ...

class DeleteRecordRequest(_message.Message):
    __slots__ = ("user", "record")
    USER_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    user: str
    record: str
    def __init__(self, user: _Optional[str] = ..., record: _Optional[str] = ...) -> None: ...

class DeleteRecordResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ...) -> None: ...

class StartRecordRequest(_message.Message):
    __slots__ = ("user", "project", "name", "description")
    USER_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    user: str
    project: str
    name: str
    description: str
    def __init__(self, user: _Optional[str] = ..., project: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class StartRecordResponse(_message.Message):
    __slots__ = ("status", "message", "record")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    record: _base_pb2.Serialized
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., record: _Optional[_Union[_base_pb2.Serialized, _Mapping]] = ...) -> None: ...

class StopRecordRequest(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: str
    def __init__(self, user: _Optional[str] = ...) -> None: ...

class StopRecordResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ...) -> None: ...

class CountRecordEventRequest(_message.Message):
    __slots__ = ("user", "record")
    USER_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    user: str
    record: str
    def __init__(self, user: _Optional[str] = ..., record: _Optional[str] = ...) -> None: ...

class CountRecordEventResponse(_message.Message):
    __slots__ = ("status", "message", "total")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    total: int
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., total: _Optional[int] = ...) -> None: ...
