messi_dict ={"name":"梅西",
        "age":32,
        "team":"barcelona",
        "no":10}

# 统计键值对的数量
print(len(messi_dict))

# 合并字典
temp_dict = {"country":"argentina","age":18}

messi_dict.update(temp_dict)
print(messi_dict)

# 清空字典
messi_dict.clear()
print(messi_dict)