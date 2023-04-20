import socket

HOST = 'socket.cryptohack.org'
PORT = 13377

# Connect to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Receive data from the server
data = s.recv(1024)
print(data.decode())

# Send data to the server
s.sendall(b"Hello, server!")

# Receive more data from the server
data = s.recv(1024)
print(data.decode())

# Close the connection
s.close()
