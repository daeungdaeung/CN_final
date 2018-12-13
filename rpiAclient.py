from socket import *
import sys

sentence = sys.argv[1]

serverName = '192.168.0.17'
serverPort = 12017
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = sentence
clientSocket.send(sentence.encode())
clientSocket.close()
