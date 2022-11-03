'''
Task 110 (Client)
Seth Maurice-Brant
'''

import socket


host = "127.0.0.1"
port = 65534 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as stream:
    stream.connect((host, port))
    stream.send(b"Client connected") # Send first message to server
    data = stream.recv(1024) # Handle first message (connection initiator)

def SendMessage():
    msg = input("Type here: ")
    stream.send(bytes(("<Client> "+msg),'utf-8'))


def ReceiveMessage():
    data = stream.recv(1024)
    data = data.decode('utf-8')
    print(f"{data}")


SendMessage()
ReceiveMessage()
