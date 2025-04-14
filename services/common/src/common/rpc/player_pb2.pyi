from common.rpc import base_pb2 as _base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerScriptUpdateRequest(_message.Message):
    __slots__ = ("user", "record", "script")
    USER_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    user: str
    record: str
    script: str
    def __init__(self, user: _Optional[str] = ..., record: _Optional[str] = ..., script: _Optional[str] = ...) -> None: ...

class PlayerScriptUpdateResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ...) -> None: ...

class PlayerRawScriptExecuteRequest(_message.Message):
    __slots__ = ("user", "script", "session")
    USER_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    user: str
    script: str
    session: str
    def __init__(self, user: _Optional[str] = ..., script: _Optional[str] = ..., session: _Optional[str] = ...) -> None: ...

class PlayerRawScriptExecuteResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ...) -> None: ...

class PlayerScriptExecuteRequest(_message.Message):
    __slots__ = ("user", "record", "session")
    USER_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    user: str
    record: str
    session: str
    def __init__(self, user: _Optional[str] = ..., record: _Optional[str] = ..., session: _Optional[str] = ...) -> None: ...

class PlayerScriptExecuteResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ...) -> None: ...

class PlayerScriptExistRequest(_message.Message):
    __slots__ = ("user", "record")
    USER_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    user: str
    record: str
    def __init__(self, user: _Optional[str] = ..., record: _Optional[str] = ...) -> None: ...

class PlayerScriptExistResponse(_message.Message):
    __slots__ = ("status", "message", "found")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FOUND_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    found: bool
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., found: bool = ...) -> None: ...

class PlayerScriptLoadRequest(_message.Message):
    __slots__ = ("user", "record")
    USER_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    user: str
    record: str
    def __init__(self, user: _Optional[str] = ..., record: _Optional[str] = ...) -> None: ...

class PlayerScriptLoadResponse(_message.Message):
    __slots__ = ("status", "message", "script")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    script: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., script: _Optional[str] = ...) -> None: ...

class PlayerScriptGenerateRequest(_message.Message):
    __slots__ = ("user", "record", "declarative", "synthetic")
    USER_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    DECLARATIVE_FIELD_NUMBER: _ClassVar[int]
    SYNTHETIC_FIELD_NUMBER: _ClassVar[int]
    user: str
    record: str
    declarative: bool
    synthetic: bool
    def __init__(self, user: _Optional[str] = ..., record: _Optional[str] = ..., declarative: bool = ..., synthetic: bool = ...) -> None: ...

class PlayerScriptGenerateResponse(_message.Message):
    __slots__ = ("status", "message", "script")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    script: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., script: _Optional[str] = ...) -> None: ...
