from concurrent import futures
import grpc
import hello_world_pb2
import hello_world_pb2_grpc


class Greeter(hello_world_pb2_grpc.GreeterServicer):
    def SayHelloByNumber(self, request, context):
        
        messages = {
            1: "Arabic Greeting (مــــــرحبــــا)",
            2: "French Greeting (Bonjour !)",
            3: "English Greeting (Good morning !)",
        }
        
        message = messages.get(request.number, "Number not recognized.")
        return hello_world_pb2.HelloReply(message=message)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_world_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Server started, listening on port 50051')
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
