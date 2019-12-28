"""
- 新式类：以 object 为基类的类，推荐使用
- 经典类：不以 object 为基类的类，不推荐使用

- 在 Python 3.x 中定义类时，如果没有指定父类，会 默认使用 object 作为该类的 基类 —— Python 3.x 中定义的类都是 新式类
- 在 Python 2.x 中定义类时，如果没有指定父类，则不会以 object 作为 基类

为了保证编写的代码能够同时在 Python 2.x 和 Python 3.x 运行！
今后在定义类时，如果没有父类，建议统一继承自 object

"""

class A(object):
    pass

class B:
    pass

a = A()
print(dir(a))

print("-" * 100)

b = B()
print(dir(b))







