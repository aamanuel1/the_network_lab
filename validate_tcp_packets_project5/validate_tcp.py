import sys

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
    print(ip_pseudoheader)
    return ip_pseudoheader

def main():
    filename = "./tcp_data/tcp_addrs_0.txt"

    #Read in the address file, split the address file line in two
    with open(filename, 'r') as file:
        ip_addr = file.readline().split()

    #Change into bytestring
    ip_addr_bytes = []
    for ip in ip_addr:
        ip_addr_bytes.append(ip_addr_to_bytestring(ip))
    
    filename = "./tcp_data/tcp_data_0.dat"
    with open(filename, 'rb') as fp:
        tcp_data = fp.read()
        tcp_length = len(tcp_data)
        tcp_length_bytestring = bytearray(tcp_length.to_bytes(2, "big"))

    print(tcp_length)
    print(tcp_length_bytestring)
    
    ip_pseudoheader = create_ip_pseudoheader(ip_addr_bytes, tcp_length_bytestring)


        
if __name__ == "__main__":
    main()