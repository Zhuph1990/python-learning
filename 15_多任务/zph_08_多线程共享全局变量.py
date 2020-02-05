from threading import Thread
import time

# 定义全局变量
g_num = 100

def work1():
    global g_num
    g_num += 1
    print("----in work1, g_num is %d---"%g_num)


def work2():
    print("----in work2, g_num is %d---"%g_num)


def main():
    t1 = Thread(target=work1)
    t2 = Thread(target=work2)

    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)

    print("---in main Thread g_num is %d---" % g_num)


if __name__ == "__main__":
    main()
