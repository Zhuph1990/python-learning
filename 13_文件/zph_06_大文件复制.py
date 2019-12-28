# 1.打开文件
file_read = open("README")

file_write = open("READ[复制]","w")


# 2. 读写
while True:

    # 读取一行
    text = file_read.readline()

    if not text:
        break
    file_write.write(text)

# 3. 关闭文件

file_read.close()
file_write.close()