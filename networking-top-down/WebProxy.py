from socket import *
import sys

if len(sys.argv) <= 1:
    print('Usage: "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address of Proxy Server]')
    sys.exit(2)

#create a server socker, bind to a port and start listening for connections.
tcpSerSock = socket(AF_INET, SOCK_STREAM)

#TODO: something.

#END TODO

while 1:
    #Start receiving data from client
    print('Ready to serve.')
    tcpClientSock, addr = tcpSerSock.accept()
    print('Received a connection from: ', addr)
    message = "placeholder" #TODO: something.
    print(message)

    #Extract the filename from the message.
    print(message.split()[1])
    filename = message.split()[1].partition("/")[2]
    print(filename)
    fileExist = "false"
    fileToUse = "/" + filename
    print(fileToUse)
    
    try:
        #check wheter the file exists in the cache.
        f = open(fileToUse[1:], "r")
        outputdata = f.readlines()
        fileExist = "true"

        #ProxyServer finds a cache hit and generates response message
        tcpClientSock.send("HTTP/1.0 200 0K\r\n")
        tcpClientSock.send("Content-Type:text/html\r\n")
        #TODO: something.

        #END TODO
        print('Read from cache')

    #Error handling for file not found in cache
    except IOError:
        if fileExist == "false":
            c = "#TODO something"
            hostn = filename.replace("www.", ",", 1)
            print(hostn)
            try:
                #Connect to socket to port 80.
                #TODO: something.

                #END TODO
                #Create a temporary file 
                fileObj = c.makefile('r', 0)
                fileObj.write("GET " + "http://" + filename + "HTTP/1.0\n\n") 
               
                #Read the response into buffer
                #TODO: something.

                #END TODO
               
                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket and the corresponding file in the cach
            except:
                print("Illegal request")

        else:
            # HTTP response message for file not found
            #TODO Fill in start.
            something = "placeholder"
            # Fill in end.


    # Close the client and the server sockets 
    tcpClientSock.close()

#TODO Fill in start.
# Fill in end.
