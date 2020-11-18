# -----------------------------------------------------------------
# File: udp_client.py 
# Author: Renee Lu & Arthur Sze
# Last Revised: 11 November 2020
# -----------------------------------------------------------------
# This code creates a UDP client which sends a message to a UDP
# server requesting the list of students and their marks. 
# It takes this information and stores it in a JSON file.
# The command string "studentmarklist" is used to query the server.
# ------------------------------------------------------------------

#!/usr/bin/env python3

import socket   # Library for socket connectioms
import json     # Library for encoding into JSON format
import re       # Library for regex applications

# The server's hostname or IP address
# Actual server: 149.171.36.238
# Local server: 127.0.0.1
HOST = '149.171.36.238' 

# The port used by the server
PORT = 5000

# Setting command string
encoding = 'utf-8'
message = ('studentmarklist' + '\0')
message_byte = bytes(message, encoding)

# JSON output file name
out_name = 'student-data-original.json' 

print()
print("----------- Querying Server -----------")
print()
print("1. Creating UDP socket")
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    print("2. Connecting to the server")
    s.connect((HOST, PORT))

    print("3. Sending mesage: " + str(message_byte) +  " to the server")
    s.sendall(message_byte) # Send API

    print("4. Receiving and formattting message from the server")
    data = s.recv(1024)     # Store Byte object data in the data variable
    print("   Message received:")
    print(repr(data))
    print()
    print("5. Closing the socket")
    s.close()

print()
print("----------- Writing to database -----------")
print()
print("6. Decoding and formatting data")

# Decode UTF-8 data to Unicode
data_decode = data.decode(encoding)

# Retrieve number of students from data
num_students = int(data_decode[:4])

# Remove number of students from the data
data_decode = data_decode[4:]

# Separate students by whitespace
data_spaced = re.sub(r"([0-9]+(\.[0-9]+)?)",r"-\1 ",
              data_decode).strip()
print("   Formatted data:")
print(data_spaced)
print()
print("7. Converting data into JSON format")

# Create list of students and their marks
student_list = data_spaced.split(" ")

# Dictionary of students used to create JSON file
student_dict = {}

# Fields in database
fields = ['studentname', 'studentmark']

# Populate the student dictionary
for student in student_list:
    
    # Dictionary to store current student's details
    # to append to the overall student dictionary
    current_student = {}
    
    # List of current student's details
    student_details = student.split("-")
    
    # Populating the current student's dictionary
    # Index 0 = studentname (string with Unicode NULL removed)
    # Index 1 = studentmark (integer)
    student_name = student_details[0].rstrip('\u0000')
    current_student[fields[0]] = student_name 
    current_student[fields[1]] = int(student_details[1])

    # Appending the record of the current student to 
    # the main student dictionary. 
    # Identified by student name.
    student_dict[student_name] = current_student

print("8. Creating the JSON file " + out_name)

# Write the contents of the student dictionary
# into JSON format with the file name given
# by the variable defined at the beginning 'out_name'
out_file = open(out_name, "w")
json.dump(student_dict, out_file, indent = 4)
out_file.close()
print()
print('----------- SUCCESS! -----------')
print("To see the database, open " + out_name)
