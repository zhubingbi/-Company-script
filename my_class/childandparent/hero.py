#!/usr/bin/python
#coding=utf-8
import glob
import linecache,socket,struct
import re
import sys
import urllib,urllib2
from urllib import urlopen
import json
import time,datetime
import MySQLdb
import os
def get_request_info(str_1,ip,time,pv,ua,realUrl,area_info,hour,day):
        try:
                request_info_list = str_1.split("&")
                list_value = []
                list_key = []
                for i in request_info_list:
                        list_2 = i.split('=')
                        if list_2[1] == '':
                                list_2[1] = '0'
                        list_2[1] = urllib.unquote(list_2[1])
                        list_value.append(list_2[1].strip())
                        list_key.append(list_2[0].strip())
                list_key[0] = 'referrer'
                list_key.append('ip')
                list_value.append(ip)
                list_key.append('rtime')
                list_value.append(time)
                list_key.append('hour')
                list_value.append(hour)
                list_key.append('day')
                list_value.append(day)
                list_key.append('pv')
                list_value.append(pv)
                list_key.append('ua')
                list_value.append(ua)
                list_key.append('realUrl')
                list_value.append(realUrl)
                list_key.extend(['country', 'region', 'city', 'area', 'isp'])
                list_value.extend(area_info)
                list_value[list_key.index('osv')] = list_value[list_key.index('osv')].strip().lstrip().rstrip(';')
                list_value[list_key.index('netType')] = list_value[list_key.index('netType')].split(' ')[0]
                dict_info = dict(zip(list_key,list_value))
        except Exception, e:
                print Exception,':',e
                pass
        return dict_info

def get_time(str_1):
        time_list = str_1.split(' ')
        del time_list[1]
        return ''.join(time_list)

def flush_key(list_1):
        str1 = ','.join(list_1)
        fh = open('/tmp/key.txt','a')
        fh.write(str1)
        fh.write("\n")
        fh.close()

def std_sort(dict_info):
        std_list = ['aid','wxid','fromWxid','ghid','cid','tid','title','url','realUrl','ip','pv','screen','referrer','brvsub','brv','netType','lg','os','osv','mobile','mobileName','srcType','logType','shareType','shareUrl','attent','country','region','city','area','isp','rtime','ua','media_id','media_area','media_nickname','media_order_id','media_account','sex','chid','chtype','day','hour']
        result_list = ['0']*len(std_list)
        for key in dict_info:
                if key in std_list:
                        index = std_list.index(key)
                        result_list[index] = dict_info[key]
        if result_list[17] == 'iPhone':
                if result_list[11] == '320x480':
                        result_list[11] = '640x960'
                        result_list[19] = 'iPhone 4/4S'
                elif result_list[11] == '320x568':
                        result_list[11] = '640x1136'
                        result_list[19] = 'iPhone 5/5S/5C'
                elif result_list[11] == '375x667':
                        result_list[11] = '750x1334'
                        result_list[19] = 'iPhone 6/6S'
                elif result_list[11] == '414x736':
                        result_list[11] = '1242x2208'
                        result_list[19] = 'iPhone 6/6S Plus'
        return result_list

def get_dict_area(ip,long_ip):
        area_info = []
        cur.execute('select country,region,city,area,isp from ip_addr where ip = %d' % long_ip)
        mysql_info = cur.fetchone()
        if mysql_info == None:
                pass
                #url_list = 'http://ip.taobao.com/service/getIpInfo.php?ip='+ip
                #doc = urlopen(url_list).read()
                #doc = json.loads(doc)
                #country = urllib.unquote(doc['data']['country'].encode('utf-8'))
                #area_info.append(country)
                #region = urllib.unquote(doc['data']['region'].encode('utf-8'))
                #area_info.append(region)
                #city = urllib.unquote(doc['data']['city'].encode('utf-8'))
                #area_info.append(city)
                #area = urllib.unquote(doc['data']['area'].encode('utf-8'))
                #area_info.append(area)
                #isp = urllib.unquote(doc['data']['isp'].encode('utf-8'))
                #area_info.append(isp)
        else:
                area_info = list(mysql_info)
                #area_info = map(lambda x: x.encode('utf-8'), area_info)
        return area_info

