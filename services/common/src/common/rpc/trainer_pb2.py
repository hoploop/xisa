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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x63ommon/rpc/trainer.proto\x1a\x15\x63ommon/rpc/base.proto\"\x91\x01\n\x17TrainImageObjectRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0e\n\x06lesson\x18\x02 \x01(\t\x12\r\n\x05\x66rame\x18\x03 \x01(\x05\x12\r\n\x05label\x18\x04 \x01(\t\x12\x0e\n\x06xstart\x18\x05 \x01(\x02\x12\x0c\n\x04xend\x18\x06 \x01(\x02\x12\x0e\n\x06ystart\x18\x07 \x01(\x02\x12\x0c\n\x04yend\x18\x08 \x01(\x02\"X\n\x18TrainImageObjectResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\n\n\x02id\x18\x03 \x01(\tB\n\n\x08_message\"J\n\x18LessonSetDetectorRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x10\n\x08\x64\x65tector\x18\x02 \x01(\t\x12\x0e\n\x06lesson\x18\x03 \x01(\t\"j\n\x19LessonSetDetectorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1b\n\x06lesson\x18\x03 \x01(\x0b\x32\x0b.SerializedB\n\n\x08_message\"6\n\x16RecordHasLessonRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0e\n\x06record\x18\x02 \x01(\t\"x\n\x17RecordHasLessonResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12 \n\x06lesson\x18\x03 \x01(\x0b\x32\x0b.SerializedH\x01\x88\x01\x01\x42\n\n\x08_messageB\t\n\x07_lesson\"9\n\x19RecordCreateLessonRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0e\n\x06record\x18\x02 \x01(\t\"k\n\x1aRecordCreateLessonResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1b\n\x06lesson\x18\x03 \x01(\x0b\x32\x0b.SerializedB\n\n\x08_message2\xc9\x02\n\x07Trainer\x12\x14\n\x04ping\x12\x05.Ping\x1a\x05.Pong\x12\x44\n\x0frecordHasLesson\x12\x17.RecordHasLessonRequest\x1a\x18.RecordHasLessonResponse\x12M\n\x12recordCreateLesson\x12\x1a.RecordCreateLessonRequest\x1a\x1b.RecordCreateLessonResponse\x12J\n\x11lessonSetDetector\x12\x19.LessonSetDetectorRequest\x1a\x1a.LessonSetDetectorResponse\x12G\n\x10trainImageObject\x12\x18.TrainImageObjectRequest\x1a\x19.TrainImageObjectResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.rpc.trainer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TRAINIMAGEOBJECTREQUEST']._serialized_start=52
  _globals['_TRAINIMAGEOBJECTREQUEST']._serialized_end=197
  _globals['_TRAINIMAGEOBJECTRESPONSE']._serialized_start=199
  _globals['_TRAINIMAGEOBJECTRESPONSE']._serialized_end=287
  _globals['_LESSONSETDETECTORREQUEST']._serialized_start=289
  _globals['_LESSONSETDETECTORREQUEST']._serialized_end=363
  _globals['_LESSONSETDETECTORRESPONSE']._serialized_start=365
  _globals['_LESSONSETDETECTORRESPONSE']._serialized_end=471
  _globals['_RECORDHASLESSONREQUEST']._serialized_start=473
  _globals['_RECORDHASLESSONREQUEST']._serialized_end=527
  _globals['_RECORDHASLESSONRESPONSE']._serialized_start=529
  _globals['_RECORDHASLESSONRESPONSE']._serialized_end=649
  _globals['_RECORDCREATELESSONREQUEST']._serialized_start=651
  _globals['_RECORDCREATELESSONREQUEST']._serialized_end=708
  _globals['_RECORDCREATELESSONRESPONSE']._serialized_start=710
  _globals['_RECORDCREATELESSONRESPONSE']._serialized_end=817
  _globals['_TRAINER']._serialized_start=820
  _globals['_TRAINER']._serialized_end=1149
# @@protoc_insertion_point(module_scope)
