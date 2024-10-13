# HelloWorld Distributed Application

This repository contains a distributed client-server application named **HelloWorld** that supports greetings in three languages: French, English, and Arabic. The application is designed to allow users to select their preferred language for greetings, showcasing the versatility of gRPC for efficient communication between the client and server.

## Project Description

The **HelloWorld** application utilizes gRPC to facilitate communication between a client and server, where the server responds with greetings in the language selected by the user. The project aims to demonstrate the following key features:

- **Multilingual Support:** Users can receive greetings in French, English, or Arabic, based on their preference.
- **Distributed Architecture:** The application is designed to run across multiple programming languages, such as Go and Python, showcasing the interoperability of gRPC.
- **Streaming Capability:** The server implements a streaming RPC, allowing for continuous communication and interaction between the client and server.

## Features

- **User Language Selection:** The client prompts users to select a language for their greeting, making the application user-friendly and adaptable.
- **gRPC Communication:** The application employs gRPC to ensure efficient and robust communication between the client and server.
- **Cross-Platform:** The project can be tested locally on a single machine, distributed across two PCs, or even run on a PC with a smartphone client, demonstrating flexibility in deployment.

## Setup

To set up the application, users will need to install the necessary dependencies for the programming languages used in the project. This includes installing the Protocol Buffers compiler and the gRPC libraries specific to the chosen languages.

Once the dependencies are installed, users can compile the Protocol Buffers files to generate the required code. The application consists of both server and client implementations, which can be built and run in their respective environments.

## Testing

The application can be tested in various environments:
- **Local Testing:** Both the server and client can be run on a single machine to verify functionality.
- **Distributed Testing:** The server can be hosted on one PC while the client runs on another, allowing for testing of the network communication.
- **Mobile Testing:** The application can also be tested by deploying a mobile client on a smartphone, ensuring that it can communicate with the server running on a PC.


## License

This project is licensed under the Apache 2.0 License. For more details, please refer to the [LICENSE](LICENSE) file included in the repository.
