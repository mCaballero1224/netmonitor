#!/bin/python

import socket


def udp_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = '127.0.0.1'
    server_port = 12345

    try:
        message = 'Hello, UDP Server!'
        print(f"Sending: {message}")
        sock.sendto(message.encode(), (server_address, server_port))

        response, server = sock.recvfrom(1024)
        print(f"Received: {response.decode()} from {server}")

    finally:
        sock.close()


if __name__ == "__main__":
    udp_client()
