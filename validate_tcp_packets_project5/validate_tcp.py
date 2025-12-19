import sys
import glob, re

def ip_addr_to_bytestring(ip_addr):
    ip_addr_bytes = ip_addr.split(".")

    #Note that the bytestring might need to be turned into hex using
    #bytearray.hex(" ")
    ip_bytestring = bytearray()
    for index, ip_byte in enumerate(ip_addr_bytes):
        ip_byte = int(ip_byte).to_bytes(1, "big")
        ip_bytestring += ip_byte
    return ip_bytestring

def create_ip_pseudoheader(ip_bytestrings, tcp_len_bytestring):
    zero_section = b'\x00'
    protocol = b'\x06'
    ip_pseudoheader = ip_bytestrings[0] + ip_bytestrings[1] + zero_section + protocol + tcp_len_bytestring
    return ip_pseudoheader

def compute_checksum(tcp_ip_pkt):
    offset = 0
    total = 0
    words = []
    while offset < len(tcp_ip_pkt):
        word = tcp_ip_pkt[offset:offset + 2]
        words.append(word)
        offset += 2

    for wd in words:
        total += int.from_bytes(wd)
        #get the ones complement sum and add the carry (carry-around)
        total = (total & 0xffff) + (total >> 16)
    
    #Get the ones complement of the ones complement sum
    checksum = (~total) & 0xffff
    return checksum

def main():

    tcp_addr_filenames = glob.glob('./tcp_data/tcp_addrs_[0-9].txt')
    tcp_addr_filenames.sort()
    # filename = "./tcp_data/tcp_addrs_0.txt"

    for file_no, tcp_addr_file in enumerate(tcp_addr_filenames):
        #Read in the address file, split the address file line in two
        with open(tcp_addr_file, 'r') as file:
            ip_addr = file.readline().split()

        #Change into bytestring
        ip_addr_bytes = []
        for ip in ip_addr:
            ip_addr_bytes.append(ip_addr_to_bytestring(ip))

        filename = "./tcp_data/tcp_data_" + str(file_no) + ".dat"
        with open(filename, 'rb') as fp:
            tcp_data = fp.read()
            tcp_length = len(tcp_data)
            tcp_length_bytestring = bytearray(tcp_length.to_bytes(2, "big"))

        ip_pseudoheader = create_ip_pseudoheader(ip_addr_bytes, tcp_length_bytestring)   
    
        #get the tcp checksum and turn it into a number for comparison
        tcp_checksum = int.from_bytes(tcp_data[16:18], "big")

        #insert 0 in byte 16-17 offset
        tcp_zero_cksum = tcp_data[:16] + b'\x00\x00' + tcp_data[18:]
        
        #pad the packet if it's odd sized
        if len(tcp_zero_cksum) % 2 == 1:
            tcp_zero_cksum += b'\x00'

        #concatenate pseudo header with zeroed TCP data
        zeroed_tcp_ip_pkt = bytearray(ip_pseudoheader + tcp_zero_cksum)

        calc_checksum = compute_checksum(zeroed_tcp_ip_pkt)

        if tcp_checksum == calc_checksum:
            print("PASS")
        else:
            print("FAIL")
        
if __name__ == "__main__":
    main()