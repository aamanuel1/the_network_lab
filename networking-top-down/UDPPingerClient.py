from socket import *
import sys
import time

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

message = input('Input a lowercase sentence:')
pings = 10
completed_pings = 0

for i in range(pings):
    ping_start = time.time()
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage = None
    timeout_flag = False
    ping_end = 0
    ping_times = []

    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        ping_end = time.time()
    except:
        TimeoutError()
        timeout_flag = True

    if modifiedMessage is not None:
        rtt = ping_end - ping_start
        print("Ping {:d} {:04.3f}".format(i, rtt))
        print("Message: ", modifiedMessage.decode())
    elif timeout_flag == True:
        print("Request timed out.")
    else:
        print("Another issue.")



clientSocket.close()
