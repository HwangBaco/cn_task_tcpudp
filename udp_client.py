from socket import *
# ADDR = ('172.16.186.108', 15000) # 차봉
# serverName = '192.168.192.249'
serverName = '172.30.26.100'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
m = input('Input lowercase sentence:')
# clientSocket.sendto(m.encode(), ADDR) # 차봉
clientSocket.sendto(m.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