def flush_file(list_1,file_name):
        str1 = '@'.join(list_1)
        fh = open('/data/nginx_log/pre_hadoop/hadoop.txt','a')
        fh.write(str1)
        fh.write("\n")
        fh.close()

def get_sys_time(hours=1,date_format='%Y-%m-%d %H:%M:%S'):
        hours = int(hours)
        sys_time = time.time() - hours*60*60
        t = time.strftime('%Y-%m-%d-%H',time.localtime(sys_time))
        h = time.strftime('%H',time.localtime(sys_time))
        d = time.strftime('%Y-%m-%d',time.localtime(sys_time))
        return t,h,d

if __name__ == "__main__":
        conn = MySQLdb.connect(host='10.0.0.61',port=3306,user='lzhd',passwd='lzhdadmin',db='lzhd_admin')
        #conn = MySQLdb.connect(host='127.0.0.1',port=3329,user='root',passwd='careland',db='lzhd',charset='utf8')
        cur = conn.cursor()
        sys_time = get_sys_time()
        sum_num = 0
        with open('/data/nginx_log/pre_hadoop/access-hadoop.log','r') as f:
                for line in f.readlines():
                        R=r'(.*?) (.*?) (.*?) (.*?) \[(.*?)\] \"(.*?)\" (.*?) \"(.*?)\" (\d+) (\d+) \"(.*?)\" \"(.*?)\" \"(.*?)\" \"(.*?)\" (\d+)'
                        #R=r'(.*?) (.*?) (.*?) (.*?)  \[(.*?)\] \"(.*?)\" \"(.*?)\" (.*?) (.*?) \"(.*?)\" \"(.*?)\" \"(.*?)\" \"(.*?)\" (.*?) (.*?)'
                        o = re.compile(R)
                        b = o.match(line.replace('\n',''))
                        nginx_info = b.groups()
                        ip = nginx_info[0]
                        rtime = get_time(nginx_info[4])
                        pv = '1'
                        ua = nginx_info[11]
                        realUrl = nginx_info[10]
                        long_ip = struct.unpack('!L',socket.inet_aton(ip))[0]
                        area_info = get_dict_area(ip,long_ip)
                        if not area_info:
                                unkownip_file = '/data/nginx_log/pre_hadoop/unkown_ip'
                                fh = open('/data/nginx_log/pre_hadoop/unkown_ip','a')
                                fh.write(ip+"\n")
                                fh.close()
                        hadoop_file = '/data/nginx_log/pre_hadoop/hadoop.txt'
                        try:
                                flush_file(std_sort(get_request_info(nginx_info[7],ip,rtime,pv,ua,realUrl,area_info,sys_time[1],sys_time[2])),hadoop_file)
                        except Exception:
                                continue
                        sum_num += 1
        f = open('/tmp/num.txt','a')
        sys_time = get_sys_time()
        f.write(sys_time[0]+' '+str(sum_num)+'\n')
        f.close()
        os.system('/soft/sh/Insert_mysql.py')
        os.system('/soft/sh/hive.sh')
        os.system('/soft/sh/Insert_result.py')
        os.system('/soft/sh/Insert_activity_region.py')
        os.system('/soft/sh/Insert_activity_isp.py')
        os.system('/soft/sh/Insert_activity_mobile.py')
        os.system('/soft/sh/Insert_activity_os.py')
        os.system('/soft/sh/Insert_activity_gender.py')
        cur.close()
        conn.commit()
        conn.close()
        os.system('cat /data/nginx_log/pre_hadoop/unkown_ip|sort|uniq > /data/nginx_log/pre_hadoop/ip.txt')