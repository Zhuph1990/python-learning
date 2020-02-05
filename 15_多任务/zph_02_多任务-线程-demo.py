from time import sleep
from threading import Thread

def sing():
    for i in range(5):
        print("正在唱歌...%d" % i)
        sleep(1)

def dance():
    for i in range(5):
        print("正在跳舞...%d" % i)
        sleep(1)


def main():
    t1 = Thread(target=sing)
    t2 = Thread(target=dance)
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()
