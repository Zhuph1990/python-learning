a = 6
b = 100

# 1 使用其他变量
# c = a
# a = b
# b = c
print(a)
print(b)

# 2 不使用临时变量
# a = a + b
# b = a - b
# a = a - b
print(a)
print(b)

# 3 Python专有，利用元组  ===> 多个变量接收元组  a, b = (b, a)  ==> a, b = b, a
a, b = b, a
print(a)
print(b)