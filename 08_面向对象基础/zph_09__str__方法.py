class Cat:

    def __init__(self, new_name):
        self.name = new_name

        print("%s 来了" % self.name)

    def __del__(self):
         print("%s 去了" % self.name)

    def __str__(self):
        return "我是小猫[%s]" % self.name

# tom是一个全局变量
tom = Cat("tomCat")
print(tom)


