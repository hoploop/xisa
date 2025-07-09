from common.rpc import base_pb2 as _base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NannyUpdateRequest(_message.Message):
    __slots__ = ("service", "status")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    service: str
    status: bool
    def __init__(self, service: _Optional[str] = ..., status: bool = ...) -> None: ...

class NannyUpdateResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    def __init__(self, status: bool = ...) -> None: ...

class UpdateSessionRequest(_message.Message):
    __slots__ = ("session", "document")
    SESSION_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    session: str
    document: _base_pb2.Serialized
    def __init__(self, session: _Optional[str] = ..., document: _Optional[_Union[_base_pb2.Serialized, _Mapping]] = ...) -> None: ...

class UpdateSessionResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ...) -> None: ...
