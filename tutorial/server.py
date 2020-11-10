#!/usr/bon/env python3

import socket

HOST = '127.0.0.1' # localhost
PORT = 65432 # Port to listen on (non-privileged ports are > 1023)

# 1. Create a socket
print("1. Creating a socket")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creates socket object s using ipv4 and TCP

# 2. Bind the created socket with a specific network interface and port number
print("2. Binding the socket with HOST:" + HOST + " at PORT:" + str(PORT))
s.bind((HOST, PORT)) # bind is a method of the socket object

# 3. Listen for connection, allowing a server to accept the connection
print("3. Listening for a connection")
s.listen()

# Loop until break
while True:
   # 4. Wait for incoming connection, when a client connects it returns a new socket object
   print("4. Waiting for incoming connection ......")
   conn, addr = s.accept() # conn represents the connection, addr is for address is a tuple containing host and port number of client

   with conn:
      print('Connected by', addr)

      data = conn.recv(1024)
      print("5. Received data: " + str(data))

      print("6. Replying with: " + str(data)) # Echo back the message it receives
      conn.sendall(data)

      if data == b'CLOSE': # if message received is 'CLOSE', close the API call
         print("7. Closing the socket")
         s.close()
         break
