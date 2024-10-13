from __future__ import print_function
import logging
import grpc
import hello_world_pb2
import hello_world_pb2_grpc

RED = "\033[35m"
YELLOW = "\033[33m"
BOLD = "\033[1m"
RESET = "\033[0m"

default_name = "world"
addr = "localhost:50051"

def run():

    with grpc.insecure_channel(addr) as channel:
        stub = hello_world_pb2_grpc.GreeterStub(channel)


        print(YELLOW + BOLD + "-------------------------------------------" + RESET)
        print(YELLOW + BOLD + "          Choose Your Greeting            " + RESET)
        print(YELLOW + BOLD + "-------------------------------------------" + RESET)
        print("1. Arabic Greeting (مــــــرحبــــا)")
        print("2. French Greeting (Bonjour !)")
        print("3. English Greeting (Good morning !)")
        print("-------------------------------------------")

        # Prompt the user for input
        client_input_lang = input("Please enter your choice (1, 2, or 3): ")
        print(f"You selected option: {client_input_lang}")

       try:
            ctx = grpc.insecure_channel(addr)
            with grpc.insecure_channel(addr) as channel:
                stub = hello_world_pb2_grpc.GreeterStub(channel)
                response = stub.SayHello(
                    hello_world_pb2.HelloRequest(name=client_input_lang)
                )


            print(RED + BOLD + f"Server Response: {response.message}" + RESET)

        except grpc.RpcError as e:
            logging.error(f"RPC failed: {e}")

if __name__ == "__main__":
    logging.basicConfig()
    run()
