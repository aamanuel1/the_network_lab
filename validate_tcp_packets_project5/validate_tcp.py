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

def main():
    filename = "./tcp_data/tcp_addrs_0.txt"

    with open(filename, 'r') as file:
        ip_addr = file.readline().split()

    ip_addr_bytes = []
    for ip in ip_addr:
        ip_addr_bytes.append(ip_addr_to_bytestring(ip))
        
if __name__ == "__main__":
    main()