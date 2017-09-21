#!/usr/bin/python
#coding=utf-8
import MySQLdb
import thread


def worker(table, lock):
    conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='careland', port=3329, db='lzhd_admin',
                           charset='utf8')
    cur = conn.cursor()
    conn2 = MySQLdb.connect(host='127.0.0.1', user='root', passwd='careland', port=3329, db='kol', charset='utf8')
    cur2 = conn2.cursor()
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
    lock.release()
    conn2.commit()
    cur2.close()
    conn2.close()
    cur.close()
    conn.close()


def main():
    for i in range(10, 13):
        lock = thread.allocate_lock()
        lock.acquire()
        table = 'stat_table_'+str(i)
        thread.start_new_thread(worker, (table, lock))
if __name__ == '__main__':
    main()