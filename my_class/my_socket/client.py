# coding=utf-8
import socket
'''
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(("127.0.0.1",8000))

while True:
    recvData = sock.recv(512)
    print recvData
    if recvData == 'break':
        break
    sendData = raw_input('<<<')
    sock.send(sendData)
    if sendData == 'break':
        break
sock.close()




sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.connect(('127.0.0.1', 8000))

sock.send('在么？')

print sock.recv(512)

sock.close()
'''