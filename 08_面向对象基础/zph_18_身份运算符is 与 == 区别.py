# 身份运算符用于 比较 两个对象的 内存地址 是否一致 —— 是否是对同一个对象的引用
a = [1, 2, 3]
b = [1, 2, 3]
print(b is a)
print(b == a)

