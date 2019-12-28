class Tool(object):

    # 使用赋值语句，定义类属性，记录创建工具对象的总数
    count = 0

    def __init__(self, name):
        self.name = name

        # 针对类属性做一个计数+1
        Tool.count += 1


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("铁锹")

# 输出工具对象的总数
# print("现在创建了 %d 个工具" % Tool.count)
"""
1. 类名.类属性**
2. **对象.类属性** （不推荐）
"""
print("工具对象的总数 %d " % tool3.count)