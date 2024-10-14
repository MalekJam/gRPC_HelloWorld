# gRPC Go Project

This repository contains a gRPC-based project written in Go. The project demonstrates the use of gRPC and Protocol Buffers to define services, generate Go code from `.proto` files, and implement a client-server model using Go's standard library and gRPC framework.

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Requirements](#requirements)
- [Running the Application](#running-the-application)
- [Testing](#testing)


## Project Description

This project demonstrates how to use **gRPC** in Go to establish communication between client and server. **Protocol Buffers** are used to define a `SayHello` service, and Go code is generated from the `.proto` files to implement both the server and client.

## Features

- **gRPC** client-server model in Go.
- **Protocol Buffers** for efficient data serialization.
- Generated Go stubs for server and client communication.
- Basic unit testing with Go's built-in testing tools.

## Requirements

Ensure you have the following tools installed:

- Go 1.15 or higher
- `protoc` (Protocol Buffers compiler)
- `protoc-gen-go` and `protoc-gen-go-grpc` plugins

You can install the necessary plugins with the following Go commands:

```bash
go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
```

## Running the Application

- Compiling Proto Files
To generate code from the `.proto` files, use `protoc` with the appropriate plugins for each language:
```bash
protoc --go_out=. --go-grpc_out=. helloworld.proto
```
This will generate Go files for the gRPC service and the protocol buffer messages based on your `.proto` file.

- Builiding the Server and Client
Once the `.proto` files have been compiled, you can build the server and client:
**Build the server**
```bash
go build -o $(go env GOPATH)/bin/helloworld_server server.go

```
**Build the client**
```bash
go build -o $(go env GOPATH)/bin/helloworld_client client.go

```

- Testing

**Run the server**
```bash
$(go env GOPATH)/bin/helloworld_server
```
**Build the client**
```bash
$(go env GOPATH)/bin/helloworld_client

```


