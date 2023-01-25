import logging
from concurrent import futures
from typing import Any

import grpc
from grpc_test import helloworld_pb2_grpc
from grpc_test.xyz import msg_pb2


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(
        self,
        request: msg_pb2.HelloRequest,
        context: Any,
    ) -> msg_pb2.HelloReply:
        return msg_pb2.HelloReply(message='Hello, %s!' % request.name)


def serve() -> None:
    port = '50052'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(
        Greeter(), server,
    )  # type: ignore
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
