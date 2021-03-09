import socket
import sys
from threading import Thread

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
name = input("enter your username :")
localIP = "127.0.0.1"
UDPClientSocket.bind((localIP, 20002))


def recv():
    bytesToSend1 = str.encode(name +" : Joined the chat")
    serverAddressPort = ("127.0.0.1", 20001)

    bufferSize = 1024
    UDPClientSocket.sendto(bytesToSend1, serverAddressPort)
    while(1):

     msgFromServer = UDPClientSocket.recvfrom(bufferSize)

     msg = "{}".format(msgFromServer[0].decode())

     print(msg)

Thread(target=recv).start()



while(1):
    msg = input()
    bytesToSend1 = str.encode(name+":"+msg)

    serverAddressPort = ("127.0.0.1", 20001)

    bufferSize = 1024


    # Create a UDP socket at client side



    # Send to server using created UDP socket

    UDPClientSocket.sendto(bytesToSend1, serverAddressPort)

