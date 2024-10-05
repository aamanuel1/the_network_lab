import socket
import sys
import os

if len(sys.argv) == 1:
    port = 80
else:
    port = int(sys.argv[1])

s = socket.socket()
s.bind(('', port))
s.listen()

while True:
    new_conn = s.accept()
    new_socket = new_conn[0]

    #Parse request header
    raw_request = new_socket.recv(4096)
    print(raw_request)
    request = raw_request.decode("ISO-8859-1")
    eof = request.find("\r\n\r\n") 
    if(eof == -1):
        print("continue")
        continue
    
    header = request.split("\r\n")
    request_method, path, protocol, *others = header[0].split()

    #Strip the path
    path, filename = os.path.split(path)

    #Read and determine data type, then build header content type
    filetype = os.path.splitext(filename)[1]
    content_type = None
    if(filetype == ".txt"):
        content_type = "Content-Type: text/plain\r\n"
    elif(filetype == ".html"):
        content_type = "Content-Type: text/html\r\n"
    elif(filetype == ".jpg" or filetype == ".jpeg"):
        content_type = "Content-Type: image/jpeg\r\n"
    elif(filetype == ".gif"):
        content_type = "Content-Type: image/gif\r\n"
    else:
        content_type = "application/octet-stream\r\n"

    #Read file and append to response
    #Build the response
    data = None
    response = None
    encode_response = None
    encode_response_payload = None
    encode_response_end = None
    try:
        with open(filename, "rb") as fp:
            data = fp.read()
            content_length = len(data)
            response = "HTTP/1.1 200 OK\r\n"\
                    + content_type +\
                    "Content-Length: {}\r\n"\
                    "Connection: close\r\n\r\n".format(content_length, data)
            #Remember that the file is already a bytestream "rb", then append\r\n. 
            encode_response_payload = data
            encode_response_end = "\r\n".encode("ISO-8859-1")
    except Exception as e:
        print(e)
        response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\n"\
        "Content-Length: 13\r\n"\
        "Connection: close\r\n\r\n404 Not Found\r\n\r\n"

    print(response)
    
    encode_response = response.encode("ISO-8859-1")

    #Send response
    new_socket.sendall(encode_response)
    #If it isn't a 404 response, then we need the payload.
    if encode_response_payload is not None:
        new_socket.sendall(encode_response_payload)
        new_socket.sendall(encode_response_end)
    new_socket.close()


