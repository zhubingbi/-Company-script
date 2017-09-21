# coding=utf-8
import threading
import time

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

main()

