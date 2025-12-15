import sys
import socket

# How many bytes is the word length?
WORD_LEN_SIZE = 2

def usage():
    print("usage: wordclient.py server port", file=sys.stderr)

packet_buffer = b''

def get_next_word_packet(s):
    """
    Return the next word packet from the stream.

    The word packet consists of the encoded word length followed by the
    UTF-8-encoded word.

    Returns None if there are no more words, i.e. the server has hung
    up.
    """

    global packet_buffer

    # DONE -- Write me!
    word_size = 0
    packet = b''
    is_connection_closed = False
    while True:

        if is_connection_closed is False:
            data = s.recv(4096)
        
        if data == b'':
            is_connection_closed = True
        
        if len(data) != 0:
            packet_buffer += data

        if word_size == 0:
            word_size = int.from_bytes(packet_buffer[:WORD_LEN_SIZE], "big")

        packet_size = word_size + WORD_LEN_SIZE

        if len(packet_buffer) >= packet_size:
            packet = packet_buffer[:packet_size]
            packet_buffer = packet_buffer[packet_size:]
            word_size = 0
            return packet

        #If length of the data is 0 (no length) then flag as complete
        #We should have sent the last packet before getting here.
        if len(packet_buffer) == 0:
            return None
        


def extract_word(word_packet):
    """
    Extract a word from a word packet.

    word_packet: a word packet consisting of the encoded word length
    followed by the UTF-8 word.

    Returns the word decoded as a string.
    """

    # DONE -- Write me!
    word_len_bytes = word_packet[:WORD_LEN_SIZE]
    word_len = int.from_bytes(word_len_bytes, "big")
    word_bytes = word_packet[WORD_LEN_SIZE:]
    word = word_bytes.decode()

    return word

# Do not modify:

def main(argv):
    try:
        host = argv[1]
        port = int(argv[2])
    except:
        usage()
        return 1

    s = socket.socket()
    s.connect((host, port))

    print("Getting words:")

    while True:
        word_packet = get_next_word_packet(s)

        if word_packet is None:
            break

        word = extract_word(word_packet)

        print(f"    {word}")

    s.close()

if __name__ == "__main__":
    sys.exit(main(sys.argv))
