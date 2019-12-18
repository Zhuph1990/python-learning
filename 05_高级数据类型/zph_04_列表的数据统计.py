name_list = ["messi", "suarez", "pique","messi"]

list_len = len(name_list)
print("列表中包含 %d 个元素" % list_len)

print("-" * 50)
name = "messi"
count = name_list.count(name)
print("列表中%s 出现了 %d 次" % (name, count))