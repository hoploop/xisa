from common.rpc import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DetectorImageMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRAIN: _ClassVar[DetectorImageMode]
    VAL: _ClassVar[DetectorImageMode]
    TEST: _ClassVar[DetectorImageMode]
TRAIN: DetectorImageMode
VAL: DetectorImageMode
TEST: DetectorImageMode

class CountDetectorImageLabelRequest(_message.Message):
    __slots__ = ("user", "image")
    USER_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    user: str
    image: str
    def __init__(self, user: _Optional[str] = ..., image: _Optional[str] = ...) -> None: ...

class CountDetectorImageLabelResponse(_message.Message):
    __slots__ = ("status", "message", "total")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    total: int
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., total: _Optional[int] = ...) -> None: ...

class RemoveDetectorImageLabelRequest(_message.Message):
    __slots__ = ("user", "label")
    USER_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    user: str
    label: str
    def __init__(self, user: _Optional[str] = ..., label: _Optional[str] = ...) -> None: ...

class RemoveDetectorImageLabelResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ...) -> None: ...

class CountDetectorClassRequest(_message.Message):
    __slots__ = ("user", "detector")
    USER_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_FIELD_NUMBER: _ClassVar[int]
    user: str
    detector: str
    def __init__(self, user: _Optional[str] = ..., detector: _Optional[str] = ...) -> None: ...

class CountDetectorClassResponse(_message.Message):
    __slots__ = ("status", "message", "total")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    total: int
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., total: _Optional[int] = ...) -> None: ...

class ListDetectorClassRequest(_message.Message):
    __slots__ = ("user", "detector", "skip", "limit", "search")
    USER_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    user: str
    detector: str
    skip: int
    limit: int
    search: str
    def __init__(self, user: _Optional[str] = ..., detector: _Optional[str] = ..., skip: _Optional[int] = ..., limit: _Optional[int] = ..., search: _Optional[str] = ...) -> None: ...

class ListDetectorClassResponse(_message.Message):
    __slots__ = ("status", "message", "total", "classes")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    CLASSES_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    total: int
    classes: _containers.RepeatedCompositeFieldContainer[_base_pb2.Serialized]
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., total: _Optional[int] = ..., classes: _Optional[_Iterable[_Union[_base_pb2.Serialized, _Mapping]]] = ...) -> None: ...

class ListDetectorImageLabelRequest(_message.Message):
    __slots__ = ("user", "image", "skip", "limit", "search")
    USER_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    user: str
    image: str
    skip: int
    limit: int
    search: str
    def __init__(self, user: _Optional[str] = ..., image: _Optional[str] = ..., skip: _Optional[int] = ..., limit: _Optional[int] = ..., search: _Optional[str] = ...) -> None: ...

class ListDetectorImageLabelResponse(_message.Message):
    __slots__ = ("status", "message", "total", "labels")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    total: int
    labels: _containers.RepeatedCompositeFieldContainer[_base_pb2.Serialized]
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., total: _Optional[int] = ..., labels: _Optional[_Iterable[_Union[_base_pb2.Serialized, _Mapping]]] = ...) -> None: ...

class UploadDetectorImageRequest(_message.Message):
    __slots__ = ("user", "detector", "data", "modes")
    USER_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MODES_FIELD_NUMBER: _ClassVar[int]
    user: str
    detector: str
    data: str
    modes: _containers.RepeatedScalarFieldContainer[DetectorImageMode]
    def __init__(self, user: _Optional[str] = ..., detector: _Optional[str] = ..., data: _Optional[str] = ..., modes: _Optional[_Iterable[_Union[DetectorImageMode, str]]] = ...) -> None: ...

class UploadDetectorImageResponse(_message.Message):
    __slots__ = ("status", "message", "images")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    images: _containers.RepeatedCompositeFieldContainer[_base_pb2.Serialized]
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., images: _Optional[_Iterable[_Union[_base_pb2.Serialized, _Mapping]]] = ...) -> None: ...

class AddDetectorImageLabelRequest(_message.Message):
    __slots__ = ("user", "image", "xstart", "xend", "ystart", "yend", "classes")
    USER_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    XSTART_FIELD_NUMBER: _ClassVar[int]
    XEND_FIELD_NUMBER: _ClassVar[int]
    YSTART_FIELD_NUMBER: _ClassVar[int]
    YEND_FIELD_NUMBER: _ClassVar[int]
    CLASSES_FIELD_NUMBER: _ClassVar[int]
    user: str
    image: str
    xstart: float
    xend: float
    ystart: float
    yend: float
    classes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user: _Optional[str] = ..., image: _Optional[str] = ..., xstart: _Optional[float] = ..., xend: _Optional[float] = ..., ystart: _Optional[float] = ..., yend: _Optional[float] = ..., classes: _Optional[_Iterable[str]] = ...) -> None: ...

