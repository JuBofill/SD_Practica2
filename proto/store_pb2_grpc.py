# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto import store_pb2 as store__pb2


class KeyValueStoreStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.put = channel.unary_unary(
                '/distributedstore.KeyValueStore/put',
                request_serializer=store__pb2.PutRequest.SerializeToString,
                response_deserializer=store__pb2.PutResponse.FromString,
                )
        self.get = channel.unary_unary(
                '/distributedstore.KeyValueStore/get',
                request_serializer=store__pb2.GetRequest.SerializeToString,
                response_deserializer=store__pb2.GetResponse.FromString,
                )
        self.slowDown = channel.unary_unary(
                '/distributedstore.KeyValueStore/slowDown',
                request_serializer=store__pb2.SlowDownRequest.SerializeToString,
                response_deserializer=store__pb2.SlowDownResponse.FromString,
                )
        self.restore = channel.unary_unary(
                '/distributedstore.KeyValueStore/restore',
                request_serializer=store__pb2.RestoreRequest.SerializeToString,
                response_deserializer=store__pb2.RestoreResponse.FromString,
                )
        self.registerSlave = channel.unary_unary(
                '/distributedstore.KeyValueStore/registerSlave',
                request_serializer=store__pb2.RegisterSlaveRequest.SerializeToString,
                response_deserializer=store__pb2.RegisterSlaveResponse.FromString,
                )
        self.registerNode = channel.unary_unary(
                '/distributedstore.KeyValueStore/registerNode',
                request_serializer=store__pb2.RegisterNodeRequest.SerializeToString,
                response_deserializer=store__pb2.RegisterNodeResponse.FromString,
                )
        self.askVote = channel.unary_unary(
                '/distributedstore.KeyValueStore/askVote',
                request_serializer=store__pb2.AskVoteRequest.SerializeToString,
                response_deserializer=store__pb2.AskVoteResponse.FromString,
                )
        self.canCommit = channel.unary_unary(
                '/distributedstore.KeyValueStore/canCommit',
                request_serializer=store__pb2.CommitRequest.SerializeToString,
                response_deserializer=store__pb2.CommitResponse.FromString,
                )
        self.doCommit = channel.unary_unary(
                '/distributedstore.KeyValueStore/doCommit',
                request_serializer=store__pb2.CommitRequest.SerializeToString,
                response_deserializer=store__pb2.Empty.FromString,
                )


class KeyValueStoreServicer(object):
    """Missing associated documentation comment in .proto file."""

    def put(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def slowDown(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def restore(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def registerSlave(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def registerNode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def askVote(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def canCommit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def doCommit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KeyValueStoreServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'put': grpc.unary_unary_rpc_method_handler(
                    servicer.put,
                    request_deserializer=store__pb2.PutRequest.FromString,
                    response_serializer=store__pb2.PutResponse.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=store__pb2.GetRequest.FromString,
                    response_serializer=store__pb2.GetResponse.SerializeToString,
            ),
            'slowDown': grpc.unary_unary_rpc_method_handler(
                    servicer.slowDown,
                    request_deserializer=store__pb2.SlowDownRequest.FromString,
                    response_serializer=store__pb2.SlowDownResponse.SerializeToString,
            ),
            'restore': grpc.unary_unary_rpc_method_handler(
                    servicer.restore,
                    request_deserializer=store__pb2.RestoreRequest.FromString,
                    response_serializer=store__pb2.RestoreResponse.SerializeToString,
            ),
            'registerSlave': grpc.unary_unary_rpc_method_handler(
                    servicer.registerSlave,
                    request_deserializer=store__pb2.RegisterSlaveRequest.FromString,
                    response_serializer=store__pb2.RegisterSlaveResponse.SerializeToString,
            ),
            'registerNode': grpc.unary_unary_rpc_method_handler(
                    servicer.registerNode,
                    request_deserializer=store__pb2.RegisterNodeRequest.FromString,
                    response_serializer=store__pb2.RegisterNodeResponse.SerializeToString,
            ),
            'askVote': grpc.unary_unary_rpc_method_handler(
                    servicer.askVote,
                    request_deserializer=store__pb2.AskVoteRequest.FromString,
                    response_serializer=store__pb2.AskVoteResponse.SerializeToString,
            ),
            'canCommit': grpc.unary_unary_rpc_method_handler(
                    servicer.canCommit,
                    request_deserializer=store__pb2.CommitRequest.FromString,
                    response_serializer=store__pb2.CommitResponse.SerializeToString,
            ),
            'doCommit': grpc.unary_unary_rpc_method_handler(
                    servicer.doCommit,
                    request_deserializer=store__pb2.CommitRequest.FromString,
                    response_serializer=store__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'distributedstore.KeyValueStore', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class KeyValueStore(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def put(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/distributedstore.KeyValueStore/put',
            store__pb2.PutRequest.SerializeToString,
            store__pb2.PutResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/distributedstore.KeyValueStore/get',
            store__pb2.GetRequest.SerializeToString,
            store__pb2.GetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def slowDown(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/distributedstore.KeyValueStore/slowDown',
            store__pb2.SlowDownRequest.SerializeToString,
            store__pb2.SlowDownResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def restore(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/distributedstore.KeyValueStore/restore',
            store__pb2.RestoreRequest.SerializeToString,
            store__pb2.RestoreResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def registerSlave(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/distributedstore.KeyValueStore/registerSlave',
            store__pb2.RegisterSlaveRequest.SerializeToString,
            store__pb2.RegisterSlaveResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def registerNode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/distributedstore.KeyValueStore/registerNode',
            store__pb2.RegisterNodeRequest.SerializeToString,
            store__pb2.RegisterNodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def askVote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/distributedstore.KeyValueStore/askVote',
            store__pb2.AskVoteRequest.SerializeToString,
            store__pb2.AskVoteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def canCommit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/distributedstore.KeyValueStore/canCommit',
            store__pb2.CommitRequest.SerializeToString,
            store__pb2.CommitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def doCommit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/distributedstore.KeyValueStore/doCommit',
            store__pb2.CommitRequest.SerializeToString,
            store__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
