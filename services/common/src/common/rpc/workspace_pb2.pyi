from common.rpc import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateProjectRequest(_message.Message):
    __slots__ = ("user", "name", "description")
    USER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    user: str
    name: str
    description: str
    def __init__(self, user: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class CreateProjectResponse(_message.Message):
    __slots__ = ("status", "message", "project")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    project: _base_pb2.Serialized
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., project: _Optional[_Union[_base_pb2.Serialized, _Mapping]] = ...) -> None: ...

class LoadProjectRequest(_message.Message):
    __slots__ = ("user", "id")
    USER_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    user: str
    id: str
    def __init__(self, user: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class LoadProjectResponse(_message.Message):
    __slots__ = ("status", "message", "project")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    project: _base_pb2.Serialized
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., project: _Optional[_Union[_base_pb2.Serialized, _Mapping]] = ...) -> None: ...

class ListProjectRequest(_message.Message):
    __slots__ = ("user", "skip", "limit", "search")
    USER_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    user: str
    skip: int
    limit: int
    search: str
    def __init__(self, user: _Optional[str] = ..., skip: _Optional[int] = ..., limit: _Optional[int] = ..., search: _Optional[str] = ...) -> None: ...

class ListProjectResponse(_message.Message):
    __slots__ = ("status", "message", "total", "projects")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    PROJECTS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    total: int
    projects: _containers.RepeatedCompositeFieldContainer[_base_pb2.Serialized]
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., total: _Optional[int] = ..., projects: _Optional[_Iterable[_Union[_base_pb2.Serialized, _Mapping]]] = ...) -> None: ...

class UpdateProjectRequest(_message.Message):
    __slots__ = ("id", "user", "name", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    user: str
    name: str
    description: str
    def __init__(self, id: _Optional[str] = ..., user: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class UpdateProjectResponse(_message.Message):
    __slots__ = ("status", "message", "project")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    project: _base_pb2.Serialized
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., project: _Optional[_Union[_base_pb2.Serialized, _Mapping]] = ...) -> None: ...

class DeleteProjectRequest(_message.Message):
    __slots__ = ("user", "id")
    USER_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    user: str
    id: str
    def __init__(self, user: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class DeleteProjectResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ...) -> None: ...
