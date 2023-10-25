import random
from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))
print("The server is ready to receive!")

while True:
    rand = random.randint(0, 10)
    message, address = serverSocket.recvfrom(1024)
    message = message.upper()
    print(message)
    print(rand)

    if rand < 4:
        continue

    serverSocket.sendto(message, address)
