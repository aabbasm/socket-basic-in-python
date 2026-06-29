import socket

HOST = "127.0.0.1"
PORT = 2008

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

client_socket.sendall(b"Hello server, im basic clinet, nice to meet you!")

data = client_socket.recv(1024)
print("Received:", data.decode())

