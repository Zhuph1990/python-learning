
a = 1
print(id(a))

a = "hello"
print(id(a))

a = [1, 2, 3]
print(id(a))

a = [3, 2, 1]
print(id(a))

print("=" * 50)


demo_list = [1, 2, 3]

print("定义列表后的内存地址 %d" % id(demo_list))

demo_list.append(999)
demo_list.pop(0)
demo_list.remove(2)
demo_list[0] = 10

print("修改数据后的内存地址 %d" % id(demo_list))

demo_dict = {"name": "小明"}

print("定义字典后的内存地址 %d" % id(demo_dict))

demo_dict["age"] = 18
demo_dict.pop("name")
demo_dict["name"] = "老王"

print("修改数据后的内存地址 %d" % id(demo_dict))

demo_dict.clear()
print("clear数据后的内存地址 %d" % id(demo_dict))

demo_dict = {}
print("clear数据后重新扶植空 {} 的内存地址 %d" % id(demo_dict))

# 字典的 key 只能使用不可变类型的数据
demo_dict[1] = "整数"
print(demo_dict)

demo_dict[(1,)] = "元组"
print(demo_dict)


# demo_dict[[1,2,3]] = "列表"   unhashable
print(demo_dict)

# demo_dict[{1,2,3}] = "字典"   unhashable
print(demo_dict)

# 哈希
print(hash(1))
print(hash("hello"))

# print(hash([1,2,3,4]))   unhashable type: 'list'
# 在 Python 中，设置字典的 键值对 时，会首先对key 进行 hash`
# 已决定如何在内存中保存字典的数据，以方便 后续 对字典的操作：增、删、改、查


