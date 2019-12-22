def demo(num, num_list):

    print("函数内部")

    # 赋值语句
    num = 200
    num_list = [1, 2, 3]

    print(num)
    print(num_list)

    print("函数代码完成")


gl_num = 99
gl_list = [4, 5, 6]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)

"""
无论传递的参数是 可变 还是 不可变
只要针对参数使用 赋值语句，会在 函数内部 修改 局部变量的引用，不会影响到 外部变量的引用
"""