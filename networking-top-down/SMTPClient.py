from socket import *

msg = "\r\n I love computers!"
endmsg = "\r\n.\r\n"

#TODO choose the mailserver.
mailserver = ('smtp.gmail.com', 587)

#Create TCP Socket
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

#Send HELO and print server response.
heloCommand = 'HELO Aaron\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] !='250':
    print('250 reply not received from server')
