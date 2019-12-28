class Animal:

    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Dog(Animal):

    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):

    def fly(self):
        print("我会飞")

    # 重写之后，在运行时，只会调用 子类中重写的方法，而不再会调用 父类封装的方法
    def bark(self):
        print("叫的跟神一样...")


xtq = XiaoTianQuan()

xtq.bark()

