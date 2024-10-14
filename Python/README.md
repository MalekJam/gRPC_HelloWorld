# gRPC Python Project

This repository contains a gRPC-based project using Python. The project demonstrates the use of gRPC and protocol buffers to define services, generate Python code from `.proto` files, and implement a client-server model using Python's asynchronous capabilities.

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
  - [Installing Dependencies](#installing-dependencies)
  - [Compiling Proto Files](#compiling-proto-files)
- [Running the Application](#running-the-application)


## Project Description

This project demonstrates how to use **gRPC** for communication between client and server using **Python**. It uses **Protocol Buffers** to define a simple service in the `hello_world.proto` file, which is then used to generate Python stubs for both the client and server.

## Features

- **gRPC** client-server model.
- **Protocol Buffers** for efficient serialization.
- **AsyncIO** for asynchronous communication.
- Unit testing and coverage reports with **unittest** and **coverage**.

## Requirements

- Python 3.7+
- `pip` (Python package installer)
- `protoc` (Protocol Buffers compiler)

Python package dependencies are listed in the `requirements.txt` file.

## Setup

### Compiling Proto Files

You'll need to compile the `.proto` files using the `protoc` compiler to generate Python code.

1. Install `protoc` if you don't already have it installed. You can download it from the [official Protocol Buffers releases page](https://github.com/protocolbuffers/protobuf/releases), or use a package manager like `brew`:

    ```bash
    pip install protobuf
    ```

2. Compile the `helloworld.proto` file to generate Python stubs:

    ```bash
    protoc --python_out=. --grpc_python_out=. hello_world.proto
    ```

This will generate Python files for the gRPC service and the protocol buffer messages based on your `.proto` file.

## Running the Application

1. **Start the gRPC server:**

    Run the server script to start listening for client requests:

    ```bash
    python server.py
    ```

2. **Run the gRPC client:**

    In another terminal window, run the client script to communicate with the server:

    ```bash
    python client.py
    ```

The client should successfully make requests to the gRPC service, and the server should respond accordingly.




