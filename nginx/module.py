#!/usr/bin/python
# coding=utf-8
import MySQLdb

conn = MySQLdb.connect(
    host='118.89.157.163',
    user='root',
    passwd='careland',
    port=3329,
    db='kol'
)
cursor = conn.cursor()
#for i in range(10, 100):
while True:
    table_name = 'stat_table_09'
    #drop = 'drop table if exists '+table_name
    #cursor.execute(drop)
    sql = """CREATE TABLE %s (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `aid` int(1) NOT NULL DEFAULT '0',
        `son` varchar(200) NOT NULL,
        `parent` varchar(200) NOT NULL,
        `grandparent` varchar(200) NOT NULL,
        PRIMARY KEY (`id`,`aid`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """ % table_name
    cursor.execute(sql)
    break

conn.close()