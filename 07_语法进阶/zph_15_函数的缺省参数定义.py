def print_info(name, gender=True):

    gender_text = "男生"
    if not gender:
        gender_text = "女生"

    print("%s 是 %s" % (name, gender_text))

print_info("messi")
print_info("阿美",False)

# 缺省参数，需要使用 最常见的值 作为默认值！