from common.rpc import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LanguageEncodeRequest(_message.Message):
    __slots__ = ("user", "text")
    USER_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    user: str
    text: str
    def __init__(self, user: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...

class LanguageEncodeResponse(_message.Message):
    __slots__ = ("status", "message", "tokens")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    tokens: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., tokens: _Optional[_Iterable[int]] = ...) -> None: ...

class LanguageDecodeRequest(_message.Message):
    __slots__ = ("user", "tokens")
    USER_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    user: str
    tokens: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, user: _Optional[str] = ..., tokens: _Optional[_Iterable[int]] = ...) -> None: ...

class LanguageDecodeResponse(_message.Message):
    __slots__ = ("status", "message", "text")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    text: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...
