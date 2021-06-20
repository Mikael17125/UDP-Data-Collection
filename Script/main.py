#!/usr/bin/env python

import sys
import socket
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP

# Uncomment this if you plan to broadcast from this script
#client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Set the socket to non blocking, allows the program to continue and not wait for data the whole time
client.setblocking(1)

# Bind to all interfaces and to port 2255
client.bind(('', 2255))

def check_data():
    try:
        # Data received
        data, addr = client.recvfrom(1024)
        #print("received message: %s from %s" % (data,addr))

        # return the decoded bytes as a string
        return data.decode()
    # If no data is received just return None
    except socket.error:
        return None

def mergeData(line):
    data = np.array([[float(line[0]),float(line[1]), float(line[2]), float(line[3]), float(line[4]), float(line[5]), float(line[6])]])
    # print(data[0][0])
    return data

def main():

    data_ = np.empty((0,7), np.double)

    counter = 19
    loop = True
    count = False
    enter = 'N'
    startTime = 0
    timeNow = 0
    while True:
        # Check for UDP data
        line = check_data()
        # If there is data split it and print it to console
        if line:
            
            split_line = line.split('|')
            data = mergeData(split_line)
            
            data_ = np.append(data_, data, axis = 0)

            if count is False:
                enter = input("PRESS ENTER")
                startTime = round(time.time())
                count = True
            else:
                timeNow = round(time.time()) - startTime
                if timeNow >= 4:
                    np.savetxt("log"+str(counter)+".csv", data_, delimiter = ',', fmt='%1.3f')
                    data_ = np.empty((0,7), np.double)
                    count = False
                    counter = counter + 1
                
    

if __name__ == '__main__':
    try:
        main()
    # CTRL + C pressed so exit gracefully
    except KeyboardInterrupt:
        print('Interrupted.')
        sys.exit()