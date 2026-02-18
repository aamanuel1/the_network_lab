#Final project
#chat_client.py
#Example usage: python chat_client somedude localhost 42069

import sys
import socket
from chatui import init_windows, read_command, print_message, end_windows
import json

PKT_LEN_SIZE = 2

def usage():
    print("usage: chat_client.py nick host port", file = sys.stderr)

def get_next_packet(socket, buffer):
    data = socket.recv(4096)
    buffer[socket] += data

def chat_window():
    #loop - get packets, extract and parse full message, then print message
    pass

def create_hello_message(nick):
    hello_message_dict = {
        "type": "hello",
        "nick": f"{nick}"
    }
    hello_pkt = create_pkt(hello_message_dict)
    return hello_pkt

def create_chat_message(message):
    chat_message_dict = {
        "type": "chat",
        "message": f"{message}"
    }
    chat_pkt = create_pkt(chat_message_dict)
    return chat_pkt

def create_pkt(message_dict):
    message_json = json.dumps(message_dict)
    print_message(message_json)
    message_size = len(message_json)
    message_bytes = message_json.encode()
    message_size_bytes = message_size.to_bytes(PKT_LEN_SIZE, "big")
    message_pkt = message_size_bytes + message_bytes
    return message_pkt

def extract_message():
    pass

def parse_message():
    pass

def parse_special_input(command, sock):
    if command.strip() == "\\q":
        close_conn(sock)
        exit(0)

def broadcast_message():
    pass

def close_conn(sock):
    sock.close()

def main(argv):
    try:
        nick = argv[1]
        host = argv[2]
        port = int(argv[3])
    except:
        usage()
        return 1
    
    #Connect to socket
    s = socket.socket()
    s.connect((host, port))


    #Start second thread with looping input()


    #Create and send hello message
    hello_message_pkt = create_hello_message(nick)
    s.sendall(hello_message_pkt)
    # print_message(str(hello_message_pkt))
    
    #Main input loop - get message from user, package it into packets and send it 
    while True:
        try:
            command = read_command(f"{nick}> ")
        except:
            break

        if command == "":
            continue

        if command[0] == "\\":
            parse_special_input(command, s)

        chat_message_pkt = create_chat_message(command)
        s.sendall(chat_message_pkt)
        # print_message(str(chat_message_pkt))



if __name__ == "__main__":
    sys.exit(main(sys.argv))