import socket
import json
import sys
from threading import Thread

print("######Instructions##############")
print("1:Enter username")
print("2:Enter msg")
print("3:Enter audience 255 for broadcast and 0 to people joined for uni_casting ")

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
name = input("enter your username :")
localIP = "127.0.0.1"
UDPClientSocket.bind((localIP, 20004))

ID=""
def recv():
    stringfull = (name +" : Joined the chat")
    data = json.dumps({"a": stringfull, "b": 255})
    bytesToSend1 = str.encode(data)

    serverAddressPort = ("127.0.0.1", 20001)

    bufferSize = 1024
    UDPClientSocket.sendto(bytesToSend1, serverAddressPort)
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)

    global ID
    ID="{}".format(msgFromServer[0].decode())
    while(1):

     msgFromServer = UDPClientSocket.recvfrom(bufferSize)

     msg = "{}".format(msgFromServer[0].decode())

     print(msg)

Thread(target=recv).start()



while(1):
    msg = input()
    stringfull=("ID:"+ID+"->"+name+":"+msg)
    sendto= input()
    data = json.dumps({"a": stringfull, "b": sendto})
    bytesToSend1 = str.encode(data)

    serverAddressPort = ("127.0.0.1", 20001)

    bufferSize = 1024


    UDPClientSocket.sendto(bytesToSend1, serverAddressPort)

