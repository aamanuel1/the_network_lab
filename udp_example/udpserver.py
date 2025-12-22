#UDP Server

import sys 
import socket

try:
    port = int(sys.argv[1])
except:
    print("usage: udpserver.py port", file=sys.stderr)
    sys.exit(1)

#make new UDP socket and bind to a port
s = socket.socket(type=socket.SOCK_DGRAM)
s.bind(("", port))

#Loop receiving data
while True:
    #Get data
    data, sender = s.recvfrom(4096)
    print(f"Got data from {sender[0]}:{sender[1]}: \"{data.decode()}\"")

    #Send response back
    s.sendto(f"Got your {len(data)} bytes of data!".encode(), sender)