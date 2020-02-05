
def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        yield a
        a, b = b, a+b
        current_num += 1
    return "OK...."

# 创建一个生成器对象

obj2 = create_num(2)
while True:
    try:
        ret = next(obj2)
        print("obj2:",ret)
    except Exception as ret:
        print(ret.value)
        break

