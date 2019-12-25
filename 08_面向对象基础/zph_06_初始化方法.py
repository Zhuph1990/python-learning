class Cat:
    def __init__(self):
        print("这是一个初始化方法")

        # self.属性名 = 属性的初始值
        self.name = "tomCat"

    def eat(self):
        print("%s 爱吃鱼" % self.name)

tom = Cat()
print(tom.name)
tom.eat()