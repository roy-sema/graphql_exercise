import socket
import threading

class SimpleSocketServer:
    def __init__(self, host='127.0.0.1', port=12345):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")

    def handle_client(self, client_socket, address):
        print(f"Connection established with {address}")
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                print(f"Received: {data.decode('utf-8')}")
                client_socket.sendall(data)  # Echo back
        except ConnectionResetError:
            print("Client disconnected abruptly.")
        finally:
            client_socket.close()
            print(f"Connection closed with {address}")

    def start(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            client_handler = threading.Thread(target=self.handle_client, args=(client_socket, addr))
            client_handler.start()

if __name__ == "__main__":
    server = SimpleSocketServer()
    server.start()

