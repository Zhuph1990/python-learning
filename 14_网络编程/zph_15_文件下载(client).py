from socket import *


def main():

    # 1. 创建socket
    tcp_client_socket = socket(AF_INET, SOCK_STREAM)

    # 2. 目的信息  获取服务器的 ip port
    server_ip = input("请输入服务器ip:")
    server_port = int(input("请输入服务器port:"))

    # 3. 链接服务器
    tcp_client_socket.connect((server_ip, server_port))

    # 4. 输入需要下载的文件名
    download_file_name = input("请输入要下载的文件名：")

    # 5. 发送文件下载请求  文件名字发送到服务器
    tcp_client_socket.send(download_file_name.encode("utf-8"))

    # 6. 接收对方发送过来的数据，最大接收1024个字节（1K）
    recv_data = tcp_client_socket.recv(1024*1024)  # 1k*1024=1M

    # print('接收到的数据为:', recv_data.decode('utf-8'))
    # 7. 如果接收到数据再创建文件，否则不创建
    if recv_data:
        with open("[new]"+download_file_name, "wb") as f:
            f.write(recv_data)

    # 8. 关闭套接字
    tcp_client_socket.close()


if __name__ == "__main__":
    main()