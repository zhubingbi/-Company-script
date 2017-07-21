# coding=utf-8

import socket
'''
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(("127.0.0.1", 8000))

sock.listen(5)

content, address = sock.accept()
# content 用来接收客户的消息和发送对该请求用户的消息的功能

print ("%s:%s is connect" % address)
while True:
    sendData = raw_input('>>>')
    content.send(sendData)
    if sendData == 'break':
        break
    recvData = content.recv(512)
    print (recvData)
    if recvData == 'break':
        break
print (content.recv(512))
sock.close()
'''

#udp
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(("127.0.0.1",8000))

data, address = sock.recvfrom(512)

print ('%s:%s is connect' % address)
print (data)
sock.sendto('Hello world!', address)

sock.close()

