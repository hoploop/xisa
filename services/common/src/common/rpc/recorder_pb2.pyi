from common.rpc import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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
