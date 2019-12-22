num_list = [1,2,3,4]

# 1. 内置函数
print(num_list)
# 关键字删除
del num_list[2]

print(num_list)
# 函数删除
del(num_list[2])

print(num_list)

# 最大最小字符
t_str = "dkjarikhjefsfleskrlsejfknzxsfkeskrlser"
print(max(t_str))
print(min(t_str))

t_dict = {"a":"z","b":"y","c":"x"}
print(max(t_dict))
print(min(t_dict))

# 比较大小
 # 字典不可以参加比较
print("1" > "2")
print("aaa" < "bbb")
print([1,1,1] > [2,2,2])
print((1,1,10) < (2,2,2))


#2. 切片
print("-" * 50)
str1 = "01234"
print(str1[1:3])

list1 = [0,1,2,3,4]
print(list1[1:3])

tuple1 = (0,1,2,3,4)
print(tuple1[1:3])

# 字典不可以切片
dict1 = {"a":"a","b":"b"}
# print(dict1[0:1])

# 3. 运算符
print("-" * 50)
list2 = [1,2]
print(list2 * 5)

tuple2 = (1,2)
print(tuple2 *2)
# 字典不可以参与运算

str2 = "hello" + "messi"
print(str2)
tuple3 = (1,2) +(3,4)
print(tuple3)

# 新的列表
list3 = [1,2] + [3,4]
print(list3)

# 改变原来的列表
list4 = [1,3]
list4.extend([2,4])
print(list4)

# 添加一个元素  当作
list5 = [2,4]
list5.append(6)
print(list5)
list5.append([8])
print(list5)

# in / not in
print("a" in "asdaa")
print("a" not in "asdaa")

print(1 in [0,1,2])
print(1 not in [0,1,2])

print("name" in {"name":"messi"})
print("messi" in {"name":"messi"})

# for 循环
