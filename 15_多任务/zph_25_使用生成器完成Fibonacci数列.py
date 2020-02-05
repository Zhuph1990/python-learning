
def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        # 使用了yield关键字的函数不再是函数，而是一个生成器的模板
        # yield关键字有两点作用：
        #   保存当前运行状态（断点），然后暂停执行，即将生成器（函数）挂起
        #   将yield关键字后面表达式的值作为返回值返回，此时可以理解为起到了return的作用
        yield a
        a, b = b, a+b
        current_num += 1

# 创建一个生成器对象
obj = create_num(10)

# 调用生成器（迭代器）的next方法：
ret = next(obj)
print(ret)

ret = next(obj)
print(ret)

# 生成器是一类特殊的迭代器
# for num in obj:
#     print(num)
