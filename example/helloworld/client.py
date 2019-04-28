import asyncio

from grpclib.client import Channel

# generated by protoc
from .helloworld_pb2 import HelloRequest, HelloReply
from .helloworld_grpc import GreeterStub


async def main():
    loop = asyncio.get_event_loop()
    channel = Channel('127.0.0.1', 50051, loop=loop)
    greeter = GreeterStub(channel)

    reply: HelloReply = await greeter.SayHello(HelloRequest(name='Dr. Strange'))
    print(reply.message)

    channel.close()


if __name__ == '__main__':
    asyncio.run(main())
