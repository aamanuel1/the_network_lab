import sys

def main():
    filename = "./tcp_data/tcp_addrs_0.txt"

    with open(filename, 'r') as file:
        ip_addr = file.readline().split()

    ip_addr_bytes = []
    for ip in ip_addr:
        print(ip)
        subnet_bytes = ip.split(".")
        ip_bytestring = bytearray()
        for index, ip_byte in enumerate(subnet_bytes):
            ip_byte = int(ip_byte)
            ip_byte = ip_byte.to_bytes(1, "big")
            ip_bytestring += ip_byte
        # ip_addr_bytes.append(subnet_bytes)
        print(ip_bytestring.hex(" "))
        ip_addr_bytes
        print(ip_addr_bytes)
        
        

if __name__ == "__main__":
    main()