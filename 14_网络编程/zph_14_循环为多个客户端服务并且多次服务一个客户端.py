from socket import *


def main():

    # 1. 创建socket
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)

    # 2. 本地信息
    address = ('', 7788)

    # 绑定
    tcp_server_socket.bind(address)

    # 3. 使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的，这样就可以接收别人的链接了
    tcp_server_socket.listen(128)

    while True:

        print("等待一个新的客户端的到来...")

        # 4. 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
        # client_socket用来为这个客户端服务
        # tcp_server_socket就可以省下来专门等待其他新客户端的链接
        client_socket, client_addr = tcp_server_socket.accept()

        print("一个新的客户端已经到来:%s" % str(client_addr))

        while True:
            # 接收对方发送过来的数据
            recv_data = client_socket.recv(1024)  # 接收1024个字节
            print("客户端发送过来的请求是:%s" % recv_data.decode("gbk"))

            # 如果recv解堵塞，那么有两种方式：
            # 1. 客户端发送过来数据
            # 2. 客户端调用close而导致解堵塞
            if recv_data:
                # 发送一些数据到客户端
                client_socket.send("thank you !".encode("gbk"))
            else:
                break    

        # 关闭为这个客户端服务的套接字，只要关闭了，就意味着为不能再为这个客户端服务了，如果还需要服务，只能再次重新连接
        client_socket.close()
        print("已经为这个客户端服务完毕...")
    # 如果将监听套接字关闭了，那么会导致不能再次等待新客户端的到来，即xxx.accept就会失败    
    tcp_server_socket.close()

if __name__ == '__main__':
	main()