import socket

def main():

	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# 绑定本地信息
	udp_socket.bind(("", 7890))

	while True:
		send_data = input("请输入要发送的数据:")

		udp_socket.sendto(send_data.encode('utf-8'), ('192.168.0.104', 8080))

	udp_socket.close()

if __name__ == '__main__':
	main()