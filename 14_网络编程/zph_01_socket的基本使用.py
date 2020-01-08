import socket

def main():
	
    # 创建tcp的套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 可以使用套接字收发数据
    udp_socket.sendto(b"hahahaha",("192.168.0.104",8080))

    # 不用的时候，关闭套接字
    udp_socket.close()

    print("-------run-------")


if __name__ == '__main__':
        main()
