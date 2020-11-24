import requests
import re
import json

class KrSpider(object):
    def __init__(self):
        self.url = "http://36kr.com/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
        }
    def get_page_from_url(self):
        response = requests.get(self.url,headers=self.headers)
        return response.content.decode()
    def get_data_from_page(self,page):
        json_str = re.findall('<script>var props=(.+?),locationnal=.*</script>',page)[0]
        dic = json.loads(json_str)
        return dic
    def save_data(self,data):
        with open("kr.json",'w',encoding='utf-8') as f:
            json.dump(data,f,ensure_ascii=False,indent=2)

    def save_page(self,page):
        with open("./down_temp/36kr_homepage.html",'wb') as f:
            f.write(page.encode())
    def run(self):
        page = self.get_page_from_url()
        self.save_page(page)
        data = self.get_data_from_page(page)
        self.save_data(data)

if __name__ == '__main__':
    krs = KrSpider()
    krs.run()


# class krSpider(object):
#     def __init__(self):
#         self.url = 'http://36kr.com/'
#         self.headers = {
#             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
#         }
#
#     def get_page_from_url(self):
#         response = requests.get(self.url, headers=self.headers)
#         return response.content.decode()
#
#     def get_data_from_page(self, page):
#         '''# 解析页面, 提取需要的数据'''
#         json_str = re.findall('<script>var props=(.+?),locationnal=.*</script>', page)[0]
#         # with open('kr.txt', 'w', encoding='utf8') as f:
#         #     f.write(json_str)
#         dic = json.loads(json_str)
#         return dic
#
#     def save_data(self, data):
#         with open('kr.json', 'w', encoding='utf8') as f:
#             json.dump(data, f, ensure_ascii=False, indent=2);
#
#
#     def run(self):
#         # 准备URL
#         # 发送请求获取响应数据
#         page = self.get_page_from_url()
#         # 解析页面, 提取需要的数据
#         data = self.get_data_from_page(page)
#         # 保存数据
#         self.save_data(data)
#
# if __name__ == '__main__':
#     krs = krSpider()
#     krs.run()
#
