students = [
    {"name": "messi",
     "age": 35,
     "gender": True,
     "height": 1.7,
     "weight": 75.0},
    {"name": "suarez",
     "age": 37,
     "gender": True,
     "height": 1.85,
     "weight": 85},
]

find_name = "suarez"

for stu_dict in students:

    print(stu_dict)

    # 判断当前遍历的字典中姓名是否为find_name
    if stu_dict["name"] == find_name:
        print("找到了")

        # 如果已经找到，直接退出循环，就不需要再对后续的数据进行比较
        break

else:
    # 如果 不存在，在 循环整体结束 后，希望 得到一个统一的提示
    print("没有找到")

print("循环结束")