class AddDetectorImageLabelResponse(_message.Message):
    __slots__ = ("status", "message", "label")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    label: _base_pb2.Serialized
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., label: _Optional[_Union[_base_pb2.Serialized, _Mapping]] = ...) -> None: ...

class RemoveDetectorRequest(_message.Message):
    __slots__ = ("user", "id")
    USER_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    user: str
    id: str
    def __init__(self, user: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class RemoveDetectorResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ...) -> None: ...

class RemoveDetectorImageRequest(_message.Message):
    __slots__ = ("user", "id")
    USER_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    user: str
    id: str
    def __init__(self, user: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class RemoveDetectorImageResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ...) -> None: ...

class CountDetectorImageRequest(_message.Message):
    __slots__ = ("user", "detector", "skip", "limit")
    USER_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    user: str
    detector: str
    skip: int
    limit: int
    def __init__(self, user: _Optional[str] = ..., detector: _Optional[str] = ..., skip: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class CountDetectorImageResponse(_message.Message):
    __slots__ = ("status", "message", "total")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    total: int
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., total: _Optional[int] = ...) -> None: ...

class ListDetectorImageRequest(_message.Message):
    __slots__ = ("user", "detector", "skip", "limit")
    USER_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    user: str
    detector: str
    skip: int
    limit: int
    def __init__(self, user: _Optional[str] = ..., detector: _Optional[str] = ..., skip: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class ListDetectorImageResponse(_message.Message):
    __slots__ = ("status", "message", "total", "images")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    total: int
    images: _containers.RepeatedCompositeFieldContainer[_base_pb2.Serialized]
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., total: _Optional[int] = ..., images: _Optional[_Iterable[_Union[_base_pb2.Serialized, _Mapping]]] = ...) -> None: ...

class TrainDetectorRequest(_message.Message):
    __slots__ = ("user", "session", "detector", "epochs", "imageSize")
    USER_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_FIELD_NUMBER: _ClassVar[int]
    EPOCHS_FIELD_NUMBER: _ClassVar[int]
    IMAGESIZE_FIELD_NUMBER: _ClassVar[int]
    user: str
    session: str
    detector: str
    epochs: int
    imageSize: int
    def __init__(self, user: _Optional[str] = ..., session: _Optional[str] = ..., detector: _Optional[str] = ..., epochs: _Optional[int] = ..., imageSize: _Optional[int] = ...) -> None: ...

class TrainDetectorResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ...) -> None: ...

class CreateDetectorRequest(_message.Message):
    __slots__ = ("user", "project", "name", "description", "origin")
    USER_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    user: str
    project: str
    name: str
    description: str
    origin: str
    def __init__(self, user: _Optional[str] = ..., project: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., origin: _Optional[str] = ...) -> None: ...

class CreateDetectorResponse(_message.Message):
    __slots__ = ("status", "message", "detector")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    detector: _base_pb2.Serialized
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., detector: _Optional[_Union[_base_pb2.Serialized, _Mapping]] = ...) -> None: ...

class LoadDetectorRequest(_message.Message):
    __slots__ = ("user", "id")
    USER_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    user: str
    id: str
    def __init__(self, user: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class LoadDetectorResponse(_message.Message):
    __slots__ = ("status", "message", "detector")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    detector: _base_pb2.Serialized
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., detector: _Optional[_Union[_base_pb2.Serialized, _Mapping]] = ...) -> None: ...

class UpdateDetectorRequest(_message.Message):
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

class UpdateDetectorResponse(_message.Message):
    __slots__ = ("status", "message", "detector")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    detector: _base_pb2.Serialized
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., detector: _Optional[_Union[_base_pb2.Serialized, _Mapping]] = ...) -> None: ...

class CountDetectorRequest(_message.Message):
    __slots__ = ("user", "project")
    USER_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    user: str
    project: str
    def __init__(self, user: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class CountDetectorResponse(_message.Message):
    __slots__ = ("status", "message", "total")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    total: int
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., total: _Optional[int] = ...) -> None: ...

class ListDetectorRequest(_message.Message):
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

class ListDetectorResponse(_message.Message):
    __slots__ = ("status", "message", "total", "detectors")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    DETECTORS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    total: int
    detectors: _containers.RepeatedCompositeFieldContainer[_base_pb2.Serialized]
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., total: _Optional[int] = ..., detectors: _Optional[_Iterable[_Union[_base_pb2.Serialized, _Mapping]]] = ...) -> None: ...
