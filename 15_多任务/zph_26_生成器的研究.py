
def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:

        yield a
        a, b = b, a+b
        current_num += 1

# 创建一个生成器对象
obj = create_num(10)
obj2 = create_num(2)

# 调用生成器（迭代器）的next方法：
ret = next(obj)
print("obj:", ret)

ret = next(obj)
print("obj:",ret)

ret = next(obj)
print("obj:",ret)

ret = next(obj)
print("obj:",ret)

ret = next(obj2)
print("obj2:",ret)

ret = next(obj2)
print("obj2:",ret)



# 生成器是一类特殊的迭代器
# for num in obj:
#     print(num)
