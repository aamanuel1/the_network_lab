#Final project
#chat_server.py
#Example usage: python chat_server.py 4303

import sys
import socket
import select
import json

PKT_LEN_SIZE = 2


def usage():
    print("usage: chat_server.py port", file=sys.stderr)

def get_next_packet(socket, buffers):
    data = socket.recv(4096)

    # if data == b'':
    #     close_conn(socket, buffers)

    buffers[socket] += data


def run_server(port):
    listener_sock = socket.socket()
    listener_sock.bind(('', port))
    listener_sock.listen()

    chatters_sock = set()
    chatters_sock.add(listener_sock)
    chatters_name = dict()

    # base_packet_buffer = b''

    chat_buffers = dict()

    while True:

        ready_to_read, _, _ = select.select(chatters_sock, {}, {})

        for chatter_sock in ready_to_read:

            if chatter_sock == listener_sock:
                new_chatter = chatter_sock.accept()
                chatters_sock.add(new_chatter[0])
                chat_buffers[new_chatter[0]] = b''
                chatter_sock.listen()

            else:
                get_next_packet(chatter_sock, chat_buffers)
                pkt_size = int.from_bytes(chat_buffers[chatter_sock][:PKT_LEN_SIZE], "big")
                pkt_total_length = pkt_size + PKT_LEN_SIZE

                if len(chat_buffers[chatter_sock]) >= pkt_total_length:
                    # message_pkt = chat_buffers[chatter][:pkt_total_length]
                    chat_buffers[chatter_sock] = chat_buffers[chatter_sock][pkt_total_length:]
                    
                    message = extract_message(chat_buffers[chatter_sock], pkt_total_length)
                    if message is None:
                        continue
                    response, size = parse_incoming_message(chatter_sock, chatters_name, message)

                    response_pkt = size.to_bytes(PKT_LEN_SIZE, "big") + response.encode()
                    broadcast_all(chatters_sock, response_pkt)

                if len(chat_buffers[chatter_sock]) == 0:
                    response_pkt = close_conn(chatter_sock, chatters_name)
                    chatters_sock.remove(chatter_sock)
                    chatters_name.remove(chatter_sock)
                    broadcast_all(chatters_sock, response_pkt)

def broadcast_all(sockets, packet):
    
    for chatter in sockets:
        chatter.sendall(packet)


def extract_message(chat_buffer, msg_length):

    if len(chat_buffer) == 0:
        return None
    
    msg_bytes = chat_buffer[PKT_LEN_SIZE:PKT_LEN_SIZE + msg_length]
    msg = msg_bytes.decode()

    return msg

def parse_incoming_message(chatter_sock, chatters_name, message_full_payload):
    #TODO test message forming.
    message_json = json.loads(message_full_payload)
    message_type = message_json["type"]
    response = ""
    size = 0

    match message_type:
        case "hello":
            nick = message_json["nick"]
            size, response = create_join_message(nick)
            chatters_name[chatter_sock] = nick
        case "chat":
            nick = message_json["nick"]
            message = message_json["message"]
            size, response = create_chat_message(nick, message)
    response_bytes = response.encode()
    size_bytes = size.to_bytes(PKT_LEN_SIZE, "big")
    return response_bytes, size_bytes

def create_join_message(chatter_name):
    join_message_dict = {
        "type": "join",
        "nick": f"{chatter_name}"
    }
    join_message_json = json.dumps(join_message_dict)
    return len(join_message_json), join_message_json

def create_chat_message(chatter_name, message):
    chat_message_dict = {
        "type": "chat",
        "nick": f"{chatter_name}",
        "message": f"{message}"
    }
    chat_message_json = json.dumps(chat_message_dict)
    return len(chat_message_json), chat_message_json

def create_leave_message(chatter_name):
    leave_message_dict = {
        "type": "leave",
        "nick": f"{chatter_name}"
    }
    leave_message_json = json.dumps(leave_message_dict)
    return len(leave_message_json), leave_message_json

def close_conn(socket, names):
    name = names[socket]
    message_size, message = create_leave_message(name)
    message_size_bytes = message_size.to_bytes(PKT_LEN_SIZE, "big")
    message_bytes = message.encode()
    close_conn_pkt = message_size_bytes + message_bytes
    return close_conn_pkt

def main(argv):
    try:
        port = int(argv[1])
    except:
        usage()
        return 1
    
    run_server(port)

if __name__ == "__main__":
    sys.exit(main(sys.argv))