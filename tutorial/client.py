#!/usr/bin/env python3

import socket

HOST = '127.0.0.1' # The server's hostname or IP address
PORT = 65432 # The port used by the server

message = input("Type your message:")
message_byte = bytes(message, 'utf-8')

print("1. Creating socket")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
   print("2. Connecting to the server")
   s.connect((HOST, PORT))

   print("3. Sending mesage: " + str(message_byte) +  " to the server")
   s.sendall(message_byte) # send API

   print("4. Receiving message from the server")
   data = s.recv(1024) # store data in the data variable

   print('      Received:', repr(data))

   print("5. Closing the socket")
   s.close()
