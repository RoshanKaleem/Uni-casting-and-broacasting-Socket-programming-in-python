import socket
import json

localIP = "127.0.0.1"

localPort = 20001

bufferSize = 1024



# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams
clients=[]
j=0
while (True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)


    data = json.loads(bytesAddressPair[0].decode())
    # print(data)
    arr = data.get("a")
    var = data.get("b")

    print(arr)
    print(var)

    address = bytesAddressPair[1]

    check=0
    transverse=0

    for i in clients:
        if(clients[transverse][1]==address):

            check=1
        transverse+=1

    msgFromServer = "to all ->" + arr
    if(check==0):
        clients.append((j, address))

        j += 1
        msgFromServer = str(j-1)
        bytesToSend = str.encode(msgFromServer)
        UDPServerSocket.sendto(bytesToSend, address)
        msgFromServer = "to all->" + arr+" with ID: "+ str(j-1)



    bytesToSend = str.encode(msgFromServer)
    # Broadcasting


    clientIP = "Client IP Address:{}".format(address)
    var=int(var)
    if var in range(0, j):
        msgFromServer = "private/to you: ->" + arr
        bytesToSend = str.encode(msgFromServer)
        UDPServerSocket.sendto(bytesToSend, clients[var][1])
        msgFromServer = "private/from you: ->" + arr
        bytesToSend = str.encode(msgFromServer)
        UDPServerSocket.sendto(bytesToSend, address)


    else:
        x=0
        for i in clients:
            #print(i)
            UDPServerSocket.sendto(bytesToSend, clients[x][1])
            x+=1


