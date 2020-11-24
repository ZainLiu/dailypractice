import requests
from lxml import etree
import json
import re

class TiebaSpider(object):
    def __init__(self,name):
        self.url = 'https://tieba.baidu.com/f?kw='+name+'&mo_device=1&pn={}&'
        self.name = name
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
        }
        self.domain_url = "https://tieba.baidu.com"

    def get_page_from_url(self,url):
        response = requests.get(url,headers=self.headers)
        return response.content.decode()

    def get_data_from_page(self,page):
        element = etree.HTML(page)
        lis = element.xpath('//li[@class="t1_shadow tl tl_shaow_new"]')
        data_list = []
        for li in lis:
            item = {}
            item["title"] = li.xpath('//li[@class="tl_shadow tl_shadow_new"]')
            item["detail_url"] = self.domain_url + li.xpath('./a/@href')[0]
            item["imgs"] = self.get_imgs_from_url(item["detail_url"])
            data_list.append(item)

        page_size = int(re.findall('"page_size":(\d+)',page)[0])
        current_page = int(re.findall('"current_page":(\d+)',page)[0])
        total_page = int(re.findall('"total_page":(\d+)',page)[0])
        if current_page < total_page:
            next_url = self.url.format(current_page*page_size)
        else:
            next_url = None
        print(next_url)
        return data_list,next_url

    def get_imgs_from_url(self,detail_url):
        """从详情页提取图片URL列表"""
        detail_url_pattern = detail_url+'&pn={}'
        imgs = []
        while True:
            detail_page = self.get_page_from_url(detail_url)
            element = etree.HTML(detail_page)
            img_urls = element.xpath('//div[@data-class="BDE_Image"]/@data-url')

            for img_url in img_urls:
                img_url = requests.utils.unquote(img_url)
                img_url = img_url.split('src=')[1]
                imgs.append(img_url)

            print(detail_url)
            page_sizes = re.findall('"page_size":(\d+)',detail_page)

            if len(page_sizes) == 0:
                break

            page_size = int(page_sizes[0])
            c

