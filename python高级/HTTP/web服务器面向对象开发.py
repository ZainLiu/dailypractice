import socket
import re
import gevent
from gevent import monkey

monkey.patch_all()


class HttpWebServer(object):
    def __init__(self):
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        tcp_server_socket.bind(('', 8080))
        tcp_server_socket.listen(128)
        # server_socket,addr=tcp_server_socket.recv(1024)
        # 创建对象，提供socket属性
        self.tcp_server_socket = tcp_server_socket

    # 启动服务器
    def start(self):
        while True:
            server_socket, addr = self.tcp_server_socket.accept()
            # TODO 多任务处理 done
            gevent.spawn(self.handle_client_request, server_socket)

    @staticmethod
    def handle_client_request(server_socket):
        client_request_data = server_socket.recv(4096)
        print(client_request_data)
        client_request_conent = client_request_data.decode('utf-8')
        match_obj = re.search('/\S*', client_request_conent)
        if not match_obj:
            print('访问路径有误...')
            server_socket.close()
            return
        request_path = match_obj.group()
        print(request_path)
        if request_path == '/':
            request_path = '/index.html'
        try:
            with open('.'+request_path, 'rb') as file:  # 原本：with open('static' + request_path, 'rb') as file:
                file_data = file.read()
        except Exception as e:
            # 返回404页面
            respon_line = 'HTTP / 1.1 404 Not Found\r\n'
            response_header = 'server: PWS1.0\r\nContent-Type: text/html;charset=utf-8\r\n'
            response_body = '<h1>抱歉，您当前访问的网页已经不存在了</h1>'
            response_data = (respon_line + response_header + '\r\n' + response_body).encode('utf-8')
            server_socket.send(response_data)
        else:
            # 请求成功，返回资源内容
            respon_line = "HTTP/1.1 200 OK\r\n"
            response_header = 'server: PWS1.0\r\nContent-Type: text/html;charset=utf-8\r\n'
            response_body = file_data
            response_data = (respon_line + response_header + '\r\n').encode('utf-8') + response_body

            server_socket.send(response_data)
        finally:
            server_socket.close()


def main():
    sever = HttpWebServer()
    sever.start()


if __name__ == '__main__':
    main()
