#!/usr/bin/python
# coding=utf-8
import threading
import time
import sys
import MySQLdb


class MysqlConn:
    def __init__(self):
        self.host = '192.168.245.129'
        self.user = 'root'
        self.passwd = 'careland'
        self.db = 'student'
        self.port = 3329

    def mysql_connect(self):
        conn = MySQLdb.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            db=self.db,
            port=self.port,
            charset='utf8'
        )
        cursor = conn.cursor()
        return cursor
