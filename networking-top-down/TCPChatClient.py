from socket import *


def connectSocket(serverName, serverPort):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    return clientSocket

def incomingMessageFromSocket(connectionSocket):
    return connectionSocket.recv(1024).decode()

def outgoingMessageToSocket(connectionSocket, message):
    connectionSocket.send(message.encode())

def main():
    user_1 = input("Hello! Please input your name: ")
    theSocket = connectSocket('localhost', 12000)
    print("The client is ready to send first message")

    #First volley, send user 1 name get user 2 name
    outgoingMessageToSocket(theSocket, user_1)
    user_2 = incomingMessageFromSocket(theSocket)

    while True:
        outgoingMessage = input(user_1 + ": ")
        outgoingMessageToSocket(theSocket, outgoingMessage)
        if outgoingMessage == 'bye':
            break
        incomingMessage = incomingMessageFromSocket(theSocket)
        print(user_2 + ": " + incomingMessage)
        if incomingMessage == 'bye':
            break

    theSocket.close()
    print("Connection closed.")

if __name__ == "__main__":
    main()