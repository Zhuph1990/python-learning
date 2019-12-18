name_list = ["messi", "suarez", "pique"]

# 取值和取索引
print(name_list[0])

print(name_list.index("pique"))


# 修改
name_list[1] = "busquets"

# 增加
name_list.append("rakitic")
name_list.insert(1,"alba")

temp_list = ["孙悟空" ,"猪八戒","沙悟净"]
name_list.extend(temp_list)

# 删除

print(name_list)

name_list.remove("猪八戒")
print(name_list)

# 默认删除列表中最后一个
# name_list.pop()
print(name_list)

# 清空列表
name_list.clear()
print(name_list)

print("=" * 50)
print(name_list)

