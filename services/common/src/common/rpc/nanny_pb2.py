# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: common/rpc/nanny.proto
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
    'common/rpc/nanny.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.rpc import base_pb2 as common_dot_rpc_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x63ommon/rpc/nanny.proto\x1a\x15\x63ommon/rpc/base.proto\"\x14\n\x12NannyStatusRequest\"2\n\x12NannyServiceStatus\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x08\"<\n\x13NannyStatusResponse\x12%\n\x08services\x18\x01 \x03(\x0b\x32\x13.NannyServiceStatus2W\n\x05Nanny\x12\x14\n\x04ping\x12\x05.Ping\x1a\x05.Pong\x12\x38\n\x0bnannyStatus\x12\x13.NannyStatusRequest\x1a\x14.NannyStatusResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.rpc.nanny_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_NANNYSTATUSREQUEST']._serialized_start=49
  _globals['_NANNYSTATUSREQUEST']._serialized_end=69
  _globals['_NANNYSERVICESTATUS']._serialized_start=71
  _globals['_NANNYSERVICESTATUS']._serialized_end=121
  _globals['_NANNYSTATUSRESPONSE']._serialized_start=123
  _globals['_NANNYSTATUSRESPONSE']._serialized_end=183
  _globals['_NANNY']._serialized_start=185
  _globals['_NANNY']._serialized_end=272
# @@protoc_insertion_point(module_scope)
