# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: common/rpc/trainer.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'common/rpc/trainer.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.rpc import base_pb2 as common_dot_rpc_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x63ommon/rpc/trainer.proto\x1a\x15\x63ommon/rpc/base.proto\"C\n!TrainImageObjectToDetectorRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x10\n\x08\x64\x65tector\x18\x02 \x01(\t\"e\n\"TrainImageObjectToDetectorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\r\n\x05total\x18\x03 \x01(\x05\x42\n\n\x08_message\"9\n\x1dTrainImageObjectRemoveRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\"R\n\x1eTrainImageObjectRemoveResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_message\"\xaf\x01\n\x1dTrainImageObjectUpdateRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0e\n\x06labels\x18\x02 \x03(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\r\n\x05train\x18\x04 \x01(\x08\x12\x0c\n\x04test\x18\x05 \x01(\x08\x12\x0b\n\x03val\x18\x06 \x01(\x08\x12\x0e\n\x06xstart\x18\x07 \x01(\x02\x12\x0c\n\x04xend\x18\x08 \x01(\x02\x12\x0e\n\x06ystart\x18\t \x01(\x02\x12\x0c\n\x04yend\x18\n \x01(\x02\"R\n\x1eTrainImageObjectUpdateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_message\"\xbc\x01\n\x17TrainImageObjectRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0e\n\x06lesson\x18\x02 \x01(\t\x12\r\n\x05\x66rame\x18\x03 \x01(\x05\x12\x0e\n\x06labels\x18\x04 \x03(\t\x12\x0e\n\x06xstart\x18\x05 \x01(\x02\x12\x0c\n\x04xend\x18\x06 \x01(\x02\x12\x0e\n\x06ystart\x18\x07 \x01(\x02\x12\x0c\n\x04yend\x18\x08 \x01(\x02\x12\r\n\x05train\x18\t \x01(\x08\x12\x0c\n\x04test\x18\n \x01(\x08\x12\x0b\n\x03val\x18\x0b \x01(\x08\"i\n\x18TrainImageObjectResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1b\n\x06object\x18\x03 \x01(\x0b\x32\x0b.SerializedB\n\n\x08_message\"R\n\x1eLessonSetTextConfidenceRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0e\n\x06lesson\x18\x02 \x01(\t\x12\x12\n\nconfidence\x18\x03 \x01(\x02\"p\n\x1fLessonSetTextConfidenceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1b\n\x06lesson\x18\x03 \x01(\x0b\x32\x0b.SerializedB\n\n\x08_message\"T\n LessonSetObjectConfidenceRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0e\n\x06lesson\x18\x02 \x01(\t\x12\x12\n\nconfidence\x18\x03 \x01(\x02\"r\n!LessonSetObjectConfidenceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1b\n\x06lesson\x18\x03 \x01(\x0b\x32\x0b.SerializedB\n\n\x08_message\"J\n\x18LessonSetDetectorRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x10\n\x08\x64\x65tector\x18\x02 \x01(\t\x12\x0e\n\x06lesson\x18\x03 \x01(\t\"j\n\x19LessonSetDetectorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1b\n\x06lesson\x18\x03 \x01(\x0b\x32\x0b.SerializedB\n\n\x08_message\"6\n\x16RecordHasLessonRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0e\n\x06record\x18\x02 \x01(\t\"x\n\x17RecordHasLessonResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12 \n\x06lesson\x18\x03 \x01(\x0b\x32\x0b.SerializedH\x01\x88\x01\x01\x42\n\n\x08_messageB\t\n\x07_lesson\"9\n\x19RecordCreateLessonRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0e\n\x06record\x18\x02 \x01(\t\"k\n\x1aRecordCreateLessonResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1b\n\x06lesson\x18\x03 \x01(\x0b\x32\x0b.SerializedB\n\n\x08_message\"Y\n\x1bTrainImageObjectListRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0e\n\x06lesson\x18\x02 \x01(\t\x12\x12\n\x05\x66rame\x18\x03 \x01(\x05H\x00\x88\x01\x01\x42\x08\n\x06_frame\"}\n\x1cTrainImageObjectListResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x1c\n\x07objects\x18\x04 \x03(\x0b\x32\x0b.SerializedB\n\n\x08_message\"H\n&TrainImageObjectCountByDetectorRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x10\n\x08\x64\x65tector\x18\x02 \x01(\t\"j\n\'TrainImageObjectCountByDetectorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\r\n\x05total\x18\x03 \x01(\x05\x42\n\n\x08_message2\xf3\x07\n\x07Trainer\x12\x14\n\x04ping\x12\x05.Ping\x1a\x05.Pong\x12\x44\n\x0frecordHasLesson\x12\x17.RecordHasLessonRequest\x1a\x18.RecordHasLessonResponse\x12M\n\x12recordCreateLesson\x12\x1a.RecordCreateLessonRequest\x1a\x1b.RecordCreateLessonResponse\x12\\\n\x17lessonSetTextConfidence\x12\x1f.LessonSetTextConfidenceRequest\x1a .LessonSetTextConfidenceResponse\x12\x62\n\x19lessonSetObjectConfidence\x12!.LessonSetObjectConfidenceRequest\x1a\".LessonSetObjectConfidenceResponse\x12J\n\x11lessonSetDetector\x12\x19.LessonSetDetectorRequest\x1a\x1a.LessonSetDetectorResponse\x12Y\n\x16trainImageObjectUpdate\x12\x1e.TrainImageObjectUpdateRequest\x1a\x1f.TrainImageObjectUpdateResponse\x12G\n\x10trainImageObject\x12\x18.TrainImageObjectRequest\x1a\x19.TrainImageObjectResponse\x12S\n\x14trainImageObjectList\x12\x1c.TrainImageObjectListRequest\x1a\x1d.TrainImageObjectListResponse\x12t\n\x1ftrainImageObjectCountByDetector\x12\'.TrainImageObjectCountByDetectorRequest\x1a(.TrainImageObjectCountByDetectorResponse\x12Y\n\x16trainImageObjectRemove\x12\x1e.TrainImageObjectRemoveRequest\x1a\x1f.TrainImageObjectRemoveResponse\x12\x65\n\x1atrainImageObjectToDetector\x12\".TrainImageObjectToDetectorRequest\x1a#.TrainImageObjectToDetectorResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.rpc.trainer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TRAINIMAGEOBJECTTODETECTORREQUEST']._serialized_start=51
  _globals['_TRAINIMAGEOBJECTTODETECTORREQUEST']._serialized_end=118
  _globals['_TRAINIMAGEOBJECTTODETECTORRESPONSE']._serialized_start=120
  _globals['_TRAINIMAGEOBJECTTODETECTORRESPONSE']._serialized_end=221
  _globals['_TRAINIMAGEOBJECTREMOVEREQUEST']._serialized_start=223
  _globals['_TRAINIMAGEOBJECTREMOVEREQUEST']._serialized_end=280
  _globals['_TRAINIMAGEOBJECTREMOVERESPONSE']._serialized_start=282
  _globals['_TRAINIMAGEOBJECTREMOVERESPONSE']._serialized_end=364
  _globals['_TRAINIMAGEOBJECTUPDATEREQUEST']._serialized_start=367
  _globals['_TRAINIMAGEOBJECTUPDATEREQUEST']._serialized_end=542
  _globals['_TRAINIMAGEOBJECTUPDATERESPONSE']._serialized_start=544
  _globals['_TRAINIMAGEOBJECTUPDATERESPONSE']._serialized_end=626
  _globals['_TRAINIMAGEOBJECTREQUEST']._serialized_start=629
  _globals['_TRAINIMAGEOBJECTREQUEST']._serialized_end=817
  _globals['_TRAINIMAGEOBJECTRESPONSE']._serialized_start=819
  _globals['_TRAINIMAGEOBJECTRESPONSE']._serialized_end=924
  _globals['_LESSONSETTEXTCONFIDENCEREQUEST']._serialized_start=926
  _globals['_LESSONSETTEXTCONFIDENCEREQUEST']._serialized_end=1008
  _globals['_LESSONSETTEXTCONFIDENCERESPONSE']._serialized_start=1010
  _globals['_LESSONSETTEXTCONFIDENCERESPONSE']._serialized_end=1122
  _globals['_LESSONSETOBJECTCONFIDENCEREQUEST']._serialized_start=1124
  _globals['_LESSONSETOBJECTCONFIDENCEREQUEST']._serialized_end=1208
  _globals['_LESSONSETOBJECTCONFIDENCERESPONSE']._serialized_start=1210
  _globals['_LESSONSETOBJECTCONFIDENCERESPONSE']._serialized_end=1324
  _globals['_LESSONSETDETECTORREQUEST']._serialized_start=1326
  _globals['_LESSONSETDETECTORREQUEST']._serialized_end=1400
  _globals['_LESSONSETDETECTORRESPONSE']._serialized_start=1402
  _globals['_LESSONSETDETECTORRESPONSE']._serialized_end=1508
  _globals['_RECORDHASLESSONREQUEST']._serialized_start=1510
  _globals['_RECORDHASLESSONREQUEST']._serialized_end=1564
  _globals['_RECORDHASLESSONRESPONSE']._serialized_start=1566
  _globals['_RECORDHASLESSONRESPONSE']._serialized_end=1686
  _globals['_RECORDCREATELESSONREQUEST']._serialized_start=1688
  _globals['_RECORDCREATELESSONREQUEST']._serialized_end=1745
  _globals['_RECORDCREATELESSONRESPONSE']._serialized_start=1747
  _globals['_RECORDCREATELESSONRESPONSE']._serialized_end=1854
  _globals['_TRAINIMAGEOBJECTLISTREQUEST']._serialized_start=1856
  _globals['_TRAINIMAGEOBJECTLISTREQUEST']._serialized_end=1945
  _globals['_TRAINIMAGEOBJECTLISTRESPONSE']._serialized_start=1947
  _globals['_TRAINIMAGEOBJECTLISTRESPONSE']._serialized_end=2072
  _globals['_TRAINIMAGEOBJECTCOUNTBYDETECTORREQUEST']._serialized_start=2074
  _globals['_TRAINIMAGEOBJECTCOUNTBYDETECTORREQUEST']._serialized_end=2146
  _globals['_TRAINIMAGEOBJECTCOUNTBYDETECTORRESPONSE']._serialized_start=2148
  _globals['_TRAINIMAGEOBJECTCOUNTBYDETECTORRESPONSE']._serialized_end=2254
  _globals['_TRAINER']._serialized_start=2257
  _globals['_TRAINER']._serialized_end=3268
# @@protoc_insertion_point(module_scope)
