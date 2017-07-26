#!/usr/bin/python
# coding=utf-8
import peewee
db = peewee.MySQLDatabase(
    database='my_socket',
    host='192.168.245.129',
    user='root',
    passwd='careland',
    port=3329
)


class Upload(peewee.Model):
    up_addr = peewee.TextField()
    up_name = peewee.TextField()
    up_dir = peewee.TextField()
    up_size = peewee.TextField()

    class Meta:
        database = db


class Download(peewee.Model):
    down_addr = peewee.TextField()  # 哪个IP端口请求下载
    down_name = peewee.TextField()  # 下载了什么文件
    down_size = peewee.TextField()    # 下载文件大小

    class Meta:
        database = db

if __name__ == '__main__':
    try:
        Upload.create_table()
        Download.create_table()
    except:
        print 'It\'s all created!!!'
