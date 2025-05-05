from common.rpc import base_pb2 as _base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Question(_message.Message):
    __slots__ = ("user", "session", "message")
    USER_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    user: str
    session: str
    message: str
    def __init__(self, user: _Optional[str] = ..., session: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class Answer(_message.Message):
    __slots__ = ("status", "message", "text")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    text: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...
