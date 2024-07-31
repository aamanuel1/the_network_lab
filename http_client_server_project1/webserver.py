import socket
import sys
import re

if len(sys.argv) == 1:
    port = 80
else:
    port = int(sys.argv[1])

#Bind and listen to connections
s = socket.socket()
s.bind(('', port))
s.listen()

while True:
    #Accept connection and socket
    print('Ready to accept new connection...')
    new_conn = s.accept()
    new_socket = new_conn[0]

    d = new_socket.recv(4096)
    print(d)    #Print request
    eof = re.search("\r\n\r\n", d.decode("ISO-8859-1")) #Find end of request with \r\n\r\n
    print(new_conn[1]) #Print socket info.

    if eof is not None:
        d_str = d.decode("ISO-8859-1")
        if "POST" in d_str:
            print(d_str.split('\r\n\r\n'))
            header, body= d_str.split('\r\n\r\n', 3) #list is [header, body, empty string]
            body_len = str(len(body))

            #Print custom response
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n"\
                    "Content-Length: {}\r\n"\
                    "Connection: close\r\n\r\n{}\r\n\r\n".format(body_len, body)
        else:
            #At the end of the request, send this response. 
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n"\
                    "Content-Length: 6\r\n"\
                    "Connection: close\r\n\r\nHello!\r\n\r\n"
        encode_response = response.encode("ISO-8859-1")
        new_socket.sendall(encode_response)
        new_socket.close()


