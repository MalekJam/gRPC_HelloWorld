# Copyright 2021 gRPC authors.


import asyncio
import logging

import grpc
import hellostreamingworld_pb2
import hellostreamingworld_pb2_grpc


async def run() -> None:
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = hellostreamingworld_pb2_grpc.MultiGreeterStub(channel)


        async for response in stub.sayHello(
            hellostreamingworld_pb2.HelloRequest(name="you")
        ):
            print(
                "client received from async generator: "
                + response.message
            )

        hello_stream = stub.sayHello(
            hellostreamingworld_pb2.HelloRequest(name="you")
        )
        while True:
            response = await hello_stream.read()
            if response == grpc.aio.EOF:
                break
            print(
                "client received from direct read: " + response.message
            )


if __name__ == "__main__":
    logging.basicConfig()
    asyncio.run(run())
