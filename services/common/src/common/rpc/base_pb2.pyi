from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Ping(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    def __init__(self, status: bool = ...) -> None: ...

class Pong(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    def __init__(self, status: bool = ...) -> None: ...

class Serialized(_message.Message):
    __slots__ = ("signature", "data")
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    signature: str
    data: str
    def __init__(self, signature: _Optional[str] = ..., data: _Optional[str] = ...) -> None: ...

class Step(_message.Message):
    __slots__ = ("order", "scenario", "event", "byClass", "byText", "byOrder", "duration", "retry")
    ORDER_FIELD_NUMBER: _ClassVar[int]
    SCENARIO_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    BYCLASS_FIELD_NUMBER: _ClassVar[int]
    BYTEXT_FIELD_NUMBER: _ClassVar[int]
    BYORDER_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    RETRY_FIELD_NUMBER: _ClassVar[int]
    order: int
    scenario: str
    event: str
    byClass: _containers.RepeatedScalarFieldContainer[str]
    byText: _containers.RepeatedScalarFieldContainer[str]
    byOrder: _containers.RepeatedScalarFieldContainer[int]
    duration: float
    retry: int
    def __init__(self, order: _Optional[int] = ..., scenario: _Optional[str] = ..., event: _Optional[str] = ..., byClass: _Optional[_Iterable[str]] = ..., byText: _Optional[_Iterable[str]] = ..., byOrder: _Optional[_Iterable[int]] = ..., duration: _Optional[float] = ..., retry: _Optional[int] = ...) -> None: ...
