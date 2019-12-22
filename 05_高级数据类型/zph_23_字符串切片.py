"""
- 1. 截取从 2 ~ 5 位置 的字符串
- 2. 截取从 2 ~ `末尾` 的字符串
- 3. 截取从 `开始` ~ 5 位置 的字符串
- 4. 截取完整的字符串
- 5. 从开始位置，每隔一个字符截取字符串
- 6. 从索引 1 开始，每隔一个取一个
- 7. 截取从 2 ~ `末尾 - 1` 的字符串
- 8. 截取字符串末尾两个字符
- 9. 字符串的逆序（面试题）
"""

num_str= "0123456789"

print(num_str[2:6])

print(num_str[2:])

print(num_str[0:6])

print(num_str[:6])

print(num_str[:])

print(num_str[::2])

print(num_str[1::2])

print(num_str[2:-1])

print(num_str[-2:])

print(num_str[-1::-1])

print(num_str[::-1])


