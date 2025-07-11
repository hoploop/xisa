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

class DetectorImageRequest(_message.Message):
    __slots__ = ("user", "id")
    USER_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    user: str
    id: str
    def __init__(self, user: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class DetectorImageResponse(_message.Message):
    __slots__ = ("data", "content_type", "found")
    DATA_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FOUND_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    content_type: str
    found: bool
    def __init__(self, data: _Optional[bytes] = ..., content_type: _Optional[str] = ..., found: bool = ...) -> None: ...

class TrainResultRequest(_message.Message):
    __slots__ = ("user", "filename")
    USER_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    user: str
    filename: str
    def __init__(self, user: _Optional[str] = ..., filename: _Optional[str] = ...) -> None: ...

class TrainResultResponse(_message.Message):
    __slots__ = ("data", "content_type", "found")
    DATA_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FOUND_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    content_type: str
    found: bool
    def __init__(self, data: _Optional[bytes] = ..., content_type: _Optional[str] = ..., found: bool = ...) -> None: ...

class LoadDetectorLabelRequest(_message.Message):
    __slots__ = ("user", "id")
    USER_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    user: str
    id: str
    def __init__(self, user: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class LoadDetectorLabelResponse(_message.Message):
    __slots__ = ("status", "message", "label")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    label: _base_pb2.Serialized
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., label: _Optional[_Union[_base_pb2.Serialized, _Mapping]] = ...) -> None: ...

class CanRemoveDetectorLabelRequest(_message.Message):
    __slots__ = ("user", "id")
    USER_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    user: str
    id: str
    def __init__(self, user: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class CanRemoveDetectorLabelResponse(_message.Message):
    __slots__ = ("status", "message", "result")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    result: bool
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., result: bool = ...) -> None: ...

class RemoveDetectorLabelRequest(_message.Message):
    __slots__ = ("user", "id")
    USER_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    user: str
    id: str
    def __init__(self, user: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class RemoveDetectorLabelResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ...) -> None: ...

class FindDetectorImageLabelRequest(_message.Message):
    __slots__ = ("user", "detector", "name")
    USER_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    user: str
    detector: str
    name: str
    def __init__(self, user: _Optional[str] = ..., detector: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class FindDetectorImageLabelResponse(_message.Message):
    __slots__ = ("status", "message", "label")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    label: _base_pb2.Serialized
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., label: _Optional[_Union[_base_pb2.Serialized, _Mapping]] = ...) -> None: ...

class SuggestStepRequest(_message.Message):
    __slots__ = ("user", "data", "event", "detector", "confidence")
    USER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    user: str
    data: str
    event: str
    detector: str
    confidence: float
    def __init__(self, user: _Optional[str] = ..., data: _Optional[str] = ..., event: _Optional[str] = ..., detector: _Optional[str] = ..., confidence: _Optional[float] = ...) -> None: ...

class SuggestStepResponse(_message.Message):
    __slots__ = ("status", "message", "suggestions")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    suggestions: _containers.RepeatedCompositeFieldContainer[_base_pb2.Serialized]
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., suggestions: _Optional[_Iterable[_Union[_base_pb2.Serialized, _Mapping]]] = ...) -> None: ...

class AddDetectorLabelRequest(_message.Message):
    __slots__ = ("user", "detector", "name")
    USER_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    user: str
    detector: str
    name: str
    def __init__(self, user: _Optional[str] = ..., detector: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AddDetectorLabelResponse(_message.Message):
    __slots__ = ("status", "message", "label")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    label: _base_pb2.Serialized
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., label: _Optional[_Union[_base_pb2.Serialized, _Mapping]] = ...) -> None: ...

class ExistsDetectorLabelRequest(_message.Message):
    __slots__ = ("user", "detector", "name")
    USER_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    user: str
    detector: str
    name: str
    def __init__(self, user: _Optional[str] = ..., detector: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ExistsDetectorLabelResponse(_message.Message):
    __slots__ = ("status", "message", "label")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    label: _base_pb2.Serialized
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., label: _Optional[_Union[_base_pb2.Serialized, _Mapping]] = ...) -> None: ...

class DetectText(_message.Message):
    __slots__ = ("x", "y", "w", "h", "page", "block", "par", "line", "word", "value", "confidence")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    H_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    PAR_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    WORD_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    w: float
    h: float
    page: int
    block: int
    par: int
    line: int
    word: int
    value: str
    confidence: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., w: _Optional[float] = ..., h: _Optional[float] = ..., page: _Optional[int] = ..., block: _Optional[int] = ..., par: _Optional[int] = ..., line: _Optional[int] = ..., word: _Optional[int] = ..., value: _Optional[str] = ..., confidence: _Optional[float] = ...) -> None: ...

