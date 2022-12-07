import socket
import threading

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    while True:
        client_connection, _ = server_socket.accept()  # wait for client
        thread = threading.Thread(target=handle_connection, args=(client_connection,))
        thread.start()
    
def handle_connection(client_connection):
    while True:
        try:
            client_connection.recv(1024) # wait for client to send data
            client_connection.send(b"+PONG\r\n")
        except ConnectionError:
            break
	
if __name__ == "__main__":
    main()
