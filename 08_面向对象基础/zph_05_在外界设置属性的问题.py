class Cat:
    """这是一个猫类"""
    def eat(self):
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 爱喝水" % self.name)


# 创建对象

tom = Cat()

tom.eat()
tom.drink()
# 'Cat' object has no attribute 'name'
tom.name = "tomCat"