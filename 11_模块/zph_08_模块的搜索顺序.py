import random

rand = random.randint(0, 10)

print(rand)

print(random.__file__)

# 注意：如果当前目录下，存在一个 random.py 的文件，程序就无法正常执行了！
# 这个时候，Python 的解释器会 加载当前目录 下的 random.py 而不会加载 系统的 random 模块