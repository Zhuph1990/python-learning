hello_str = "hello world"


print(hello_str.startswith("hello"))

print(hello_str.endswith("world"))

print(hello_str.find("llo"))

# 与index方法区别 不存在 -1 不会报错
print(hello_str.find("abc"))

print(hello_str.replace("world","messi"))

print(hello_str)