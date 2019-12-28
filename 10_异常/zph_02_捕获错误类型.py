# 1. 提示用户输入一个整数
# 2. 使用 `8` 除以用户输入的整数并且输出
try:
    num = int(input("请输入整数："))
    result = 8 / num
    print(result)
except ValueError:
    print("请输入正确的整数")
except ZeroDivisionError:
    print("除 0 错误")


