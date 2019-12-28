# coding=utf8


# 在字符串前，增加一个 u 表示这个字符串是一个 utf8 字符串
hello_str_u = u"你好世界"

hello_str = "hello世界"

print(hello_str)

for c in hello_str:
    print(c)


"""
Python 2.x 默认使用 ASCII 编码格式
Python 3.x 默认使用 UTF-8 编码格式
"""