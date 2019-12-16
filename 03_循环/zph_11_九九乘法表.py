# @Author : Zhuph
# @Time : 2019/12/16 22:42
row = 1

while row <= 9:

    col = 1
    # 开始循环

    while col <= row:
        # print("%d" % col)
        print("%d * %d = %d" % (col,row,col * row), end="\t")

        col += 1

    # print("第 %d 行" % row)
    print("")

    row += 1