import socket

def send_msg(udp_socket):
    msg = input("请输入要发送的数据")
    dest_ip = input("请输入对方的ip")
    dest_port  = input("请输入对方的端口")
    udp_socket.sendto(msg.encode("utf-8"))
def recv_msg(udp_socket):
    recv_msg = udp_socket.recvfrom(1024)
    recv_ip = recv_msg[1]
    recv_msg = recv_msg[0].decode("utf-8")
    print(str(recv_ip),recv_msg)
def main():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.bind(("",7891))
    while True:
        print("="*30)
        print("1:发送消息")
        print("2:接收消息")
        print("="*30)
        op_num = input("请输入操作")
        if op_num == "1":
            send_msg(udp_socket)
        if op_num == "2":
            recv_msg(udp_socket)
        else:
            print("输入有误，请重新输入！")
if __name__ == '__main__':
    main()