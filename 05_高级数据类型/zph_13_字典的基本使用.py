messi_dict ={"name":"梅西",
        "age":32,
        "team":"barcelona",
        "no":10}

# 取值
print(messi_dict["name"])

# 增加 修改

messi_dict["gender"] = "male"
print(messi_dict)

messi_dict["team"] = "Argentina"
print(messi_dict)


# 删除
messi_dict.pop("no")
print(messi_dict)



