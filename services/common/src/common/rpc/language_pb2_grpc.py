# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from common.rpc import base_pb2 as common_dot_rpc_dot_base__pb2
from common.rpc import language_pb2 as common_dot_rpc_dot_language__pb2

GRPC_GENERATED_VERSION = '1.67.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in common/rpc/language_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class LanguageStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ping = channel.unary_unary(
                '/Language/ping',
                request_serializer=common_dot_rpc_dot_base__pb2.Ping.SerializeToString,
                response_deserializer=common_dot_rpc_dot_base__pb2.Pong.FromString,
                _registered_method=True)
        self.languageEncode = channel.unary_unary(
                '/Language/languageEncode',
                request_serializer=common_dot_rpc_dot_language__pb2.LanguageEncodeRequest.SerializeToString,
                response_deserializer=common_dot_rpc_dot_language__pb2.LanguageEncodeResponse.FromString,
                _registered_method=True)
        self.languageDecode = channel.unary_unary(
                '/Language/languageDecode',
                request_serializer=common_dot_rpc_dot_language__pb2.LanguageDecodeRequest.SerializeToString,
                response_deserializer=common_dot_rpc_dot_language__pb2.LanguageDecodeResponse.FromString,
                _registered_method=True)
        self.languageTranslate = channel.unary_unary(
                '/Language/languageTranslate',
                request_serializer=common_dot_rpc_dot_language__pb2.LanguageTranslateRequest.SerializeToString,
                response_deserializer=common_dot_rpc_dot_language__pb2.LanguageTranslateResponse.FromString,
                _registered_method=True)


class LanguageServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ping(self, request, context):
        """Performs synchronous ping of service
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def languageEncode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def languageDecode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def languageTranslate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LanguageServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ping': grpc.unary_unary_rpc_method_handler(
                    servicer.ping,
                    request_deserializer=common_dot_rpc_dot_base__pb2.Ping.FromString,
                    response_serializer=common_dot_rpc_dot_base__pb2.Pong.SerializeToString,
            ),
            'languageEncode': grpc.unary_unary_rpc_method_handler(
                    servicer.languageEncode,
                    request_deserializer=common_dot_rpc_dot_language__pb2.LanguageEncodeRequest.FromString,
                    response_serializer=common_dot_rpc_dot_language__pb2.LanguageEncodeResponse.SerializeToString,
            ),
            'languageDecode': grpc.unary_unary_rpc_method_handler(
                    servicer.languageDecode,
                    request_deserializer=common_dot_rpc_dot_language__pb2.LanguageDecodeRequest.FromString,
                    response_serializer=common_dot_rpc_dot_language__pb2.LanguageDecodeResponse.SerializeToString,
            ),
            'languageTranslate': grpc.unary_unary_rpc_method_handler(
                    servicer.languageTranslate,
                    request_deserializer=common_dot_rpc_dot_language__pb2.LanguageTranslateRequest.FromString,
                    response_serializer=common_dot_rpc_dot_language__pb2.LanguageTranslateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Language', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('Language', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Language(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Language/ping',
            common_dot_rpc_dot_base__pb2.Ping.SerializeToString,
            common_dot_rpc_dot_base__pb2.Pong.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def languageEncode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Language/languageEncode',
            common_dot_rpc_dot_language__pb2.LanguageEncodeRequest.SerializeToString,
            common_dot_rpc_dot_language__pb2.LanguageEncodeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def languageDecode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Language/languageDecode',
            common_dot_rpc_dot_language__pb2.LanguageDecodeRequest.SerializeToString,
            common_dot_rpc_dot_language__pb2.LanguageDecodeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def languageTranslate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/Language/languageTranslate',
            common_dot_rpc_dot_language__pb2.LanguageTranslateRequest.SerializeToString,
            common_dot_rpc_dot_language__pb2.LanguageTranslateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
