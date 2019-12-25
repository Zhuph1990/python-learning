class Women:

    def __init__(self, name):

        self.name = name
        # 不要问女生的年龄
        self.__age = 18

    def __secret(self):
        print("%s 的年龄是 %d" % (self.name, self.__age))


xiaofang = Women("小芳")



# Python 中，并没有 真正意义的私有

print(xiaofang._Women__age)

# 私有方法，外部不能直接调用

xiaofang._Women__secret()