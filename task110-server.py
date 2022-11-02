'''
Task 110 (Server)
Seth Maurice-Brant
'''

import socket

host = "127.0.0.1"
port = 65534

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as stream:
    stream.bind((host,port))
    stream.listen()
    conn, addr = stream.accept()
    with conn:
        print(f"Connected to {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
