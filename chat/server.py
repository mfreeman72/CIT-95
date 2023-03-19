# Import needed libraries
import socket
import threading

# Define default ip and port variables
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
port = 54000

# Get port number input from user
port_str = input("Enter the port number you'd like to use (leave blank for 54000): ")

# If the input from user contains a value, set the port number to that value, otherwise use the pre-set value
if port_str != "":
    port = int(port_str)

print(f"\nStarting server on {ip}:{port}")

# Initialize the socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the ip and port numbers
server.bind((ip, port))

# Set the server to listen for clients
server.listen()

# Setup arrays to store client IPs and nicknames
clients = []
nicknames = []


# Broadcast all incoming messages back to all clients
def broadcast(message, current):
    for client in clients:
        if client != current:
            client.send(message)


# Handle for whether or not clients are still connected
def handle(client):
    # Begin loop
    while True:
        # Check whether we are connected to the client and broadcast any received messages
        try:
            message = client.recv(4096)
            broadcast(message, client)
        # Check if client is disconnected
        except:
            # Get index of disconnected client in client list
            index = clients.index(client)
            # Remove the disconnected client
            clients.remove(client)
            # Close the disconnected client
            client.close()
            # Get the disconnected client's nickname
            nickname = nicknames[index]
            # Broadcast that the client has disconnected
            broadcast('{} has left the chat room'.format(nickname).encode('ascii'), client)
            # Remove the disconnected nickname from the list
            nicknames.remove(nickname)
            # End the loop
            break


# Receive new connections from clients
def receive():
    # Begin looping indefinitely
    while True:
        # Accept a new connection
        client, address = server.accept()
        # Print report of new connection to console
        print("Connected with {}".format(str(address)))
        # Send a request for a nickname to the connecting client
        client.send('NICKNAME'.encode('ascii'))
        # Receive nickname
        nickname = client.recv(4096).decode('ascii')
        # Add nickname to the nickname list
        nicknames.append(nickname)
        # Add new client to the client list
        clients.append(client)
        # Print new client's nickname to the console
        print("Nickname is {}".format(nickname))
        # Broadcast to all connected clients about the new client's connection
        broadcast("{} joined!".format(nickname).encode('ascii'), client)
        # Report back to the new client that they have been connected
        client.send('Connected to server!\nBegin conversation:'.encode('ascii'))
        # Add new connection to a thread for multi-threading
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


# Begin receiving clients
receive()
