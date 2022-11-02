'''
Task 110
Seth Maurice-Brant
'''
import socket

tcp_ip = "127.0.0.1"
tcp_port = 5669

def Server():
    buffer_size = 20
    stream = socket.socket(socket.SOCK_STREAM)
    stream.bind(tcp_ip+ str(tcp_port))
    stream.listen(1)

    conn, addr = stream.accept()
    print(addr)
    while 1:
        data = conn.recv(buffer_size)
        if not data:
            break
        print(data)
        conn.send("Hello client, from server") # Replace with server response later
    conn.close()

def Client():
    message = "Hello server, from client"
    buffer_size = 1024
    stream = socket.socket(socket.AF_INET, socket.SOCK_SREAM)
    stream.connect(tcp_ip+ str(tcp_port))
    stream.send(message)
    data = stream.recv(buffer_size)
    stream.close()
    print(data)


mode = input("Is this a [s]erver or a [c]lient?")
if mode == "s":
    Server()
if mode == "c":
    Client()
else:
    print("Invalid entry.")

