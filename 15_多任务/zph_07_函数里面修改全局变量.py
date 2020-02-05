num = 100
nums = [11, 22]
nums2 = [111, 222]


def test1():
    global num

    num += 100


def test2():

    nums.append(33)


def test3():
    global nums2

    nums2 += [100]


print(num)
print(nums)
print(nums2)

test1()
test2()
test3()

print(num)
print(nums)
print(nums2)


# 可变 与 不可变(数字 字符串 元组)
# 在一个函数中，对全局变量进行修改的时候，到底是否需要使用global进行说明，要看是否对全局变量的执行指向进行了修改。
# 如果修改了执行，即让全局变量指向了一个新的地方，那么必须使用global,如果仅仅是修改了指向空间中的数据，此时不用必须使用global