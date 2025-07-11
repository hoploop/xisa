from common.rpc import base_pb2 as _base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StorageExistsRequest(_message.Message):
    __slots__ = ("filename", "folder")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FOLDER_FIELD_NUMBER: _ClassVar[int]
    filename: str
    folder: str
    def __init__(self, filename: _Optional[str] = ..., folder: _Optional[str] = ...) -> None: ...

class StorageExistsResponse(_message.Message):
    __slots__ = ("status", "message", "exists")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EXISTS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    exists: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., exists: _Optional[str] = ...) -> None: ...

class StorageSaveRequest(_message.Message):
    __slots__ = ("filename", "folder", "data", "content_type")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FOLDER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    filename: str
    folder: str
    data: bytes
    content_type: str
    def __init__(self, filename: _Optional[str] = ..., folder: _Optional[str] = ..., data: _Optional[bytes] = ..., content_type: _Optional[str] = ...) -> None: ...

class StorageSaveResponse(_message.Message):
    __slots__ = ("status", "message", "id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    id: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class StorageLoadByIdRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class StorageLoadByIdResponse(_message.Message):
    __slots__ = ("status", "message", "data", "content_type", "size")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    data: bytes
    content_type: str
    size: int
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., data: _Optional[bytes] = ..., content_type: _Optional[str] = ..., size: _Optional[int] = ...) -> None: ...

class StorageLoadRequest(_message.Message):
    __slots__ = ("filename", "folder")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FOLDER_FIELD_NUMBER: _ClassVar[int]
    filename: str
    folder: str
    def __init__(self, filename: _Optional[str] = ..., folder: _Optional[str] = ...) -> None: ...

class StorageLoadResponse(_message.Message):
    __slots__ = ("status", "message", "data", "content_type", "size")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    data: bytes
    content_type: str
    size: int
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., data: _Optional[bytes] = ..., content_type: _Optional[str] = ..., size: _Optional[int] = ...) -> None: ...

class StorageRemoveRequest(_message.Message):
    __slots__ = ("filename", "folder")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FOLDER_FIELD_NUMBER: _ClassVar[int]
    filename: str
    folder: str
    def __init__(self, filename: _Optional[str] = ..., folder: _Optional[str] = ...) -> None: ...

class StorageRemoveResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ...) -> None: ...

class StorageRemoveFolderRequest(_message.Message):
    __slots__ = ("folder",)
    FOLDER_FIELD_NUMBER: _ClassVar[int]
    folder: str
    def __init__(self, folder: _Optional[str] = ...) -> None: ...

class StorageRemoveFolderResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ...) -> None: ...
