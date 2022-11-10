'''
Task 110 (Client)
Seth Maurice-Brant
'''

import socket


host = "127.0.0.1"
port = 65534 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as stream:
    stream.connect((host, port))
    
    stream.send(bytes("Hello server, from client",'utf-8'))
    data = stream.recv(1024)
    data = data.decode('utf-8')
    print(f"{data}")
