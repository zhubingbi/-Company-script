#!/usr/bin/python
# coding=utf8

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

class Hadoop:

    def __init__(self):
        self.access.log = 'data/nginx_log/pre_hadoop/access-hadoop.log'
        self.unkown_ip = '/data/nginx_log/pre_hadoop/unkownip.txt'
        self.hadoop_file = '/data/nginx_log/pre_hadoop/hadoop_test.txt'

    def split_parm(self, parm, ip, rtime, ua, realUrl, area_info, lasthour, lastday, pv = 1):
        """对nginx信息进行筛选"""
        key = ['referrer']
        value = []
        try:
            request = parm.split('&')
            for i in request:
                parm_list = i.split('=')
                if parm_list[1] == '':
                    parm_list[1] = '0'
                    # 对值为空的项置0
                parm_list[1] = urllib.unquote(parm_list[1])
                key.append(parm_list[0].strip())
                value.append(parm_list[1].strip())
            key.extend(['ip', 'rtime', 'lasthour', 'lastday', 'pv', 'ua', 'realUrl', 'country', 'region', 'city', 'area', 'isp'])
            value.extend([ip, rtime, lasthour, lastday, pv, ua, realUrl, area_info])
            value[list_key.index('osv')] = list_value[list_key.index('osv')].strip().lstrip().rstrip(';')
            value[list_key.index('netType')] = list_value[list_key.index('netType')].split(' ')[0]
            nginx_parm = dict(zip(list_key, list_value))
        except Exception, e:
            print Exception,':',e
            pass
        return nginx_parm
        # 返回筛选出来的nginx有效信息

    def std_sort(self, nginx_parm):
        """该方法是对传进来的筛选处理好的nginx项进行排序整理,主要是因为有时候项不一定全部都有"""
        std = ['aid', 'wxid', 'fromWxid', 'ghid', 'cid', 'tid', 'title', 'url', 'realUrl', 'ip', 'pv', 'screen', 'referrer', 'brvsub', 'brv', 'netType', 'lg', 'os', 'osv', 'mobile', 'mobileName', 'srcType', 'logType', 'shareType', 'shareUrl', 'attent', 'country', 'region', 'city', 'area', 'isp', 'rtime', 'ua', 'media_id', 'media_area', 'media_nickname', 'media_order_id', 'media_account', 'sex', 'chid', 'chtype', 'day', 'hour']
        # 标准key顺序
        result = ['0']*len(std)
        for key in nginx_parm:
            if key in std:
                index = std.index(key)
                result[index] = nginx_parm[key]
                # 排序组成新的result列表，里面只有按照std的顺序排好的value值
        if result[17] == 'iPhone':
            if result[11] == '320x480':
                result[11] = '640x960'
                result[19] = 'iPhone 4/4S'
            elif result[11] == '320x568':
                result[11] = '640x1136'
                result[19] = 'iPhone 5/5S/5C'
            elif result[11] == '375x667':
                result[11] = '750x1334'
                result[19] = 'iPhone 6/6S'
            elif result[11] == '414x736':
                result[11] = '1242x2208'
                result[19] = 'iPhone 6/6S Plus'
        return result
        # 返回能写进文件保存的nginx信息

    def get_areainfo(self):
        area_info = []
        cursor.execute('select country,region,city,area,isp from ip_addr where ip = %d' % long_ip)
        mysql_info = cursor.fetchone()
        if mysql_info is not None:
            area_info = list(mysql_info)
        return area_info

    def get_systime(self, hours=1):
        hours = int(hours)
        sys_time = time.time() - hours*60*60
        lasttime = time.strftime('%Y-%m-%d-%H', time.localtime(sys_time))
        lasthour = time.strftime('%H', time.localtime(sys_time))
        lastday = time.strftime('%Y-%m-%d', time.localtime(sys_time))
        return lasttime, lasthour, lastday

    def flush_file(self, nginxlist, hivefile):
        """将整理好的有效信息写入文件"""
        nginxstr = '@'.join(nginxlist)
        f = open(hivefile, 'a')
        f.write(nginxstr+'\n')
        f.close()

    def insert_parms(self, filename):
        # 将筛选出来的nginx数据导入数据库
        mysql_conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='careland', port=3329, db='lzhd', charset='utf=8')
        cursor = mysql_conn.cursor()
        with open(filename, 'r') as f:
            for line in f.readlines():
                ghid = str(binascii.crc32(info[3]) & 0xffffffff)[0:2]
                table_name = 'stat_table_'+ghid
                sql = "insert into "+table_name+ " (aid,wxid,fromWxid,ghid,cid,tid,title,url,realUrl,ip,pv,screen,referrer,brvsub,brv,netType,lg,os,osv,mobile,mobileName,srcType,logType,shareType,shareUrl,attent,country,region,city,area,isp,rtime,ua,media_id,media_area,media_nickname,media_order_id,media_account,sex,chid,chtype,day,hour) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            try:
                cursor.execute(sql, info)
            except Exception:
                continue
        cursor.close()
        mysql_conn.commit()
        mysql_conn.close()

    def insert_source(self, filename):
        # 将hive中计算出来的pv,uv等信息插入数据库
        mysql_conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='careland', port=3329, db='lzhd', charset='utf=8')
        cursor = mysql_conn.cursor()
        with open(filename, 'r') as f:
            for line in f.readlines():
                source = line.replace('\n', '').split()
                # 产生数据前几位格式：数据库时间(年，月，日)  aid   ghid
                insert_info = tuple(source)
                aid = int(source[1])
                ghid = source[2]
                update_info = source[3:]
                update_info.extend([aid, ghid, self.get_systime()[2]])
                cursor.execute('select id from stat_report where aid=%d and day="%s" and ghid="%s"' % (aid, self.get_systime()[2], ghid))
                judge = cursor.fetchone()
                if judge is None:
                    insert_sql = "insert into stat_report (day,aid,ghid,pv,uv,cv,ip,s1,s2,s3,s4,sp1,sp2,sp3,sp4,f1,f2,f3,f4,f0,fp1,fp2,fp3,fp4,fp0) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                else:
                    update_sql = 'update stat_report set pv=%s,uv=%s,cv=%s,ip=%s,s1=%s,s2=%s,s3=%s,s4=%s,sp1=%s,sp2=%s,sp3=%s,sp4=%s,f1=%s,f2=%s,f3=%s,f4=%s,f0=%s,fp1=%s,fp2=%s,fp3=%s,fp4=%s,fp0=%s where aid = %s and ghid=%s and day = %s'


    if __name__ == '__main__':
        mysql_conn = MySQLdb.connect(host='10.0.0.61', user='lzhd', passwd='lzhdadmin', port=3306, db='lzhd_admin')
        cursor = mysql_conn.cursor()
        """本地数据库连接信息,查询地理位置信息使用"""

        nginx_file = '/data/nginx_log/pre_hadoop/access-hadoop.log'
        # 要处理的nginx日志
        unkownip_file = '/data/nginx_log/pre_hadoop/unkownip.txt'
        hadoop_file = '/data/nginx_log/pre_hadoop/hadoop.txt'
        # 处理好后nginx信息文件
        source_file = '/data/nginx _log/pre_hadoop/source.txt'
        # 在hive中计算出来的PV,uv等信息
        if os.path.exists(nginx_file) and os.path.exists(unkownip_file) and os.path.exists(hadoop_file):
            with open(nginx_file, 'r') as f:
                for line in f.readlines():
                    '''逐行获取nginx日志'''
                    R = r'(.*?) (.*?) (.*?) (.*?) \[(.*?)\] \"(.*?)\" (.*?) \"(.*?)\" (\d+) (\d+) \"(.*?)\" \"(.*?)\" \"(.*?)\" \"(.*?)\" (\d+)'
                    o = re.compile(R)
                    match_line = o.match(line.replace('\n', ''))
                    nginx_info = match_line.groups()
                    # 按照正则匹配nginx项,赋值为列表nginx_info
                    ip = nginx_info[0]
                    long_ip = struct.unpack('!L',socket.inet_aton(ip))[0]
                    # 获取IP, 以及对应的long
                    rtime = get_std_time(nginx_info[4])
                    # 获取nginx 中记录的时间信息
                    parm = nginx_info[7]
                    # parm是包含了所有url请求带过来的用户参数的字符串
                    realurl = nginx_info[10]
                    # 请求的realurl
                    ua = nginx_info[11]
                    # 请求的ua
                    area_info = get_areainfo(ip,long_ip)
                    # 获取IP对应地理信息
                    sys_time = get_systime()
                    # 获取上一个小时的时间，返回上个小时的时间串(%Y-%m-%d-%H),上一个小时小时，上一个小时的年月日.
                    if not area_info:
                        f = open(unkownip_file, 'a')
                        f.write(ip + '\n')
                        fh.close()
                    try:
                            after_deal_nginx = split_parm(parm, ip, rtime, ua, realurl, area_info, sys_time[1], sys_time[2])
                            parm = std_sort(after_deal_nginx)
                            flush_file(parm, hadoop_file)
                            insert_parms(hadoop_file)
                            insert_source(source_file)
                            # 将筛选出nginx信息插入数据库

                    except Exception, e:
                            continue
