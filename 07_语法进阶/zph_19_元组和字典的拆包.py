def demo(*args, **kwargs):

    print(args)
    print(kwargs)


# 需要将一个元组变量/字典变量传递给函数对应的参数
gl_nums = (1, 2, 3)
gl_xiaoming = {"name": "messi", "age": 35}

# 会把 num_tuple 和 xiaoming 作为元组传递个 args
# demo(gl_nums, gl_xiaoming)

# demo(1,2,3, name = "messi",age = 35)

demo(*gl_nums, **gl_xiaoming)



"""
使用 拆包简化参数的传递，拆包的方式是：  ======>简化传递

- 在 元组变量前，增加 一个  * 
- 在 字典变量前，增加 两个  **

"""
