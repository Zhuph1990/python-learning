
# 变量 和 数据 是分开存储的

name_str = "messi"
print(id(name_str))

print(id("messi"))

player_name = name_str
print(id(player_name))

# 如果变量已经被定义，当给一个变量赋值的时候，本质上是 修改了数据的引用
name_str = "suarez"
print(id(name_str))