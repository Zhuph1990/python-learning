"""
    1. 定义字符串变量 `name`，输出 **我的名字叫 小明，请多多关照！**
    2. 定义整数变量 `student_no`，输出 **我的学号是 000001**
    3. 定义小数 `price`、`weight`、`money`，输出 **苹果单价 9.00 元／斤，购买了 5.00 斤，需要支付 45.00 元**
    4. 定义一个小数 `scale`，输出 **数据比例是 10.00%**
"""
name = "messi"
print("我的名字叫 %s，请多多关照！" % name)

student_no = 100
print("我的学号是 %06d" % student_no)

price = 23.3
weight = 15
money = price * weight
print("苹果单价 %.02f 元／斤，购买 %.03f 斤，需要支付 %.04f 元" % (price, weight, money))

scale = 0.2813
print("数据比例是 %.02f%%" % (scale * 100))