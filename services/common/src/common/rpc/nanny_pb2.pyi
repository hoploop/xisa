from common.rpc import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NannyStatusRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NannyServiceStatus(_message.Message):
    __slots__ = ("name", "status")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    status: bool
    def __init__(self, name: _Optional[str] = ..., status: bool = ...) -> None: ...

class NannyStatusResponse(_message.Message):
    __slots__ = ("services",)
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    services: _containers.RepeatedCompositeFieldContainer[NannyServiceStatus]
    def __init__(self, services: _Optional[_Iterable[_Union[NannyServiceStatus, _Mapping]]] = ...) -> None: ...
