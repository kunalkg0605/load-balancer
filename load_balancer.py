import socket
import threading

# List of backend servers
servers = [("localhost", 9001), ("localhost", 9002), ("localhost", 9003)]
current_server = 0

# Function to handle a client connection and forward the request to a backend server
def handle_client(client_socket):
    global current_server
    # Round-robin algorithm to choose a server
    server_address = servers[current_server]
    current_server = (current_server + 1) % len(servers)

    print(f"Forwarding request to server {server_address}")

    # Connect to the selected backend server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(server_address)

    # Forward the client's data to the server
    data = client_socket.recv(1024)
    if data:
        server_socket.sendall(data)

        # Receive the server's response and send it back to the client
        response = server_socket.recv(1024)
        client_socket.sendall(response)

    # Close the connections
    server_socket.close()
    client_socket.close()

# Start the load balancer to listen for clients
def start_load_balancer():
    lb_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lb_socket.bind(('localhost', 8000))
    lb_socket.listen(5)
    print("Load balancer listening on port 8000...")

    while True:
        client_socket, client_address = lb_socket.accept()
        print(f"Connection from {client_address}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()

# Start the load balancer
start_load_balancer()
