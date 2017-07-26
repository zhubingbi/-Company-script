#!/usr/bin/python
#coding=utf-8
import MySQLdb
conn = MySQLdb.connect(host='118.89.157.163',user='root',passwd='careland',port=3329,db='lzhd_admin',charset='utf8')
cur = conn.cursor()

conn2 = MySQLdb.connect(host='118.89.157.163',user='root',passwd='careland',port=3329,db='kol',charset='utf8')
cur2 = conn2.cursor()


for i in range(10,100):
    table = 'stat_table_'+str(i)
    #table = 'stat_table_14'
    sql = 'SELECT DISTINCT a.aid AS aid, a.wxid AS son, a.fromWxid AS parent, b.fromWxid AS grandfather FROM ((SELECT aid, wxid, fromWxid  FROM %s WHERE fromWxid != wxid GROUP BY aid, wxid, fromWxid) AS a) INNER JOIN ((SELECT wxid, fromWxid FROM %s WHERE fromWxid != wxid GROUP BY wxid, fromWxid) AS b) ON a.fromWxid = b.wxid order by a.aid desc;' % (table,table)
    try:
        cur.execute(sql)
        for row in cur.fetchall():
            value = []
            sql2 = 'insert into '+table+' (aid, son, parent, grandparent) values (%s,%s,%s,%s)'
            value.append(int(row[0]))
            value.append(row[1].encode())
            value.append(row[2].encode())
            value.append(row[3].encode())
            cur2.execute(sql2, value)
    except Exception as e:
        print e
conn2.commit()
conn2.close()
cur.close()
conn.close()