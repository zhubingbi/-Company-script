#coding=utf-8
import SocketServer
import threading

'''
class MyHandle(SocketServer.BaseRequestHandler):
    """
    重新定义一个句柄
    """
    def setup(self):
        print ('This is our server')

    def handle(self):
        """
        处理socket请求
        self.requset
        self.client_address
        self.server
        :return:
        """
        print ('%s:%s is connect' % self.client_address)
        content = self.request
        recvData = content.recv(512)
        print recvData
        content.send(recvData.upper())

    def finish(self):
        print ('server is connected')


if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1', 8000), MyHandle)
    # server.server_forever 开启服务
    server_thread = threading.Thread(target = server.serve_forever())
    server_thread.start()
    print ('%s is start' % server_thread.name)
'''

class MyHandle(SocketServer.BaseRequestHandler):
    """
    重新定义一个句柄
    """
    def setup(self):
        print ('This is our server')

    def handle(self):
        """
        处理socket请求
        self.requset
        self.client_address
        self.server
        :return:
        """
        print ('%s:%s is connect' % self.client_address)
        content = self.request
        recvData = content.recv(512)
        print recvData
        content.send(recvData.upper())

    def finish(self):
        print ('server is connected')


class OurServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """
        threadingMixIn 让服务拥有多线程特新
        tcpServer tcp服务
        tcp 多线程服务
        继承顺序不可以改
    """
    pass


if __name__ == '__main__':
    server = OurServer(('127.0.0.1', 8000), MyHandle)
    # server.server_forever 开启服务
    server_thread = threading.Thread(target=server.serve_forever())
    server_thread.start()
    print ('%s is start' % server_thread.name)