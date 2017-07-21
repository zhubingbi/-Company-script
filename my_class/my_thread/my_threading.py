#!/usr/bin/python
# coding=utf-8
import time
import threading
'''

def loop(nloop, nsec):
    print ('start loop%s at: %s' % (nloop, nsec))
    time.sleep(nsec)
    print ('stop loop%s at: %s' % (nloop, nsec))


def main():
    print ('ALL is start at: ', time.ctime())
    sleep_list = [2, 4, 1, 3]
    thread_list = []
    for i in range(len(sleep_list)):
        t = threading.Thread(target = loop, args = (i,sleep_list[i]))   # 创建线程
        thread_list.append(t)
    for i in thread_list:
        i.start()  # 开始线程
    for i in thread_list:
        i.join() 
    print ('ALL is down at: ', time.ctime())
if __name__ == '__main__':
    main()

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print ('This is our thread it is start,', time.ctime())
        time.sleep(2)
        print ('This is our thread it is done', time.ctime())

thread_list = []
for i in range(10):
    m = MyThread()
    thread_list.append(m)
for i in thread_list:
    i.start()
for i in thread_list:
    i.join()
'''

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.name = name
        self.age = age
        self.nsec = nsec

    def run(self):
        print ('This is our thread it is start,', time.ctime())
        time.sleep(self.nsec)


thread_list = []
for i in range(10):
    m = MyThread()
    thread_list.append(m)
for i in thread_list:
    i.start()
for i in thread_list:
    i.join()



