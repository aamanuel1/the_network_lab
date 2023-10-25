import socket
import sys

#Get the website from command line arguments
if len(sys.argv) == 1:
    target = "127.0.0.1"
    port = 20123
else:
    target = sys.argv[1]
    port = 80

#Create the socket and request then encode the request into byte form.
s = socket.socket()
request = "GET / HTTP/1.1\r\nHost: " + target + "\r\nConnection: close\r\n\r\n"
encode_request = request.encode("ISO-8859-1")

#Connect and then send the request
s.connect((target, port))
s.sendall(encode_request)

#Keep receiving bytes from the server until a zero byte array is sent.
while True:
    d = s.recv(4096)
    print(d)
    if len(d) == 0:
        break

s.close()