# Example usage:
#
# python select_server.py 3490

import sys
import socket
import select

def run_server(port):
    listener_sock = socket.socket()
    listener_sock.bind(('', port))
    listener_sock.listen()

    read_set = set()
    read_set.add(listener_sock)

    while True:

        ready_to_read, _, _ = select.select(read_set, {}, {})

        for the_socket in ready_to_read:

            if the_socket == listener_sock:
                new_socket = the_socket.accept()
                #You want to avoid using a tuple otherwise select doesn't think it has a fileno
                read_set.add(new_socket[0])
                print(f'{new_socket[1]}: connected')
                the_socket.listen()
            else:
                raw_data = the_socket.recv(4096)

                if len(raw_data) == 0:
                    #The socket is not subscriptable so you have to use getpeername() instead.
                    print(f'{the_socket.getpeername()}: disconnected')
                    read_set.remove(the_socket)
                else:
                    data_len = len(raw_data)
                    data = raw_data.decode()
                    print(f'{the_socket.getpeername()} {data_len} bytes: {data}')

#--------------------------------#
# Do not modify below this line! #
#--------------------------------#

def usage():
    print("usage: select_server.py port", file=sys.stderr)

def main(argv):
    try:
        port = int(argv[1])
    except:
        usage()
        return 1

    run_server(port)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
