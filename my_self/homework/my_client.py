#!/usr/bin/pyhon
# coding=utf-8
import socket
import os


def upload():
    while True:
        name = raw_input('输入上传文件路径: ')
        file_name = os.path.basename(name)
        file_size = os.stat(name).st_size
        print file_name
        print file_size
        sock.sendall(file_name+'|'+str(file_size))
        send_size = 0
        f = open(name, 'rb')
        flag = True
        while flag:
            if send_size + 1024 > file_size:
                data = f.read(file_size - send_size)
                flag = False
            else:
                data = f.read(1024)
                send_size += 1024
            sock.send(data)
        f.close()
        data = sock.recv(1024)
        print (data)
        break


def download():
    base_dir = r'D:\client'
    print '服务端文件：', sock.recv(1024)
    while True:
        filename = raw_input('请输入要下载的文件: ')
        sock.send(filename)
        file_size = sock.recv(1024)
        print file_size
        file_dir = os.path.join(base_dir, filename)
        print file_dir
        f = open(file_dir, 'wb')
        recv_size = 0
        flag = True
        while flag:
            if int(file_size) > recv_size:
                data = sock.recv(1024)
                recv_size += len(data)
            else:
                break
            f.write(data)
        f.close()
        sock.send('下载完成')
        break


while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 8018))
    choice = raw_input('What do you want?  upload or download? ')
    sock.send(choice)
    if choice == 'upload':
        upload()
    elif choice == 'download':
        download()
