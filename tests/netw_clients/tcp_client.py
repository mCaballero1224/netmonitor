#!/bin/python

import socket


def tcp_client():
    # Create a socket:
    # socket(): Create a TCP/IP socket using AF_INET for IPv4
    # and SOCK_STREAM for TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the server's IP address and port number to connect to
    server_address = '127.0.0.1'  # localhost
    server_port = 12345

    try:
        # Establish a connection:
        # connect(): Connect the socket to the server's address and port
        sock.connect((server_address, server_port))

        # Send and Recieve the Data:
        # sendall(): Send data to the server
        message = 'Hello, Server!'
        print(f"Sending {message} to {server_address} on port {server_port}")
        sock.sendall(message.encode())

        # recv(): Recieve data from the server, specifying the buffer size
        response = sock.recv(1024)
        print(f"Received {response.decode()}")

    finally:
        # Close the Connection:
        # close(): Close the socket to free up resources
        sock.close()


if __name__ == "__main__":
    tcp_client()
