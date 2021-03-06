import socket
import threading


# 接受客户端信息
def recv_msg(service_client_socket, ip_port):
    while True:
        recv_data = service_client_socket.recv(1024)
        if recv_data:
            recv_content = recv_data.decode('gbk')
            print(recv_content)
            service_client_socket.send('ok,问题正在处理中...'.encode('gbk'))
        else:
            print(ip_port, '客户端断开连接了')
            break
        service_client_socket.close()


if __name__ == '__main__':
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind('', 7891)
    tcp_server_socket.listen(128)

    while True:
        service_client_socket, ip_port = tcp_server_socket.accept()
        print(ip_port)

        # 创建接受数据的子线程
        recv_thread = threading.Thread(target=recv_msg, args=(service_client_socket, ip_port))
        # 设置守护主线程，主线程退出子线程直接销毁
        recv_thread.setDaemon(True)
        recv_thread.start()

    tcp_server_socket.close()
