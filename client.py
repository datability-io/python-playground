import logging

import grpc
from grpc_test import helloworld_pb2_grpc
from grpc_test.xyz import msg_pb2


def run() -> None:
    print("Will try to greet world ...")
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)  # type: ignore
        response = stub.SayHello(
            msg_pb2.HelloRequest(name='Thomas'),
        )
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
