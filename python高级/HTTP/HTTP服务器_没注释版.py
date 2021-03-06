import re
import socket


class HttpServer(object):
    def __init__(self):
        http_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        http_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        http_socket.bind(('', 8080))
        http_socket.listen(128)
        self.http_socket = http_socket

    def run(self):
        while True:
            client_socket, addr = self.http_socket.accept()
            self.handle_request(client_socket)

    @staticmethod
    def handle_request(client_socket):
        data = client_socket.recv(1024)
        data_str = data.decode('utf-8')
        path = re.match(r'[^/]+(/[^ ]*)\s', data_str)
        if path:
            page_path = path.group(1)
            if page_path == '/':
                page_path = '/index.html'
        else:
            client_socket.close()
            return
        response_line = 'HTTP/1.1 200 ok\r\n'
        response_header = 'content-type:text/html;charset=utf-8\r\n'
        response_space = '\r\n'
        try:
            with open('static' + page_path, 'rb') as f:
                page_data = f.read()
        except FileNotFoundError:
            response_line = 'HTTP/1.1 404 page_not_found\r\n'
            page_data = '抱歉，您请求的页面已经丢失...'.encode('utf-8')
        response_data = response_line + response_header + response_space
        client_socket.send(response_data.encode('utf-8') + page_data)
        client_socket.close()


def main():
    http_server = HttpServer()
    http_server.run()


if __name__ == '__main__':
    main()
