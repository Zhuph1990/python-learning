
def say_hello():
    print("你好 你好 sayHello...")


# 如果直接执行模块，__main__
if __name__ == "__main__":

    print(__name__)

    # 文件被导入时，能够直接执行的代码不需要被执行

    print("小明开发的模块")
    say_hello()