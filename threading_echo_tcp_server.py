import socket 
import threading

def client_handller(conn:socket.socket, client_addr):
    print(f"client {client_addr} is conected!")

    while True:
        data= conn.recv(1024)
        if not data:
            break
        print(f"client{client_addr}: {data}")
        conn.sendall(data)
    conn.close()
    print(f"{client_addr} disconnected")



HOST= "127.0.0.1"
PORT= 2008

server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print(f"server listening on {HOST}:{PORT}")

while True:
    client_conn, client_addr = server.accept()

    thread = threading.Thread(target=client_handller, args=(client_conn, client_addr))
    thread.start()