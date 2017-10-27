#!/usr/bin/python
# coding=utf-8
import time
import Model
import linecache, socket, struct, json
from urllib2 import urlopen
import thread, threading


def real_ip():
    '''读取所有真实IP,写入iplist列表中'''
    ip_file = '/root/my_ip/zzr.txt'
    iplist = []
    with open(ip_file, 'r') as f:
        for line in f.readlines():
            iplist.append(line.replace('\n', '').split()[0])
    return iplist


def get_info(ip, i, lock):
    '''先查询数据库是否存在IP，不存在就去调取淘宝接口'''
    lock.acquire()
    mysql = Model.MysqlConn()
    conn = mysql.mysql_connect()
    cursor = conn.cursor()
    long_ip = struct.unpack('!L', socket.inet_aton(ip))[0]
    sql_query = 'select ip from ip_addr where ip = %d' % long_ip
    cursor.execute(sql_query)
    info = cursor.fetchone()
    if info == None:
        area_info = []
        print ip
        request_url = 'http://ip.taobao.com/service/getIpInfo.php?ip=%s' % ip
        doc = urlopen(request_url).read()

        area_info.append(long_ip)
        area_info.append(str(ip))

        area_info.append(json.loads(doc)['data']['country'].encode('utf-8'))
        area_info.append(json.loads(doc)['data']['country_id'].encode('utf-8'))

        area_info.append(json.loads(doc)['data']['area'].encode('utf-8'))
        area_info.append(json.loads(doc)['data']['area_id'].encode('utf-8'))

        area_info.append(json.loads(doc)['data']['region'].encode('utf-8'))
        area_info.append(json.loads(doc)['data']['region_id'].encode('utf-8'))

        area_info.append(json.loads(doc)['data']['city'].encode('utf-8'))
        area_info.append(json.loads(doc)['data']['city_id'].encode('utf-8'))

        area_info.append(json.loads(doc)['data']['county'].encode('utf-8'))
        area_info.append(json.loads(doc)['data']['county_id'].encode('utf-8'))

        area_info.append(json.loads(doc)['data']['isp'].encode('utf-8'))
        area_info.append(json.loads(doc)['data']['isp_id'].encode('utf-8'))

        sql_insert = "insert into ip_addr (ip, read_ip, country, country_id, area, area_id, region, region_id, city, city_id, county, county_id, isp, isp_id) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql_insert, area_info)
        conn.commit()
        cursor.close()
        conn.close()
    lock.release()


def main():
    iplist = real_ip()
    speed = 10
    i = 0
    while i < (len(iplist) / speed) + 1:
        start = i * speed
        end = (i + 1) * speed
        thread_list = []
        for ip in iplist[int(start):int(end)]:
            Lock = threading.Lock()
            t = threading.Thread(target=get_info, args=(ip, i, Lock))
            thread_list.append(t)
        for n in thread_list:
            n.start()
            n.join()
        i = i + 1


main()