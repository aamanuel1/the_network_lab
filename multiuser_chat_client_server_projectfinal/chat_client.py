#Final project
#chat_client.py
#Example usage: python chat_client somedude localhost 42069

import sys
import socket
from chatui import init_windows, read_command, print_message, end_windows

def usage():
    print("usage: chat_client.py nick host port", file = sys.stderr)

def get_next_packet():
    pass

def chat_window():
    #loop - get packets, extract and parse full message, then print message
    pass

def create_hello_message():
    pass

def create_chat_message():
    pass

def extract_message():
    pass

def parse_message():
    pass

def broadcast_message():
    pass

def close_conn():
    pass

def main(argv):
    try:
        nick = argv[1]
        host = argv[2]
        port = int(argv[3])
    except:
        usage()
        return 1
    
    #Connect to socket


    #Start second thread with looping input()


    #Create and send hello message

    
    #Main input loop - get message from user, package it into packets and send it 



if __name__ == "__main__":
    sys.exit(main(sys.argv))