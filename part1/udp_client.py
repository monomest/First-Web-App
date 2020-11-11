# -----------------------------------------------------------------
# File: udp_client.py 
# Author: Renee Lu & Arthur Sze
# Last Revised: 11 November 2020
# -----------------------------------------------------------------
# This code creates a UDP client which sends a message to a UDP
# server requesting the list of students and their marks.
# The command string "studentmarklist" is used to query the server.
# ------------------------------------------------------------------

#!/usr/bin/env python3

import socket
import json

HOST = '149.171.36.238' # The server's hostname or IP address (real server: 149.171.36.238) (local: 127.0.0.1)
PORT = 5000  # The port used by the server

message = ('studentmarklist' + '\0')
message_byte = bytes(message, 'utf-8')
encoding = 'utf8'

print("1. Creating socket")
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    print("2. Connecting to the server")
    s.connect((HOST, PORT))

    print("3. Sending mesage: " + str(message_byte) +  " to the server")
    s.sendall(message_byte) # send API

    print("4. Receiving message from the server")
    data = s.recv(1024) # store Byte object data in the data variable
    data_decode = data.decode(encoding) # Decide UTF-8 bytes to Unicode
    print(data_decode)

    print("5. Closing the socket")
    s.close()

