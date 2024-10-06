#timeclient.py - Queries and compares atomic time from time.nist.gov
#Part of Beej's Guide to Network Concepts, project 3.
import time
import socket

def system_seconds_since_1900():
    """
    The time server returns the number of seconds since 1900, but Unix
    systems return the number of seconds since 1970. This function
    computes the number of seconds since 1900 on the system.
    """
    # Number of seconds between 1900-01-01 and 1970-01-01
    seconds_delta = 2208988800
    seconds_since_unix_epoch = int(time.time())
    seconds_since_1900_epoch = seconds_since_unix_epoch + seconds_delta

    return seconds_since_1900_epoch

def main():
    #Connect to the server
    #Form request
    target = "time.nist.gov"
    port = 37
    request = "GET / HTTP/1.1\r\nHost: " + target + "\r\nConnection: close\r\n\r\n"
    encoded_request = request.encode("ISO-8859-1")

    s = socket.socket()
    s.connect((target, port))
    s.sendall(encoded_request)
    
    #Receive data
    nist_time_bytes = s.recv(4096)

    #Decode data
    nist_time = int.from_bytes(nist_time_bytes, "big")

    #Print out NIST's time
    print("NIST time\t: {}".format(nist_time))

    #Print out system time
    system_time = system_seconds_since_1900()
    print("System time\t: {}".format(system_time))

if __name__ == '__main__':
    main()