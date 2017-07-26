#!/usr/bin/python
# coding=utf-8
import SocketServer
import os
from module import Upload
from module import Download


class MyServer(SocketServer.BaseRequestHandler):
    def handle(self):
        base_path = 'D:'
        conn = self.request
        file_addr = self.client_address
        print ('connected...')

        choice = conn.recv(1024)
        print choice

        if choice == 'upload':
            file_data = conn.recv(1024)
            print file_data
            file_name, file_size = file_data.split('|')
            recv_size = 0
            file_dir = os.path.join(base_path,file_name)

            mysql_data = Upload()
            mysql_data.up_addr = file_addr
            mysql_data.up_name = file_name
            mysql_data.up_size = file_size
            mysql_data.up_dir = file_dir
            mysql_data.save()

            f = open(file_dir, 'wb')
            flag = True
            while flag:
                if int(file_size) > recv_size:
                    data = conn.recv(1024)
                    recv_size += len(data)
                else:
                    break
                f.write(data)
            f.close()
            print ('上传成功!')
            conn.send('上传成功')

        elif choice == 'download':
            base_path = r'D:\all_File'
            conn = self.request
            addr = self.client_address
            for files in os.walk(base_path):
                file_list = files[2]
            conn.sendall(','.join(file_list))
            requese_name = conn.recv(1024)
            filename = os.path.join(base_path, requese_name)
            size = os.stat(filename).st_size
            conn.send(str(size))
            if requese_name in file_list:
                file_size = os.stat(filename).st_size
                print filename
                f = open(filename, 'rb')
                send_size = 0
                flag = True
                while flag:
                    if send_size + 1024 > file_size:
                        data = f.read(file_size - send_size)
                        flag = False
                    else:
                        data = f.read(1024)
                        send_size += 1024
                    conn.send(data)
                f.close()
            mysql_data = Download()
            mysql_data.down_addr = addr
            mysql_data.down_name = filename
            mysql_data.down_size = file_size
            mysql_data.save()
            print conn.recv(1024)

if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('', 8018), MyServer)
    server.serve_forever()

