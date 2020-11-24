import re
import socket
import sys
import gevent
from gevent import monkey

monkey.patch_all()

class HttpServer(object):
    def __init__(self, port):
        http_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        http_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        http_socket.bind(("", port))
        http_socket.listen(128)
        self.http_socket = http_socket

    def run(self):
        while True:
            handle_socket, addr = self.http_socket.accept()
            gevent.spawn(self.handle_request,handle_socket)
            # self.handle_request(handle_socket)

    def handle_request(self, handle_socket):
        revc_data = handle_socket.recv(1024)
        revc_str = revc_data.decode('utf-8')
        ret = re.match('[^/]+(/[^ ]*)\s', revc_str)
        if ret:
            path = ret.group(1)
            if path == '/':
                path = '/index.html'
        else:
            handle_socket.close()
            return
        response_line = 'HTTP/1.1 200 OK\r\n'.encode('utf-8')
        response_header = 'Content-Type:text/html;charset=utf-8\r\n'.encode('utf-8')
        space_line = '\r\n'.encode('utf-8')
        try:
            with open('static' + path, 'rb')as f:
                response_body = f.read()
        except FileNotFoundError:
            response_line = 'HTTP/1.1 404 NOT FOUND\r\n'.encode('utf-8')
            response_body = "<h1>非常抱歉！请求页面不存在...</h1>".encode('utf-8')

        handle_socket.send(response_line + response_header + space_line + response_body)
        handle_socket.close()


def main():
    if len(sys.argv) != 2:
        print("正确输入格式为：python3 xx.py 端口号")
    elif not sys.argv[1].isdigit():
        print("正确输入格式为：python3 xx.py 端口号")
    else:
        port = int(sys.argv[1])

    http_server = HttpServer(port)
    http_server.run()


if __name__ == '__main__':
    main()
