from threading import Thread
import time


def work1(temp_nums):
    temp_nums.append(33)

    print("----in work1, temp_nums is %s---" % str(temp_nums))


def work2(temp_nums):
    print("----in work2, temp_nums is %s---" % str(temp_nums))


g_nums = [11, 22]

def main():
    # target 指定将来这个线程去哪个函数执行代码
    # args 指定将来调用函数的时候 传递什么数据过去   入参必须是元组
    t1 = Thread(target=work1, args=(g_nums,))
    t2 = Thread(target=work2, args=(g_nums,))

    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)

    print("---in main Thread g_num is %s---" % str(g_nums))


if __name__ == "__main__":
    main()
