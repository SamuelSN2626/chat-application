import socket
import threading

def handle_client(client_socket):
    """Handle incoming messages from a client."""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Client: {message}")
        except:
            break
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 12345))
    server.listen(5)
    print("Server is listening on port 12345...")

    while True:
        client_socket, addr = server.accept()
        print(f"Connection from {addr} has been established.")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()

