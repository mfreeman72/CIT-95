import socket
import os
from _thread import *



# Create socket connection
ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0

# Bind the host and port to the socket
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(5)

# Function to handle client threads


def multi_threaded_client(connection):
    connection.sendall(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048)
        print(data.decode('utf-8'))
        response = 'Server message: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(response))
    connection.close()


# Loop to maintain server connection
while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()