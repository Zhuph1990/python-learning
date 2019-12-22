# 1.判断空白字符
space_str = " "
print(space_str.isspace())

space_str2 = "  \t\n\r"
print(space_str2.isspace())

print("=" * 50)

# 2. 判断字符串中是否只包含数字
# 2.1 都不能判断小数
# 2.2 unicode 字符串
# 2.3 中文数字
# num_str = "1"
# num_str = "1.23"
# num_str = "⑴"
#num_str = "\u00b2"
num_str = "一千零一"
print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())