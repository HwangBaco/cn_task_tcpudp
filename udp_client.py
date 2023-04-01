from socket import *
serverName = '<IPv4 Address>'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
m = input('Input lowercase sentence:')
clientSocket.sendto(m.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
