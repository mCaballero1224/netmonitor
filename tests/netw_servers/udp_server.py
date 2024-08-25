#!/bin/python

import socket


def udp_server():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = '127.0.0.1'
    server_port = 12345
    server_sock.bind((server_address, server_port))

    print("UDP Server is ready to receive mesages...")

    try:
        while True:
            message, client_address = server_sock.recvfrom(1024)
            print(f"Received message: {
                  message.decode()} from {client_address}")

    except KeyboardInterrupt:
        print("Server is shutting down")
        server_sock.close()
        print("Server socket closed")


if __name__ == "__main__":
    udp_server()
