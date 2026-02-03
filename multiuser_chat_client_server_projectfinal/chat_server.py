#Final project
#chat_server.py
#Example usage: python chat_server.py 4303

import sys
import socket
import select


def usage():
    print("usage: chat_server.py port", file=sys.stderr)

def run_server(port):
    listener_sock = socket.socket()
    listener_sock.bind(('', port))
    listener_sock.listen

    chatters = set()
    chatters.add(listener_sock)

    # base_packet_buffer = b''

    chat_buffers = dict()

    while True:

        ready_to_read, _, _ = select.select(chatters, {}, {})

        for chatter in ready_to_read:

            if chatter == listener_sock:
                new_chatter = chatter.accept()
                chatters.add(new_chatter[0])
                chat_buffers[new_chatter] = b''

            else:
                get_next_packet(chatter, chat_buffers)


def broadcast_all(sockets, message):
    pass

def get_next_packet(socket, buffers):
    pass

def extract_message(msg):
    pass

def close_conn(socket, buffers):
    pass

def main(argv):
    pass
    

if __name__ == "__main__":
    sys.exit(main(sys.argv))