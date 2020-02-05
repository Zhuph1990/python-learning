import threading
import time

g_num = 0

def work1(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("----in work1, g_num is %d----"%g_num)


def work2(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("----in work2, g_num is %d----"%g_num)


def main():
    print("----线程创建之前g_num is %d----" % g_num)

    t1 = threading.Thread(target=work1, args=(1000000,))
    t2 = threading.Thread(target=work2, args=(1000000,))

    t1.start()
    t2.start()

    time.sleep(5)


    print("2个线程对同一个全局变量操作之后的最终结果是:%s" % g_num)

if __name__ == "__main__":
    main()

# 如果多个线程同时对同一个全局变量操作，会出现资源竞争问题，从而数据结果会不正确