from common.rpc import base_pb2 as _base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserRequest(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class UserResponse(_message.Message):
    __slots__ = ("status", "message", "user")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    user: _base_pb2.Serialized
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., user: _Optional[_Union[_base_pb2.Serialized, _Mapping]] = ...) -> None: ...

class CheckRequest(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class CheckResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ...) -> None: ...

class LoginRequest(_message.Message):
    __slots__ = ("username", "password", "host")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    host: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ..., host: _Optional[str] = ...) -> None: ...

class LoginResponse(_message.Message):
    __slots__ = ("status", "message", "token")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    token: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class LogoutRequest(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class LogoutResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ...) -> None: ...

class RegisterRequest(_message.Message):
    __slots__ = ("username", "password", "email")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    email: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class RegisterResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ...) -> None: ...

class UnregisterRequest(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class UnregisterResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ...) -> None: ...

class ResetPasswordRequest(_message.Message):
    __slots__ = ("token", "host", "old", "new")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    OLD_FIELD_NUMBER: _ClassVar[int]
    NEW_FIELD_NUMBER: _ClassVar[int]
    token: str
    host: str
    old: str
    new: str
    def __init__(self, token: _Optional[str] = ..., host: _Optional[str] = ..., old: _Optional[str] = ..., new: _Optional[str] = ...) -> None: ...

class ResetPasswordResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ...) -> None: ...
