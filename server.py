import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an address and port
server_socket.bind(('localhost', 9001))

# Listen for incoming connections
server_socket.listen(1)
print("Server is listening on port 9001...")

# Accept a connection from a client
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

# Receive data from the client
data = client_socket.recv(1024)
print(f"Received data: {data.decode()}")

# Send a response to the client
client_socket.send(b"Hello from server1!")

# Close the connection
client_socket.close()
server_socket.close()
