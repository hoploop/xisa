# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from common.rpc import base_pb2 as common_dot_rpc_dot_base__pb2
from common.rpc import nanny_pb2 as common_dot_rpc_dot_nanny__pb2

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
        + f' but the generated code in common/rpc/nanny_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class NannyStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ping = channel.unary_unary(
                '/Nanny/ping',
                request_serializer=common_dot_rpc_dot_base__pb2.Ping.SerializeToString,
                response_deserializer=common_dot_rpc_dot_base__pb2.Pong.FromString,
                _registered_method=True)
        self.nannyStatus = channel.unary_unary(
                '/Nanny/nannyStatus',
                request_serializer=common_dot_rpc_dot_nanny__pb2.NannyStatusRequest.SerializeToString,
                response_deserializer=common_dot_rpc_dot_nanny__pb2.NannyStatusResponse.FromString,
                _registered_method=True)


class NannyServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ping(self, request, context):
        """Performs synchronous ping of service
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def nannyStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NannyServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ping': grpc.unary_unary_rpc_method_handler(
                    servicer.ping,
                    request_deserializer=common_dot_rpc_dot_base__pb2.Ping.FromString,
                    response_serializer=common_dot_rpc_dot_base__pb2.Pong.SerializeToString,
            ),
            'nannyStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.nannyStatus,
                    request_deserializer=common_dot_rpc_dot_nanny__pb2.NannyStatusRequest.FromString,
                    response_serializer=common_dot_rpc_dot_nanny__pb2.NannyStatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Nanny', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('Nanny', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Nanny(object):
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
            '/Nanny/ping',
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
    def nannyStatus(request,
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
            '/Nanny/nannyStatus',
            common_dot_rpc_dot_nanny__pb2.NannyStatusRequest.SerializeToString,
            common_dot_rpc_dot_nanny__pb2.NannyStatusResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
