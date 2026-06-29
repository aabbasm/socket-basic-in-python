import socket

HOST= "127.0.0.1"
PORT= 2008

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_sock.bind((HOST, PORT))

server_sock.listen(1)
print(f"server listen on {HOST}:{PORT}")

client_socket, client_addr= server_sock.accept()
print(f"conection from {client_addr}")

data= client_socket.recv(1024)
print(f"resiced: ", data.decode())

client_socket.sendall(b"hello client")
client_socket.close()
print(f"clinet {client_addr} disconnected")
server_sock.close()
print(f"server is down!")