# """
# 爬取某个贴吧里的所有帖子，获取每个帖子的标题，连接和帖子中图片
#
# 1. 准备URL
# https://tieba.baidu.com/f?kw=吧名&mo_device=1&pn=0&
# 2. 发送请求, 获取响应数据
# 3. 解析数据, 提取需要数据
# 4. 保存数据
#
# 列表页的分页
# URL规律:
# 第1页: https://tieba.baidu.com/f?kw=%E6%9D%8E%E5%86%B0%E5%86%B0&mo_device=1&pn=0&
# 第2页: https://tieba.baidu.com/f?kw=%E6%9D%8E%E5%86%B0%E5%86%B0&mo_device=1&pn=50&
# 第3页: https://tieba.baidu.com/f?kw=%E6%9D%8E%E5%86%B0%E5%86%B0&mo_device=1&pn=100&
#
# 提取详情页的图片URL信息
# """
#
# class TeibaSpider(object):
#
#     def __init__(self, name):
#         # URl, 在pn={}
#         self.url = 'https://tieba.baidu.com/f?kw='+name+'&mo_device=1&pn={}&'
#         # 记录吧名
#         self.name = name
#         # 请求头
#         self.headers = {
#             'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
#         }
#         # 贴吧域名(用于补全URL)
#         self.domain_url = 'https://tieba.baidu.com'
#
#     def get_page_from_url(self, url):
#         """2. 发送请求, 获取响应数据"""
#         response = requests.get(url, headers=self.headers)
#         return response.content.decode()
#
#     def get_data_from_page(self, page):
#         """解析页面内容, 提取数据"""
#         # 把页面内容转换为Element对象
#         element = etree.HTML(page)
#         # 1. 先分组, 获取包含帖子的li标签列表
#         lis = element.xpath('//li[@class="tl_shadow tl_shadow_new"]')
#         # print(lis)
#         # print(len(lis))
#         # 定义列表, 用于存储数据
#         data_list = []
#         # 2. 遍历lis, 在使用XPATH提取需要数据
#         for li in lis:
#             item = {}
#             item['title'] = li.xpath('./a/div[@class="ti_title"]/span/text()')[0]
#             item['detail_url'] = self.domain_url + li.xpath('./a/@href')[0]
#             item['imgs'] =  self.get_imgs_from_url(item['detail_url'])
#
#             # print(item)
#             data_list.append(item)
#
#         # "page_size":50,"offset":0,"current_page":1,"total_page":658
#         # 1. 提取每一页有多少条数据
#         page_size = int(re.findall('"page_size":(\d+)', page)[0])
#         # 2. 获取当前页号
#         current_page = int(re.findall('"current_page":(\d+)', page)[0])
#         # 3. 获取总页数
#         total_page = int(re.findall('"total_page":(\d+)', page)[0])
#         # 如果有下一页, 就生成下一页URL
#         if current_page < total_page:
#             # 第1页:  0     1
#             # 第2页:  50    current_page * page_size  2
#             # 第3页:  100   current_page * page_size
#             #
#             next_url = self.url.format(current_page * page_size)
#         else:
#             next_url = None
#
#         print(next_url)
#         # 返回数据
#         return data_list, next_url
#
#     def get_imgs_from_url(self, detail_url):
#         """从详情页中提取图片URL列表"""
#         # 准备详情页的URL模板
#         detail_url_pattern = detail_url + '&pn={}'
#         # 注意: 把imgs放到循环外边
#         imgs = []
#
#         while True:
#             # 1. 发送请求, 获取响应数据
#             detail_page = self.get_page_from_url(detail_url)
#             # 2. 提取的图片URL
#             element = etree.HTML(detail_page)
#             img_urls= element.xpath('//div[@data-class="BDE_Image"]/@data-url')
#
#             for img_url in img_urls:
#                 # requests.utils.quote() 对字符串进行URL编码, 把所有特殊符号和中文 => 百分号形式
#                 # url解码:  百分号形式 => 转为普通字符串
#                 img_url = requests.utils.unquote(img_url)
#                 img_url = img_url.split('src=')[1]
#                 imgs.append(img_url)
#
#             # "page_size":30,"offset":0,"current_page":1,"total_page":1896
#             print(detail_url)
#             # 1. 提取每一页有多少条数据
#             page_sizes =  re.findall('"page_size":(\d+)', detail_page)
#             # print(page_sizes)
#             # 有些时候个别页面中, 无法获取到page_size信息, 如果没有获取到就是没有下一页, 退出循环即可
#             if len(page_sizes) == 0:
#                 break
#
#             page_size = int(page_sizes[0])
#             # 2. 获取当前页号
#             current_page = int(re.findall('"current_page":(\d+)', detail_page)[0])
#             # 3. 获取总页数
#             total_page = int(re.findall('"total_page":(\d+)', detail_page)[0])
#             # 如果有下一页, 就生成下一页URL
#             if current_page < total_page:
#                 # 第1页:  0     1
#                 # 第2页:  50    current_page * page_size  2
#                 # 第3页:  100   current_page * page_size
#                 #
#                 detail_url = detail_url_pattern.format(current_page * page_size)
#             else:
#                 break
#
#         print(imgs)
#         # 3. 返回图片的URL列表
#         return imgs
#
#     def save_data(self, data_list):
#         """保存数据"""
#         file_name = "{}.jsonlines".format(self.name)
#         with open(file_name, 'a', encoding='utf-8') as f:
#             for data in data_list:
#                 json.dump(data, f, ensure_ascii=False)
#                 f.write('\n')
#
#     def run(self):
#         # 1. 准备URL
#         url = self.url
#         # 使用循环不断获取下一页, 直到没有下一页了
#         while url:
#             # 2. 发送请求, 获取响应数据
#             page = self.get_page_from_url(url)
#             # 3. 解析数据, 提取需要数据
#             data_list, url = self.get_data_from_page(page)
#             # 4. 保存数据
#             self.save_data(data_list)
#
# if __name__ == '__main__':
#     # tbs = TeibaSpider('李冰冰')
#     tbs = TeibaSpider('做头发')
#     tbs.run()
