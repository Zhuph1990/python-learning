class A:

    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法 %d %d" % (self.num1, self.__num2))

    # 子类对象可以通过 父类的 公有方法间接访问到私有属性或私有方法
    def test(self):
        print("父类的公有方法 %d" % self.__num2)

        self.__test()


class B(A):
    def demo(self):

        # 1. 子类对象 不能 在自己的方法内部直接 访问 父类的 私有属性
        #print("访问父类的私有属性 %d" % self.num2)

        #2. 子类对象 不能 在自己的方法内部直接 访问 父类的 私有方法
        # self.__test()

        # 3. 访问父类的公有属性
        print("子类方法 %d" % self.num1)

        # 4. 调用父类的公有方法
        self.test()



b = B()
print(b)

b.demo()

# 在外界访问父类的公有属性/调用公有方法
# print(b.num1)
# b.test()




