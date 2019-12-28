# from zph_01_测试模块1 import say_hello
from zph_02_测试模块2 import say_hello as module2_say_hello
from zph_01_测试模块1 import say_hello

# 如果 两个模块，存在 同名的函数，那么 后导入模块的函数，会 覆盖掉先导入的函数

say_hello()
module2_say_hello()

