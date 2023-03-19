# Import needed libraries
import socket
import threading
import os

# Define default nickname, ip, and port variables
default_name = socket.gethostname()  # This gets the hostname of the computer the client is running on
hostname = socket.gethostname()
ip = socket.gethostbyname(default_name)
port = 54000

# Get IP, Port number, and Nickname input from user
ip_text = "Enter the IP address of the server (leave blank for " + ip + "): "
ip_str = input(ip_text)
port_str = input("Enter the port the server is running on (leave blank for 54000): ")
nick_text = "Enter your nickname (leave blank for \"" + default_name + "\"): "
nickname = input(nick_text)

# Check all inputs. If any are blank, set value to default
if ip_str != "":
    ip = ip_str
if port_str != "":
    port = int(port_str)
if nickname == "":
    nickname = default_name

# Append brackets to the nickname for chat tags
nickname = '[' + nickname + ']'

# Initialize the socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the connection as the given ip and port number
client.connect((ip, port))


# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Receive messages from server
def receive():
    # Begin loop
    while True:
        # Attempt to receive from the server
        try:
            # Receive message from server
            message = client.recv(4096).decode('ascii')
            # If message is a nickname request, send the nickname
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            else:
                # Print the message to the console
                print(message)
        # Print error if unable to receive
        except:
            print("An error occurred!")
            client.close()
            break


# Get new message from user
def write():
    # Begin loop
    while True:
        # Get the message input from the user and format it with the nickname tag at the front
        message = '{} {}'.format(nickname, input(''))
        # Send the message to the server
        client.send(message.encode('ascii'))


clear_screen()

# Begin the receiving thread, targeting the "receive" function
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# Begin the sending thread, targeting the write function
write_thread = threading.Thread(target=write)
write_thread.start()
