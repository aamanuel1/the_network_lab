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

new_conn = s.accept()
new_socket = new_conn[0]
print(new_conn)


while True:
    response = None
    encode_response = None

    #Parse request header
    raw_request = new_socket.recv(4096)
    print(raw_request)
    # eof = re.search("\r\n\r\n", d.decode("ISO-8859-1"))
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
    filetype = os.path.splitext(path)
    content_type = None
    if(filetype == ".txt"):
        content_type = "Content-Type: text/plain\r\n"
    elif(filetype == ".html"):
        content_type = "Content-Type: text/html\r\n"

    #Read file and append to response
    #Build the response
    data = None
    try:
        with open(filename, "rb") as fp:
            data = fp.read()
            content_length = data.len()
            response = "HTTP/1.1 200 OK\r\n"\
                    + content_type +\
                    "Content-Length: {}\r\n".format(content_length) +\
                    "Connection: close \r\n" +\
                    data + "\r\n"
    except:
        response = "HTTP/1.1 404 Not Found\r\nContent-Type:text/plain\r\n"\
        "Content-Length: 13\r\n"\
        "Connection: close\r\n\r\n"

    print(response)
    
    encode_response = response.encode("ISO-8859-1")

    #Send response
    new_socket.sendall(encode_response)
    new_socket.close()
    new_conn = s.accept()
    new_socket = new_conn[0]