class DetectTextsRequest(_message.Message):
    __slots__ = ("user", "data", "confidence")
    USER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    user: str
    data: str
    confidence: float
    def __init__(self, user: _Optional[str] = ..., data: _Optional[str] = ..., confidence: _Optional[float] = ...) -> None: ...

class DetectTextsResponse(_message.Message):
    __slots__ = ("status", "message", "texts")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TEXTS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    texts: _containers.RepeatedCompositeFieldContainer[DetectText]
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., texts: _Optional[_Iterable[_Union[DetectText, _Mapping]]] = ...) -> None: ...

class DetectObject(_message.Message):
    __slots__ = ("x", "y", "w", "h", "confidence", "name", "code", "row", "col")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    W_FIELD_NUMBER: _ClassVar[int]
    H_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    ROW_FIELD_NUMBER: _ClassVar[int]
    COL_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    w: float
    h: float
    confidence: float
    name: str
    code: int
    row: int
    col: int
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., w: _Optional[float] = ..., h: _Optional[float] = ..., confidence: _Optional[float] = ..., name: _Optional[str] = ..., code: _Optional[int] = ..., row: _Optional[int] = ..., col: _Optional[int] = ...) -> None: ...

class DetectObjectsRequest(_message.Message):
    __slots__ = ("user", "data", "detector", "confidence")
    USER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    user: str
    data: str
    detector: str
    confidence: float
    def __init__(self, user: _Optional[str] = ..., data: _Optional[str] = ..., detector: _Optional[str] = ..., confidence: _Optional[float] = ...) -> None: ...

class DetectObjectsResponse(_message.Message):
    __slots__ = ("status", "message", "objects")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    objects: _containers.RepeatedCompositeFieldContainer[DetectObject]
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., objects: _Optional[_Iterable[_Union[DetectObject, _Mapping]]] = ...) -> None: ...

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

class CountDetectorLabelRequest(_message.Message):
    __slots__ = ("user", "detector")
    USER_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_FIELD_NUMBER: _ClassVar[int]
    user: str
    detector: str
    def __init__(self, user: _Optional[str] = ..., detector: _Optional[str] = ...) -> None: ...

class CountDetectorLabelResponse(_message.Message):
    __slots__ = ("status", "message", "total")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    total: int
    def __init__(self, status: bool = ..., message: _Optional[str] = ..., total: _Optional[int] = ...) -> None: ...

class ListDetectorLabelRequest(_message.Message):
    __slots__ = ("user", "detector", "skip", "limit", "search", "exclude")
    USER_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_FIELD_NUMBER: _ClassVar[int]
    user: str
    detector: str
    skip: int
    limit: int
    search: str
    exclude: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user: _Optional[str] = ..., detector: _Optional[str] = ..., skip: _Optional[int] = ..., limit: _Optional[int] = ..., search: _Optional[str] = ..., exclude: _Optional[_Iterable[str]] = ...) -> None: ...

class ListDetectorLabelResponse(_message.Message):
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
    __slots__ = ("user", "detector", "file", "modes")
    USER_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    MODES_FIELD_NUMBER: _ClassVar[int]
    user: str
    detector: str
    file: str
    modes: _containers.RepeatedScalarFieldContainer[DetectorImageMode]
    def __init__(self, user: _Optional[str] = ..., detector: _Optional[str] = ..., file: _Optional[str] = ..., modes: _Optional[_Iterable[_Union[DetectorImageMode, str]]] = ...) -> None: ...

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
    __slots__ = ("user", "image", "xstart", "xend", "ystart", "yend", "label")
    USER_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    XSTART_FIELD_NUMBER: _ClassVar[int]
    XEND_FIELD_NUMBER: _ClassVar[int]
    YSTART_FIELD_NUMBER: _ClassVar[int]
    YEND_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    user: str
    image: str
    xstart: float
    xend: float
    ystart: float
    yend: float
    label: str
    def __init__(self, user: _Optional[str] = ..., image: _Optional[str] = ..., xstart: _Optional[float] = ..., xend: _Optional[float] = ..., ystart: _Optional[float] = ..., yend: _Optional[float] = ..., label: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("user", "detector")
    USER_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_FIELD_NUMBER: _ClassVar[int]
    user: str
    detector: str
    def __init__(self, user: _Optional[str] = ..., detector: _Optional[str] = ...) -> None: ...

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
