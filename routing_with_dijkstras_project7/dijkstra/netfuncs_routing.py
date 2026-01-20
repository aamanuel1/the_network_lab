import sys
import json

def ipv4_to_value(ipv4_addr):
    """
    Convert a dots-and-numbers IP address to a single 32-bit numeric
    value of integer type. Returns an integer type.

    Example:

    ipv4_addr: "255.255.0.0"
    return:    4294901760  (Which is 0xffff0000 hex)

    ipv4_addr: "1.2.3.4"
    return:    16909060  (Which is 0x01020304 hex)
    """
    ipv4_addr_list = ipv4_addr.split(".")
    value = 0
    mult = 24
    for v in ipv4_addr_list:
        value = value | (int(v) << mult)
        mult = mult - 8

    return value

def value_to_ipv4(addr):
    """
    Convert a single 32-bit numeric value of integer type to a
    dots-and-numbers IP address. Returns a string type.

    Example:

    There is only one input value, but it is shown here in 3 bases.

    addr:   0xffff0000 0b11111111111111110000000000000000 4294901760
    return: "255.255.0.0"

    addr:   0x01020304 0b00000001000000100000001100000100 16909060
    return: "1.2.3.4"
    """

    ip_v4_string = []
    shift_by = 24
    ip_numbers = range(4)
    for i in ip_numbers:
        ip_number = (addr >> shift_by) & 255
        ip_v4_string.append(str(ip_number))
        shift_by -= 8

    return ".".join(ip_v4_string)

def get_subnet_mask_value(slash):
    """
    Given a subnet mask in slash notation, return the value of the mask
    as a single number of integer type. The input can contain an IP
    address optionally, but that part should be discarded.

    Returns an integer type.

    Example:

    There is only one return value, but it is shown here in 3 bases.

    slash:  "/16"
    return: 0xffff0000 0b11111111111111110000000000000000 4294901760

    slash:  "10.20.30.40/23"
    return: 0xfffffe00 0b11111111111111111111111000000000 4294966784
    """

    ip, subnet, *_ = slash.split("/")
    #Run of 1s by bitshift left the count then rolling back by 1
    subnet_mask = (1 << (int(subnet))) - 1
    host = 32 - int(subnet)
    #Then get subnet mask by bitshift left the host value (32-subnet slash)
    subnet_mask = subnet_mask << host
    return subnet_mask 

def ips_same_subnet(ip1, ip2, slash):
    """
    Given two dots-and-numbers IP addresses and a subnet mask in slash
    notation, return true if the two IP addresses are on the same
    subnet.

    Returns a boolean.

    FOR FULL CREDIT: this must use your get_subnet_mask_value() and
    ipv4_to_value() functions. Don't do it with pure string
    manipulation.

    This needs to work with any subnet from /1 to /31

    Example:

    ip1:    "10.23.121.17"
    ip2:    "10.23.121.225"
    slash:  "/23"
    return: True
    
    ip1:    "10.23.230.22"
    ip2:    "10.24.121.225"
    slash:  "/16"
    return: False
    """
    ip_subnet_mask = get_subnet_mask_value(slash)
    ip1_network_num = ipv4_to_value(ip1) & ip_subnet_mask
    ip2_network_num = ipv4_to_value(ip2) & ip_subnet_mask
    
    if ip1_network_num == ip2_network_num:
        return True

    return False

def get_network(ip_value, netmask):
    """
    Return the network portion of an address value as integer type.

    Example:

    ip_value: 0x01020304
    netmask:  0xffffff00
    return:   0x01020300
    """

    return ip_value & netmask

def find_router_for_ip(routers, ip):
    """
    Search a dictionary of routers (keyed by router IP) to find which
    router belongs to the same subnet as the given IP.

    Return None if no routers is on the same subnet as the given IP.

    FOR FULL CREDIT: you must do this by calling your ips_same_subnet()
    function.

    Example:

    [Note there will be more data in the routers dictionary than is
    shown here--it can be ignored for this function.]

    routers: {
        "1.2.3.1": {
            "netmask": "/24"
        },
        "1.2.4.1": {
            "netmask": "/24"
        }
    }
    ip: "1.2.3.5"
    return: "1.2.3.1"


    routers: {
        "1.2.3.1": {
            "netmask": "/24"
        },
        "1.2.4.1": {
            "netmask": "/24"
        }
    }
    ip: "1.2.5.6"
    return: None
    """

    router_same_subnet = None
    for router, netmask in routers.items():
        if ips_same_subnet(ip, router, netmask.get("netmask")):
            router_same_subnet = router
    return router_same_subnet


def main(argv):
    pass

if __name__ == "__main__":
    sys.exit(main(sys.argv))
    
