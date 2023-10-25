from socket import *

def welcomeSocket(serverPort):
    welcomeSocket = socket(AF_INET, SOCK_STREAM)
    welcomeSocket.bind(('', serverPort))
    welcomeSocket.listen(1)
    print("The chat server is ready to receive!")
    return welcomeSocket

def incomingMessageFromSocket(connectionSocket, addr):
    return connectionSocket.recv(1024).decode()

def outgoingMessageToSocket(connectionSocket, addr, message):
    connectionSocket.send(message.encode())


def main():
    user_2 = input("Hello! Please input your name: ")
    serverSocket = welcomeSocket(12000)
    connectionSocket, addr = serverSocket.accept()

    #First volley, get user 1 name send user 2 name
    user_1 = incomingMessageFromSocket(connectionSocket, addr)
    outgoingMessageToSocket(connectionSocket, addr, user_2)

    while True:
        print(user_1 + ":", end=" ")
        incomingMessage = incomingMessageFromSocket(connectionSocket, addr)
        print(incomingMessage)
        if incomingMessage == 'bye':
            break
        incomingMessage = ""
        outgoingMessage = input(user_2 + ": ")
        outgoingMessageToSocket(connectionSocket, addr, outgoingMessage)
        if outgoingMessage == 'bye':
            break

    connectionSocket.close()
    print("Connection closed.")


if __name__ == "__main__":
    main()