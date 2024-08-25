#!/bin/python
import socket


def tcp_server():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = '127.0.0.1'
    server_port = 12346
    server_sock.bind((server_address, server_port))

    server_sock.listen(5)  # Argument is the backlog of connections allowed
    print(f"Server is listening for incoming connections on {
          server_address}:{server_port}")

    try:
        while True:
            # Accept Connections:
            # accept(): Accept a new connection
            client_sock, client_address = server_sock.accept()
            print(f"Connection from {client_address}")

            try:
                # Send and Receive Data:
                message = client_sock.recv(1024)
                print(f"Received message: {message.decode()}")

                response = "Message received"
                client_sock.sendall(response.encode())

            finally:
                client_sock.close()
                print(f"Connection with {client_address} closed")

    except KeyboardInterrupt:
        print("Server is shutting down")

    finally:
        server_sock.close()
        print("Server socket closed")


if __name__ == "__main__":
    tcp_server()
