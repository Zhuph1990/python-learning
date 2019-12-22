poem = [
    "登鹳雀楼",
    "王之涣",
    "白日依山尽",
    "黄河入海流",
    "欲穷千里目",
    "更上一层楼"]

for poem_str in poem:
    print("|%s|" % poem_str.center(20))

print("=" * 50)
for poem_str in poem:
    print("|%s|" % poem_str.center(20,"　"))

print("=" * 50)
for poem_str in poem:
    print("|%s|" % poem_str.ljust(20,"　"))

print("=" * 50)
for poem_str in poem:
    print("|%s|" % poem_str.rjust(20,"　"))

# 去除空白字符

poem2 = [
    "\t\n登鹳雀楼",
    "王之涣",
    "白日依山尽\t\n",
    "黄河入海流",
    "欲穷千里目",
    "更上一层楼"]


print("*" * 50)
for poem_str in poem2:
    # 使用strip方法去除字符串中的空白字符
    print("|%s|" % poem_str.strip().center(20,"　"))


