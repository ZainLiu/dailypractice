import requests
import time
import random

class TiebaCrawler(object):
    url = "http://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    }
    sleep_list = [i/100 for i in range(1,11)]

    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

    def get_url_list(self):
        return [self.url.format(self.name,(i-1)*50) for i in range(self.start,self.end+1)]

    def download_from_url(self,url):
        response = requests.get(url,headers=self.headers)
        return response.content

    def write_to_file(self, filename, content):
        with open("./Nikki/"+filename,"wb") as f:
            f.write(content)
    def run(self):
        url_list = self.get_url_list()
        for url in url_list:
            sleep_time = random.random()
            content = self.download_from_url(url)
            file_name = "{}_第{}页.html".format(self.name,url_list.index(url)+1)
            self.write_to_file(file_name,content)
            time.sleep(sleep_time)
        print("写入完成")

if __name__ == '__main__':
    ts = TiebaCrawler("闪耀暖暖",1,100)
    ts.run()
# 定义一个贴吧爬虫类
# class TiebaCrawler(object):
#     # 基础URL
#     basic_url = "http://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}"
# #     初始化方法
#     def __init__(self, name, start, end):
#         self.name = name
#         self.start = start
#         self.end = end
#
#     #  2.1  根据规律生成访问贴吧内容页面的URL,放到列表中
#     def get_url_list(self):
#         # 定义一个list
#         # url_list = []
#         # # 生成URL放入list中
#         # for i in range(self.start, self.end+1):
#         #     url = self.basic_url.format(self.name, (i-1)*50)
#         #     url_list.append(url)
#         #  #返回list的列表
#         # return url_list
#         # 扁平化写法: 推荐,简洁
#         return [self.basic_url.format(self.name, (i-1)*50) for i in range(self.start, self.end+1)]
#
#     # 写一个方法下载URL中内容
#     def download_from_url(self, url):
#         response = requests.get(url)
#         return response.content
#
#     # 写一个方法把内容写到文件中
#     def write_to_file(self, filename, content):
#         with open(filename, "wb") as f:
#             f.write(content)
#
#     # 下载方法,存储主逻辑
#     def run(self):
#         # 2.1  根据规律生成访问贴吧内容页面的URL,放到列表中
#         url_list = self.get_url_list()
#         # print(url_list)
#         # 遍历URL,发送请求,获取内容
#         for url in url_list:
#            content = self.download_from_url(url)
#            # 文件名称: 贴吧名称_页码
#            file_name = "{}_第{}页.html".format(self.name, url_list.index(url)+1)
#            # 把内容页面写到文件中
#            self.write_to_file(file_name, content)
#         print("写入完成")
#
# if __name__ == '__main__':
#     # 思路: 从用户角度去考虑代码写法
#     # 你要下载那个贴吧内容创建一个对象,指定贴吧名称,起始页和结束页,调用run方法就可以了
#     ts = TiebaCrawler("电影", 1, 5)
#     ts.run()