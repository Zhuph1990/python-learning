import threading
import time

g_num = 0

def work1(num):
    global g_num

    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("----in work1, g_num is %d----"%g_num)


def work2(num):
    global g_num

    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("----in work2, g_num is %d----"%g_num)

# 创建一个互斥锁
# 默认是未上锁的状态
mutex = threading.Lock()

def main():
    print("----线程创建之前g_num is %d----" % g_num)

    t1 = threading.Thread(target=work1, args=(1000000,))
    t2 = threading.Thread(target=work2, args=(1000000,))

    t1.start()
    t2.start()

    # 等待计算完成
    while len(threading.enumerate()) != 1:
        time.sleep(1)


    print("2个线程对同一个全局变量操作之后的最终结果是:%d" % g_num)

if __name__ == "__main__":
    main()

# 如果多个线程同时对同一个全局变量操作，会出现资源竞争问题，从而数据结果会不正确