name_list = ["messi", "suarez", "pique"]

print(name_list)
del name_list[1]
print(name_list)

# del关键字本质上是用来 将一个变量从内存中删除的
name = "barcelona"
del name
# 如果使用 del关键字将变量从内存中删除，后续的代码就不能再使用这个变量了
print(name)
