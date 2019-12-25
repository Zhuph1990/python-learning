class Cat:
    """这是一个猫类"""
    def eat(self):
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 爱喝水" % self.name)


# 创建对象

tom = Cat()

tom.name = "tomCat"

tom.eat()
tom.drink()

# print(tom)

# 再创建一个猫对象

lazy_cat = Cat()
lazy_cat.name = "lazyCat"

lazy_cat.eat()
lazy_cat.drink()

# print(lazy_cat)