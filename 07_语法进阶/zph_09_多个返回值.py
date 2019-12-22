def measure():
    """返回当前的温度"""

    print("开始测量...")
    temp = 39
    wetness = 10
    print("测量结束...")

    # return (temp, wetness)
    #如果一个函数返回的是元组，括号可以省略
    return temp, wetness

result = measure()
print(result)

# 单独处理温度 湿度
print(result[0])
print(result[1])

# 如果函数返回类型是元组 同时希望单独的处理元组中的元素 可以使用多个变量一次接收函数的返回结果 个数必须保持一致
gl_temp, gl_wetness = measure()
print(gl_temp)
print(gl_wetness)