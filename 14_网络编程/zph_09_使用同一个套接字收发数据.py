import socket

def main():

	# 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 获取对方的ip port
    dest_ip = input("请输入对方的ip地址")
    dest_port = int(input("请输入对方的port"))

    # 3. 从键盘获取数据
    send_data = input("请输入要发送的数据")

    # 4. 发送数据
    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))

    # 5. 接收回送过来的数据
    recv_data = udp_socket.recvfrom(1024)
    # 套接字是一个可以同时 收发数据   （全双工）
    print(recv_data)


if __name__ == '__main__':
	main()