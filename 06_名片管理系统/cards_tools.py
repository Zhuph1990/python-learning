def show_menu():
    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0")
    print("")
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("0. 退出系统")
    print("*" * 50)

# 所有名片记录的列表
card_list = []

def new_card():
    print("-" * 50)
    print("新增名片")
    name_str = input("请输入姓名： ")
    phone_str = input("请输入电话： ")
    qq_str = input("请输入QQ： ")
    email_str = input("请输入邮箱： ")

    card_dict ={
        "name": name_str,
        "phone": phone_str,
        "qq": qq_str,
        "email" : email_str
    }

    card_list.append(card_dict)

    print(card_list)

    print("新增名片 %s 成功" % name_str)

def show_all():

    print("-" * 50)
    print("显示所有名片")

    if len(card_list) == 0:
        print("当前没有任何名片记录。请使用新增功能添加名片")

        #
        return

    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")


    print("")

    print("=" * 50)

    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))


def search_card():
    """搜索名片
    """
    print("-" * 50)
    print("功能：搜索名片")

    # 1. 提示要搜索的姓名
    find_name = input("请输入要搜索的姓名：")

    # 2. 遍历字典
    for card_dict in card_list:

        if card_dict["name"] == find_name:
            print("姓名\t\t\t电话\t\t\tQQ\t\t\t邮箱")
            print("-" * 50)

            print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (
                card_dict["name"],
                card_dict["phone"],
                card_dict["qq"],
                card_dict["email"]))

            print("-" * 50)

            # 针对找到的字典进行后续操作：修改/删除
            deal_card(card_dict)

            break
    else:
        print("没有找到 %s" % find_name)



def deal_card(find_dict):

    """操作搜索到的名片字典
    :param find_dict:找到的名片字典
    """
    print(find_dict)

    action_str = input("请选择要执行的操作 [1] 修改 [2] 删除 [0] 返回上级菜单")

    if action_str == "1":

        print("修改")
        find_dict["name"] = input_card_info(find_dict["name"], "请输入姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "请输入电话：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "请输入QQ：")
        find_dict["email"] = input_card_info(find_dict["email"], "请输入邮件：")

        print("%s 的名片修改成功" % find_dict["name"])

    elif action_str == "2":

        print("删除")
        card_list.remove(find_dict)


def input_card_info(dict_value, tip_message):

    """输入名片信息

    :param dict_value: 字典原有值
    :param tip_message: 输入提示信息
    :return: 如果输入，返回输入内容，否则返回字典原有值
    """
    # 1. 提示用户输入内容
    result_str = input(tip_message)

    # 2. 针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:

        return result_str
    # 3. 如果用户没有输入内容，返回 `字典中原有的值`
    else:

        return dict_value