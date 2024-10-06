#timeclient.py - Queries and compares atomic time from time.nist.gov
#Part of Beej's Guide to Network Concepts, project 3.
import time

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

    #Receive data

    #Decode data

    #Print out NIST's time

    #Print out system time
    pass

if __name__ == '__main__':
    main()