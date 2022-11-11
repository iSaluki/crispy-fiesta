'''
Task 110 (Server)
Seth Maurice-Brant
'''

import socket

host = "10.25.5.80"
port = 80

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as stream:
    stream.bind((host,port))
    stream.listen(1)
    conn, addr = stream.accept()
    with conn:
        print(f"Connected to {addr}")
        data = conn.recv(1024)
        data = data.decode("utf-8")
        print(f"{data}")
        conn.send(bytes(("Hello client, from server"),'utf-8'))

          
