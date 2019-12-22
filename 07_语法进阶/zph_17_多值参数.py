def demo(num, *args, **kwargs):

    print(num)
    print(args)
    print(kwargs)


demo(1)
demo(1, 2, 3, 4, 5, name="小明", age=18, gender=True)


# args 存放 元组 参数，前面有一个 *
# kwargs 存放 字典 参数，前面有两个 **