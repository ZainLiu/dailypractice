import json

import requests
#https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?start=0&count=18&loc_id=108288

class DoubanMovieSpider(object):
    def __init__(self):
        self.url_pattern = "https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?start={}&count=18&loc_id=108288"
        self.headers = {
            "Referer": "https://m.douban.com/movie/nowintheater?loc_id=108288",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
        }
    def get_json_from_url(self,url):
        response = requests.get(url,self.headers)
        print(response.content)
        return response.content.decode()
    def get_movie_list(self,json_str):
        dic = json.loads(json_str)
        movie_list = dic['subject_collection_items']
        return movie_list

    def save_movie_list(self,movie_list):
        with open("movies.txt",'a',encoding='utf-8') as f:
            for movie in movie_list:
                json.dump(movie,f,ensure_ascii=False)
                f.write("\n")

    def run(self):
        url = self.url_pattern.format(0)
        json_str = self.get_json_from_url(url)
        movie_list = self.get_movie_list(json_str)
        self.save_movie_list(movie_list)

if __name__ == '__main__':
    a = DoubanMovieSpider()
    a.run()



# class DoubanMovieSpider(object):
#
#     def __init__(self):
#         ''' 初始化方法 '''
#         # 模板URL
#         self.url_pattern = "https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?start={}&count=18&loc_id=108288"
#         # 请求头
#         self.headers = {
#             "Referer": "https://m.douban.com/movie/nowintheater?loc_id=108288",
#             "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36"
#         }
#
#     def get_json_from_url(self, url):
#         '''
#         # 2. 根据这个URL,发送请求获取热映电影json数据
#         :param url: 请求的URL
#         :return: json格式的字符串
#         '''
#         response = requests.get(url, headers=self.headers)
#         return response.content.decode()
#
#     def get_movie_list(self, json_str):
#         '''
#         3. 解析数据(json), 返回电影的列表信息
#         :param json_str:  json字符串
#         :return: 电影的列表信息
#         '''
#         dic = json.loads(json_str)
#         # 通过字典获取电影的列表数据
#         movie_list = dic['subject_collection_items']
#         return movie_list
#
#     def save_movie_list(self, movie_list):
#         '''
#         # 4. 保存数据, 每一个电影信息保存到一行上
#         :param movie_list: 电影列表信息
#         '''
#         # 为了提高写数据的效率,先打开文件在遍历. 每一次打开文件都比较消耗性能的.
#         with open("movies.txt", 'a', encoding='utf8') as f:
#             for movie in movie_list:
#                 json.dump(movie, f, ensure_ascii=False)
#                 f.write("\n")
#
#
#     def run(self):
#         '''
#         这是这个爬虫的入口方法
#         '''
#         # 定义一个变量,用于记录起始索引号
#         url = self.url_pattern.format(0)
#         # 2. 根据这个URL,发送请求获取热映电影json数据
#         json_str = self.get_json_from_url(url)
#         # 3. 解析数据(json), 获取电影列表信息
#         movie_list = self.get_movie_list(json_str)
#         # 4. 保存数据, 每一个电影信息保存到一行上
#         self.save_movie_list(movie_list)