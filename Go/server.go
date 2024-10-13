package main

import (
    "context"
    "flag"
    "fmt"
    "log"
    "net"

    "google.golang.org/grpc"
    pb "google.golang.org/grpc/examples/helloworld/helloworld"
)

var (
    port = flag.Int("port", 50051, "The server port")
)


type server struct {
    pb.UnimplementedGreeterServer
}


func (s *server) SayHello(_ context.Context, in *pb.HelloRequest) (*pb.HelloReply, error) {
    log.Printf("Received request with input: %v", in.GetName())

    name := in.GetName() // Get the name from the request
    var result string


    switch name {
    case "1":
        result = "مــــــرحبــــا" // Arabic
    case "2":
        result = "Bonjour !" // French
    case "3":
        result = "Good morning !" // English
    default:
        result = "Unknown greeting."
    }

    return &pb.HelloReply{Message: "                " + result}, nil
}

func main() {
    flag.Parse()
    lis, err := net.Listen("tcp", fmt.Sprintf(":%d", *port))
    if err != nil {
        log.Fatalf("Failed to listen: %v", err)
    }
    s := grpc.NewServer()
    pb.RegisterGreeterServer(s, &server{})

    log.Printf("Server is listening on %v", lis.Addr())
    if err := s.Serve(lis); err != nil {
        log.Fatalf("Failed to serve: %v", err)
    }
}
