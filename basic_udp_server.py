import socket 

HOST= "127.0.0.1"
PORT= 8000

server= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((HOST,PORT))
print("UDP server is listening...")

while True:
    data, addr= server.recvfrom(1024)
    print(f"message from {addr}: {data.decode()}")

    server.sendto(b"message received", addr)