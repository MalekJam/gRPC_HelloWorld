# gRPC Go Project

This repository contains a gRPC-based project written in Go. The project demonstrates the use of gRPC and Protocol Buffers to define services, generate Go code from `.proto` files, and implement a client-server model using Go's standard library and gRPC framework.

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
  - [Installing Dependencies](#installing-dependencies)
  - [Compiling Proto Files](#compiling-proto-files)
- [Running the Application](#running-the-application)
  - [Building the Server and Client](#building-the-server-and-client)
  - [Running the Server](#running-the-server)
  - [Running the Client](#running-the-client)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

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
