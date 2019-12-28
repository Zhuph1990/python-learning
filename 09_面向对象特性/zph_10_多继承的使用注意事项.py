class A:

    def test(self):
        print("A --- test方法")

    def demo(self):
        print("A --- demo方法")


class B:

    def test(self):
        print("B --- test方法")

    def demo(self):
        print("B --- demo方法")



class C(B, A):

    pass


c = C()

c.test()
c.demo()

# MRO 是 method resolution order，主要用于 在多继承时判断 方法、属性 的调用 路径

# 确定 C 类对象调用方法的顺序
print(C.__mro__)



