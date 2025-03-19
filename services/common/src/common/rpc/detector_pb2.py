# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: common/rpc/detector.proto
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
    'common/rpc/detector.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.rpc import base_pb2 as common_dot_rpc_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x63ommon/rpc/detector.proto\x1a\x15\x63ommon/rpc/base.proto\"\xa1\x01\n\nDetectText\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01w\x18\x03 \x01(\x02\x12\t\n\x01h\x18\x04 \x01(\x02\x12\x0c\n\x04page\x18\x05 \x01(\x05\x12\r\n\x05\x62lock\x18\x06 \x01(\x05\x12\x0b\n\x03par\x18\x07 \x01(\x05\x12\x0c\n\x04line\x18\x08 \x01(\x05\x12\x0c\n\x04word\x18\t \x01(\x05\x12\r\n\x05value\x18\n \x01(\t\x12\x12\n\nconfidence\x18\x0b \x01(\x02\"X\n\x12\x44\x65tectTextsRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\x12\x17\n\nconfidence\x18\x04 \x01(\x02H\x00\x88\x01\x01\x42\r\n\x0b_confidence\"c\n\x13\x44\x65tectTextsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\x05texts\x18\x03 \x03(\x0b\x32\x0b.DetectTextB\n\n\x08_message\"\x84\x01\n\x0c\x44\x65tectObject\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01w\x18\x03 \x01(\x02\x12\t\n\x01h\x18\x04 \x01(\x02\x12\x12\n\nconfidence\x18\x05 \x01(\x02\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0c\n\x04\x63ode\x18\x07 \x01(\x05\x12\x0b\n\x03row\x18\x08 \x01(\x05\x12\x0b\n\x03\x63ol\x18\t \x01(\x05\"l\n\x14\x44\x65tectObjectsRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\x12\x10\n\x08\x64\x65tector\x18\x03 \x01(\t\x12\x17\n\nconfidence\x18\x04 \x01(\x02H\x00\x88\x01\x01\x42\r\n\x0b_confidence\"i\n\x15\x44\x65tectObjectsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1e\n\x07objects\x18\x03 \x03(\x0b\x32\r.DetectObjectB\n\n\x08_message\"=\n\x1e\x43ountDetectorImageLabelRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\r\n\x05image\x18\x02 \x01(\t\"b\n\x1f\x43ountDetectorImageLabelResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\r\n\x05total\x18\x03 \x01(\x05\x42\n\n\x08_message\">\n\x1fRemoveDetectorImageLabelRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\"T\n RemoveDetectorImageLabelResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_message\";\n\x19\x43ountDetectorClassRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x10\n\x08\x64\x65tector\x18\x02 \x01(\t\"]\n\x1a\x43ountDetectorClassResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\r\n\x05total\x18\x03 \x01(\x05\x42\n\n\x08_message\"g\n\x18ListDetectorClassRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x10\n\x08\x64\x65tector\x18\x02 \x01(\t\x12\x0c\n\x04skip\x18\x03 \x01(\x05\x12\r\n\x05limit\x18\x04 \x01(\x05\x12\x0e\n\x06search\x18\x05 \x01(\t\"z\n\x19ListDetectorClassResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x1c\n\x07\x63lasses\x18\x04 \x03(\x0b\x32\x0b.SerializedB\n\n\x08_message\"i\n\x1dListDetectorImageLabelRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\r\n\x05image\x18\x02 \x01(\t\x12\x0c\n\x04skip\x18\x03 \x01(\x05\x12\r\n\x05limit\x18\x04 \x01(\x05\x12\x0e\n\x06search\x18\x05 \x01(\t\"~\n\x1eListDetectorImageLabelResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x1b\n\x06labels\x18\x04 \x03(\x0b\x32\x0b.SerializedB\n\n\x08_message\"m\n\x1aUploadDetectorImageRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x10\n\x08\x64\x65tector\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\t\x12!\n\x05modes\x18\x04 \x03(\x0e\x32\x12.DetectorImageMode\"l\n\x1bUploadDetectorImageResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1b\n\x06images\x18\x03 \x03(\x0b\x32\x0b.SerializedB\n\n\x08_message\"\x88\x01\n\x1c\x41\x64\x64\x44\x65tectorImageLabelRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\r\n\x05image\x18\x02 \x01(\t\x12\x0e\n\x06xstart\x18\x03 \x01(\x02\x12\x0c\n\x04xend\x18\x04 \x01(\x02\x12\x0e\n\x06ystart\x18\x05 \x01(\x02\x12\x0c\n\x04yend\x18\x06 \x01(\x02\x12\x0f\n\x07\x63lasses\x18\x07 \x03(\t\"m\n\x1d\x41\x64\x64\x44\x65tectorImageLabelResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\x05label\x18\x03 \x01(\x0b\x32\x0b.SerializedB\n\n\x08_message\"1\n\x15RemoveDetectorRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\"J\n\x16RemoveDetectorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_message\"6\n\x1aRemoveDetectorImageRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\"O\n\x1bRemoveDetectorImageResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_message\";\n\x19\x43ountDetectorImageRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x10\n\x08\x64\x65tector\x18\x02 \x01(\t\"]\n\x1a\x43ountDetectorImageResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\r\n\x05total\x18\x03 \x01(\x05\x42\n\n\x08_message\"W\n\x18ListDetectorImageRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x10\n\x08\x64\x65tector\x18\x02 \x01(\t\x12\x0c\n\x04skip\x18\x03 \x01(\x05\x12\r\n\x05limit\x18\x04 \x01(\x05\"y\n\x19ListDetectorImageResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x1b\n\x06images\x18\x04 \x03(\x0b\x32\x0b.SerializedB\n\n\x08_message\"j\n\x14TrainDetectorRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0f\n\x07session\x18\x02 \x01(\t\x12\x10\n\x08\x64\x65tector\x18\x03 \x01(\t\x12\x0e\n\x06\x65pochs\x18\x04 \x01(\x05\x12\x11\n\timageSize\x18\x05 \x01(\x05\"I\n\x15TrainDetectorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_message\"y\n\x15\x43reateDetectorRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x13\n\x06origin\x18\x05 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_origin\"i\n\x16\x43reateDetectorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1d\n\x08\x64\x65tector\x18\x03 \x01(\x0b\x32\x0b.SerializedB\n\n\x08_message\"/\n\x13LoadDetectorRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\"g\n\x14LoadDetectorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1d\n\x08\x64\x65tector\x18\x03 \x01(\x0b\x32\x0b.SerializedB\n\n\x08_message\"T\n\x15UpdateDetectorRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\"i\n\x16UpdateDetectorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1d\n\x08\x64\x65tector\x18\x03 \x01(\x0b\x32\x0b.SerializedB\n\n\x08_message\"5\n\x14\x43ountDetectorRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\"X\n\x15\x43ountDetectorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\r\n\x05total\x18\x03 \x01(\x05\x42\n\n\x08_message\"a\n\x13ListDetectorRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x12\x0c\n\x04skip\x18\x03 \x01(\x05\x12\r\n\x05limit\x18\x04 \x01(\x05\x12\x0e\n\x06search\x18\x05 \x01(\t\"w\n\x14ListDetectorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\r\n\x05total\x18\x03 \x01(\x05\x12\x1e\n\tdetectors\x18\x04 \x03(\x0b\x32\x0b.SerializedB\n\n\x08_message*1\n\x11\x44\x65tectorImageMode\x12\t\n\x05TRAIN\x10\x00\x12\x07\n\x03VAL\x10\x01\x12\x08\n\x04TEST\x10\x02\x32\xa9\x0b\n\x08\x44\x65tector\x12\x14\n\x04ping\x12\x05.Ping\x1a\x05.Pong\x12;\n\x0cloadDetector\x12\x14.LoadDetectorRequest\x1a\x15.LoadDetectorResponse\x12;\n\x0clistDetector\x12\x14.ListDetectorRequest\x1a\x15.ListDetectorResponse\x12\x41\n\x0eremoveDetector\x12\x16.RemoveDetectorRequest\x1a\x17.RemoveDetectorResponse\x12>\n\rcountDetector\x12\x15.CountDetectorRequest\x1a\x16.CountDetectorResponse\x12\x41\n\x0eupdateDetector\x12\x16.UpdateDetectorRequest\x1a\x17.UpdateDetectorResponse\x12\x41\n\x0e\x63reateDetector\x12\x16.CreateDetectorRequest\x1a\x17.CreateDetectorResponse\x12>\n\rtrainDetector\x12\x15.TrainDetectorRequest\x1a\x16.TrainDetectorResponse\x12>\n\rdetectObjects\x12\x15.DetectObjectsRequest\x1a\x16.DetectObjectsResponse\x12\x38\n\x0b\x64\x65tectTexts\x12\x13.DetectTextsRequest\x1a\x14.DetectTextsResponse\x12P\n\x13uploadDetectorImage\x12\x1b.UploadDetectorImageRequest\x1a\x1c.UploadDetectorImageResponse\x12J\n\x11listDetectorImage\x12\x19.ListDetectorImageRequest\x1a\x1a.ListDetectorImageResponse\x12M\n\x12\x63ountDetectorImage\x12\x1a.CountDetectorImageRequest\x1a\x1b.CountDetectorImageResponse\x12P\n\x13removeDetectorImage\x12\x1b.RemoveDetectorImageRequest\x1a\x1c.RemoveDetectorImageResponse\x12_\n\x18removeDetectorImageLabel\x12 .RemoveDetectorImageLabelRequest\x1a!.RemoveDetectorImageLabelResponse\x12\\\n\x17\x63ountDetectorImageLabel\x12\x1f.CountDetectorImageLabelRequest\x1a .CountDetectorImageLabelResponse\x12V\n\x15\x61\x64\x64\x44\x65tectorImageLabel\x12\x1d.AddDetectorImageLabelRequest\x1a\x1e.AddDetectorImageLabelResponse\x12Y\n\x16listDetectorImageLabel\x12\x1e.ListDetectorImageLabelRequest\x1a\x1f.ListDetectorImageLabelResponse\x12J\n\x11listDetectorClass\x12\x19.ListDetectorClassRequest\x1a\x1a.ListDetectorClassResponse\x12M\n\x12\x63ountDetectorClass\x12\x1a.CountDetectorClassRequest\x1a\x1b.CountDetectorClassResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.rpc.detector_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DETECTORIMAGEMODE']._serialized_start=3920
  _globals['_DETECTORIMAGEMODE']._serialized_end=3969
  _globals['_DETECTTEXT']._serialized_start=53
  _globals['_DETECTTEXT']._serialized_end=214
  _globals['_DETECTTEXTSREQUEST']._serialized_start=216
  _globals['_DETECTTEXTSREQUEST']._serialized_end=304
  _globals['_DETECTTEXTSRESPONSE']._serialized_start=306
  _globals['_DETECTTEXTSRESPONSE']._serialized_end=405
  _globals['_DETECTOBJECT']._serialized_start=408
  _globals['_DETECTOBJECT']._serialized_end=540
  _globals['_DETECTOBJECTSREQUEST']._serialized_start=542
  _globals['_DETECTOBJECTSREQUEST']._serialized_end=650
  _globals['_DETECTOBJECTSRESPONSE']._serialized_start=652
  _globals['_DETECTOBJECTSRESPONSE']._serialized_end=757
  _globals['_COUNTDETECTORIMAGELABELREQUEST']._serialized_start=759
  _globals['_COUNTDETECTORIMAGELABELREQUEST']._serialized_end=820
  _globals['_COUNTDETECTORIMAGELABELRESPONSE']._serialized_start=822
  _globals['_COUNTDETECTORIMAGELABELRESPONSE']._serialized_end=920
  _globals['_REMOVEDETECTORIMAGELABELREQUEST']._serialized_start=922
  _globals['_REMOVEDETECTORIMAGELABELREQUEST']._serialized_end=984
  _globals['_REMOVEDETECTORIMAGELABELRESPONSE']._serialized_start=986
  _globals['_REMOVEDETECTORIMAGELABELRESPONSE']._serialized_end=1070
  _globals['_COUNTDETECTORCLASSREQUEST']._serialized_start=1072
  _globals['_COUNTDETECTORCLASSREQUEST']._serialized_end=1131
  _globals['_COUNTDETECTORCLASSRESPONSE']._serialized_start=1133
  _globals['_COUNTDETECTORCLASSRESPONSE']._serialized_end=1226
  _globals['_LISTDETECTORCLASSREQUEST']._serialized_start=1228
  _globals['_LISTDETECTORCLASSREQUEST']._serialized_end=1331
  _globals['_LISTDETECTORCLASSRESPONSE']._serialized_start=1333
  _globals['_LISTDETECTORCLASSRESPONSE']._serialized_end=1455
  _globals['_LISTDETECTORIMAGELABELREQUEST']._serialized_start=1457
  _globals['_LISTDETECTORIMAGELABELREQUEST']._serialized_end=1562
  _globals['_LISTDETECTORIMAGELABELRESPONSE']._serialized_start=1564
  _globals['_LISTDETECTORIMAGELABELRESPONSE']._serialized_end=1690
  _globals['_UPLOADDETECTORIMAGEREQUEST']._serialized_start=1692
  _globals['_UPLOADDETECTORIMAGEREQUEST']._serialized_end=1801
  _globals['_UPLOADDETECTORIMAGERESPONSE']._serialized_start=1803
  _globals['_UPLOADDETECTORIMAGERESPONSE']._serialized_end=1911
  _globals['_ADDDETECTORIMAGELABELREQUEST']._serialized_start=1914
  _globals['_ADDDETECTORIMAGELABELREQUEST']._serialized_end=2050
  _globals['_ADDDETECTORIMAGELABELRESPONSE']._serialized_start=2052
  _globals['_ADDDETECTORIMAGELABELRESPONSE']._serialized_end=2161
  _globals['_REMOVEDETECTORREQUEST']._serialized_start=2163
  _globals['_REMOVEDETECTORREQUEST']._serialized_end=2212
  _globals['_REMOVEDETECTORRESPONSE']._serialized_start=2214
  _globals['_REMOVEDETECTORRESPONSE']._serialized_end=2288
  _globals['_REMOVEDETECTORIMAGEREQUEST']._serialized_start=2290
  _globals['_REMOVEDETECTORIMAGEREQUEST']._serialized_end=2344
  _globals['_REMOVEDETECTORIMAGERESPONSE']._serialized_start=2346
  _globals['_REMOVEDETECTORIMAGERESPONSE']._serialized_end=2425
  _globals['_COUNTDETECTORIMAGEREQUEST']._serialized_start=2427
  _globals['_COUNTDETECTORIMAGEREQUEST']._serialized_end=2486
  _globals['_COUNTDETECTORIMAGERESPONSE']._serialized_start=2488
  _globals['_COUNTDETECTORIMAGERESPONSE']._serialized_end=2581
  _globals['_LISTDETECTORIMAGEREQUEST']._serialized_start=2583
  _globals['_LISTDETECTORIMAGEREQUEST']._serialized_end=2670
  _globals['_LISTDETECTORIMAGERESPONSE']._serialized_start=2672
  _globals['_LISTDETECTORIMAGERESPONSE']._serialized_end=2793
  _globals['_TRAINDETECTORREQUEST']._serialized_start=2795
  _globals['_TRAINDETECTORREQUEST']._serialized_end=2901
  _globals['_TRAINDETECTORRESPONSE']._serialized_start=2903
  _globals['_TRAINDETECTORRESPONSE']._serialized_end=2976
  _globals['_CREATEDETECTORREQUEST']._serialized_start=2978
  _globals['_CREATEDETECTORREQUEST']._serialized_end=3099
  _globals['_CREATEDETECTORRESPONSE']._serialized_start=3101
  _globals['_CREATEDETECTORRESPONSE']._serialized_end=3206
  _globals['_LOADDETECTORREQUEST']._serialized_start=3208
  _globals['_LOADDETECTORREQUEST']._serialized_end=3255
  _globals['_LOADDETECTORRESPONSE']._serialized_start=3257
  _globals['_LOADDETECTORRESPONSE']._serialized_end=3360
  _globals['_UPDATEDETECTORREQUEST']._serialized_start=3362
  _globals['_UPDATEDETECTORREQUEST']._serialized_end=3446
  _globals['_UPDATEDETECTORRESPONSE']._serialized_start=3448
  _globals['_UPDATEDETECTORRESPONSE']._serialized_end=3553
  _globals['_COUNTDETECTORREQUEST']._serialized_start=3555
  _globals['_COUNTDETECTORREQUEST']._serialized_end=3608
  _globals['_COUNTDETECTORRESPONSE']._serialized_start=3610
  _globals['_COUNTDETECTORRESPONSE']._serialized_end=3698
  _globals['_LISTDETECTORREQUEST']._serialized_start=3700
  _globals['_LISTDETECTORREQUEST']._serialized_end=3797
  _globals['_LISTDETECTORRESPONSE']._serialized_start=3799
  _globals['_LISTDETECTORRESPONSE']._serialized_end=3918
  _globals['_DETECTOR']._serialized_start=3972
  _globals['_DETECTOR']._serialized_end=5421
# @@protoc_insertion_point(module_scope)
