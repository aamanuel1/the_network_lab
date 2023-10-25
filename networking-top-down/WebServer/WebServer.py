#import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverSocket.bind(('', 80))
serverSocket.listen(1)
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Fill in start #Fill in end
    print(connectionSocket)
    try:
        message =  connectionSocket.recv(1024).decode()#Fill in start #Fill in end
        print(message)
        filename = message.split()[1]
        f = open(filename[1:])

        outputdata = f.read() # Fill in start # Fill in end
        print(outputdata)

        #Send one HTTP header line into socket
        #Fill in start
        outputdataSize = len(outputdata)
        print(outputdataSize)
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n"\
                    "Content-Length: {}\r\n".format(outputdataSize) +\
                    "Connection: close \r\n\r\n"
        print(response)
        connectionSocket.sendall(response.encode())
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        # Fill in start
        errorMessage = f"""HTTP/1.1 404 Not Found\r\nContent-Type: text/html
        Content-Length: 206
        Connection: close\r\n
        <!DOCTYPE html>
        <html>
        <head>
        <title>404 Not Found</title>
        </head>
        <body>

        <p>404 Not Found</p>
        </body>
        </html>
        \r\n"""
        print(errorMessage)
        connectionSocket.sendall(errorMessage.encode())
        # Fill in end

        #Close client socket
        # Fill in start
    connectionSocket.close()
        # Fill in end
serverSocket.close()

