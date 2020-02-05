import time
import threading

def test1():
    for i in range(5):
        print("test1...%d" % i)
        time.sleep(1)


def test2():
    for i in range(5):
        print("test2...%d" % i)
        time.sleep(1)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()

    t2.start()

    while True:
        length = len(threading.enumerate())
        print('当前运行的线程数为：%d' % length)
        if length<=1:
            break

        time.sleep(0.5)

if __name__ == '__main__':
    main()
