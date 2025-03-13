# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: common/rpc/auth.proto
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
    'common/rpc/auth.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.rpc import base_pb2 as common_dot_rpc_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x63ommon/rpc/auth.proto\x1a\x15\x63ommon/rpc/base.proto\"\x1c\n\x0bUserRequest\x12\r\n\x05token\x18\x01 \x01(\t\"[\n\x0cUserResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x19\n\x04user\x18\x03 \x01(\x0b\x32\x0b.SerializedB\n\n\x08_message\"\x1d\n\x0c\x43heckRequest\x12\r\n\x05token\x18\x01 \x01(\t\"A\n\rCheckResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_message\"@\n\x0cLoginRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x0c\n\x04host\x18\x03 \x01(\t\"_\n\rLoginResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05token\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\n\n\x08_messageB\x08\n\x06_token\"\x1e\n\rLogoutRequest\x12\r\n\x05token\x18\x01 \x01(\t\"B\n\x0eLogoutResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_message\"D\n\x0fRegisterRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"D\n\x10RegisterResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_message\"\"\n\x11UnregisterRequest\x12\r\n\x05token\x18\x01 \x01(\t\"F\n\x12UnregisterResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_message\"M\n\x14ResetPasswordRequest\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x0b\n\x03old\x18\x03 \x01(\t\x12\x0b\n\x03new\x18\x04 \x01(\t\"I\n\x15ResetPasswordResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_message2\xe4\x02\n\x04\x41uth\x12\x14\n\x04ping\x12\x05.Ping\x1a\x05.Pong\x12&\n\x05\x63heck\x12\r.CheckRequest\x1a\x0e.CheckResponse\x12&\n\x05login\x12\r.LoginRequest\x1a\x0e.LoginResponse\x12#\n\x04user\x12\x0c.UserRequest\x1a\r.UserResponse\x12)\n\x06logout\x12\x0e.LogoutRequest\x1a\x0f.LogoutResponse\x12/\n\x08register\x12\x10.RegisterRequest\x1a\x11.RegisterResponse\x12\x35\n\nunregister\x12\x12.UnregisterRequest\x1a\x13.UnregisterResponse\x12>\n\rresetPassword\x12\x15.ResetPasswordRequest\x1a\x16.ResetPasswordResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.rpc.auth_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_USERREQUEST']._serialized_start=48
  _globals['_USERREQUEST']._serialized_end=76
  _globals['_USERRESPONSE']._serialized_start=78
  _globals['_USERRESPONSE']._serialized_end=169
  _globals['_CHECKREQUEST']._serialized_start=171
  _globals['_CHECKREQUEST']._serialized_end=200
  _globals['_CHECKRESPONSE']._serialized_start=202
  _globals['_CHECKRESPONSE']._serialized_end=267
  _globals['_LOGINREQUEST']._serialized_start=269
  _globals['_LOGINREQUEST']._serialized_end=333
  _globals['_LOGINRESPONSE']._serialized_start=335
  _globals['_LOGINRESPONSE']._serialized_end=430
  _globals['_LOGOUTREQUEST']._serialized_start=432
  _globals['_LOGOUTREQUEST']._serialized_end=462
  _globals['_LOGOUTRESPONSE']._serialized_start=464
  _globals['_LOGOUTRESPONSE']._serialized_end=530
  _globals['_REGISTERREQUEST']._serialized_start=532
  _globals['_REGISTERREQUEST']._serialized_end=600
  _globals['_REGISTERRESPONSE']._serialized_start=602
  _globals['_REGISTERRESPONSE']._serialized_end=670
  _globals['_UNREGISTERREQUEST']._serialized_start=672
  _globals['_UNREGISTERREQUEST']._serialized_end=706
  _globals['_UNREGISTERRESPONSE']._serialized_start=708
  _globals['_UNREGISTERRESPONSE']._serialized_end=778
  _globals['_RESETPASSWORDREQUEST']._serialized_start=780
  _globals['_RESETPASSWORDREQUEST']._serialized_end=857
  _globals['_RESETPASSWORDRESPONSE']._serialized_start=859
  _globals['_RESETPASSWORDRESPONSE']._serialized_end=932
  _globals['_AUTH']._serialized_start=935
  _globals['_AUTH']._serialized_end=1291
# @@protoc_insertion_point(module_scope)
