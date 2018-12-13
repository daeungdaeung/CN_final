from socket import *
import os

serverPort = 12014
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    print('Completed accepting')
    sentence = connectionSocket.recv(1024).decode()
    print(sentence)
    if sentence == 'turn on':
        os.system('irsend send_once AC on')
        print('AC turned on.')
        os.system('python rpiAclient.py "turn on"')
    elif sentence == 'turn off':
        os.system('irsend send_once AC off')
        print('AC turned off.')
        os.system('python rpiAclient.py "turn off"')
    else:
        print('Not defiend command.')
    connectionSocket.close()
