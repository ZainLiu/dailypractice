import sys

from . import WebFrame
import socket
import re
import multiprocessing


class WEBServer(object):
    def __init__(self, port):
        self.__tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.__tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.__tcp_server_socket.bind(("",port))
        self.__tcp_server_socket.listen(128)

    def __service_client(self,new_socket,frame_module):
        request = new_socket.recv(1024).decode("utf-8")
        request_lines = request.splitlines()
        file_name = ""
        ret = re.match(r"[^/]+(/[^ ]*)",request_lines[0])
        if ret:
            file_name = ret.group(1)
            if file_name == "/":
                file_name = "/index.html"
        response = "HTTP/1.1 200 ok\r\n"
        response += "\r\n"
        if file_name.endswith('.html'):
            env = {"PATH_INFO": file_name}
            body = frame_module.application(env,self.start_response)

            header = "HTTP/1.1 %s\r\n"%self.status
            for t in self.params:
                header += "%s:%s\r\n"%t
            data = header + '\r\n' + body
            new_socket.send(data.encode('utf-8'))
        else:
            try:
                f = open("./static" + file_name, "rb")
            except:
                response = "HTTP/1.1 404 NOT FOUND\r\n"
                response += "\r\n"
                response += "-----file not found-----"
                new_socket.send(response.encode("utf-8"))
            else:
                html_content = f.read()
                f.close()
                response = "HTTP/1.1 200 OK\r\n"
                response += "\r\n"
                new_socket.send(response.encode("utf-8"))
                new_socket.send(html_content)

        new_socket.close()

    def start_response(self,status,params):
        self.status = status
        self.params = params

    def run(self, frame_module):
        while True:
            new_socket, client_addr = self.__tcp_server_socket.accept()
            p = multiprocessing.Process(target=self.__service_client, args=(new_socket,frame_module))
            p.start()
            new_socket.close()
        self.__tcp_server_socket.close()


def main():
    with open('server.conf',"r") as f:
        conf_str = f.read()
    dict = eval(conf_str)
    port = dict['port']
    module_str = dict["module"]
    sys.path.append('dynamic')
    frame_module = __import__(module_str)
    webServer = WEBServer(port)
    webServer.run(frame_module)


if __name__ == '__main__':
    main()





