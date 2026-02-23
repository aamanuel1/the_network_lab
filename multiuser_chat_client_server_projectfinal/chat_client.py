#Final project
#chat_client.py
#Example usage: python chat_client somedude localhost 42069

import sys
import socket
from chatui import init_windows, read_command, print_message, end_windows
import json
import threading

PKT_LEN_SIZE = 2

def usage():
    print("usage: chat_client.py nick host port", file = sys.stderr)

def get_next_packet(socket, buffer):
    data = socket.recv(4096)
    buffer += data

def chat_window(socket, buffer):
    #loop - get packets, extract and parse full message, then print message
    pkt_size = None
    pkt_total_length = None
    while True:
        get_next_packet(socket, buffer)
        if pkt_size is None:
            pkt_size = int.from_bytes(buffer[:PKT_LEN_SIZE], "big")
            pkt_total_length = pkt_size + PKT_LEN_SIZE

        if len(buffer) >= pkt_total_length:
            message = extract_message(buffer, pkt_total_length)

            if message is None:
                continue

            parse_incoming_message(message)
            pkt_size = None
            pkt_total_length = None


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
    print_message(str(message_size))
    message_bytes = message_json.encode()
    message_size_bytes = message_size.to_bytes(PKT_LEN_SIZE, "big")
    message_pkt = bytearray()
    message_pkt.extend(message_size_bytes)
    message_pkt.extend(message_bytes)
    message_pkt = message_size_bytes + message_bytes
    return message_pkt

def extract_message(buffer, msg_length):
    if len(buffer) == 0:
        return None
    
    msg_bytes = buffer[PKT_LEN_SIZE:PKT_LEN_SIZE + msg_length]
    msg = msg_bytes.decode()

    return msg

def parse_incoming_message(message):
    message_json = json.loads(message)
    message_type = message_json["type"]
    sender_nick = message_json["nick"]

    match message_type:
        case "chat":
            chat_message = message_json["chat"]
            print_message(f"{sender_nick}: {chat_message}")
        case "join":
            print_message(f"*** {sender_nick} has joined the chat")
        case "leave":
            print_message(f"*** {sender_nick} has left the chat")


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

    buffer = b''

    init_windows()
    #Start second thread with looping input()
    #Thread args has to be in a tuple for some reason.
    input_thread = threading.Thread(target=chat_window, args=(s, buffer), daemon=True)
    input_thread.start()

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
    
    end_windows()



if __name__ == "__main__":
    sys.exit(main(sys.argv))