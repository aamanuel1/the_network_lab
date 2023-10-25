import socket
import sys
import re

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

response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n"\
            "Content-Length: 6\r\n"\
            "Connection: close\r\n\r\nHello!\r\n\r\n"
encode_response = response.encode("ISO-8859-1")

while True:
    d = new_socket.recv(4096)
    print(d)
    eof = re.search("\r\n\r\n", d.decode("ISO-8859-1"))
    if eof is not None:
        new_socket.sendall(encode_response)
        new_socket.close()
        new_conn = s.accept()
        new_socket = new_conn[0]

