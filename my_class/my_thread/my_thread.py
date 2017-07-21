#!/usr/bin/python
# coding=utf-8
import time
import thread
"""
def loop0():
    print ('start loop0 at: ', time.ctime())
    time.sleep(4)
    print ('loop0 down at: ', time.ctime())

def loop1():
    print ('start loop1 at: ', time.ctime())
    time.sleep(2)
    print ('loop1 down at: ', time.ctime())

def main():
    print ("ALL is start at: ", time.ctime())
    loop0()
    loop1()
    print ('ALL is down at: ', time.ctime())

if __name__=="__main__":
    main()

def loop0():
    print ('start loop0 at: ', time.ctime())
    time.sleep(4)
    print ('loop0 down at: ', time.ctime())

def loop1():
    print ('start loop1 at: ', time.ctime())
    time.sleep(2)
    print ('loop1 down at: ', time.ctime())

def main():
    print ("ALL is start at: ", time.ctime())
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    time.sleep(4)
    print ('ALL is down at: ', time.ctime())

if __name__ == "__main__":
    '''
    是python的内置属性，有两个值，如果这个脚本自己执行，那么它的值就是'__main__', 如果脚本被导入执行，那么__name__的值就是文件名
    '''
    main()
"""

'''
def loop(nloop,nsec):
    print ('start loop%s at: ' % nloop, time.ctime())
    time.sleep(nsec)
    print ("loop%s down at: " % nloop, time.ctime())

def main():
    print ("ALL is start at: ", time.ctime())
    sleep_list = [4,2]
    for i in range(len(sleep_list)):
        thread.start_new_thread(loop, (i, sleep_list[i]))
    time.sleep(4)
    print ('ALL is down at: ', time.ctime())

if __name__ == "__main__":
    main()
'''
'''
def loop(nloop,nsec,lock):
    print ('start loop%s at: ' % nloop, time.ctime())
    time.sleep(nsec)
    print ("loop%s down at: " % nloop, time.ctime())
    lock.release()
    # 释放锁，lock必须是一个已经获取的锁对象

def main():
    print ("ALL is start at: ", time.ctime())
    sleep_list = [4,2]
    lock_list = []
    #for i in range(len(sleep_list)):
    #    Lock = thread.allocate_lock()
        # 生成线程锁
    #    Lock.acquire()
        # 获取线程锁
    #    lock_list.append(Lock)

    for i in range(len(sleep_list)):
        lock = thread.allocate_lock()
        lock.acquire()
        thread.start_new_thread(loop, (i, sleep_list[i], lock))
    time.sleep(max(sleep_list))
    print ('ALL is down at: ', time.ctime())

if __name__ == "__main__":
    main()
'''


def loop(nloop,nsec,lock):
    print ('start loop%s at: %s' % (nloop,nsec))
    time.sleep(nsec)
    print ('stop loop%s at: %s' % (nloop,nsec))
    lock.release()

def main():
    print ('ALL is start at: ', time.ctime())
    sleep_list = [2, 4]
    for i in range(len(sleep_list)):
        lock = thread.allocate_lock()
        lock.acquire()
        thread.start_new_thread(loop, (i, sleep_list[i], lock))
    time.sleep(max(sleep_list))
    print ('ALL is down at: ', time.ctime())
if __name__ == '__main__':
    main()