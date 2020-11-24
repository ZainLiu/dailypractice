import json
import re

"""数据爬取链接：http://www.jzb48.com/json/get.php?type=index&list=czy"""
# 从文件中读取json数据
with open("./json_data_file/集资榜.json","r",encoding="utf-8") as fb:
    json_data = json.load(fb)
    print(json_data,type(json_data))
jz_data = json.dumps(json_data,ensure_ascii=False)
jz_data2 = re.sub('\\\\',jz_data,'\\')
jz_data3 = json.loads(jz_data2,encoding="utf-8")
print(jz_data3,type(jz_data3))
jz_data3["main_table_data"] =json.loads(jz_data3["main_table_data"])
jz_data3["growth_data"] =json.loads(jz_data3["growth_data"])
jz_data3["percentage_data"] =json.loads(jz_data3["percentage_data"])
jz_data3["advertising_url"] =json.loads(jz_data3["advertising_url"])
with open("../json_data_file/集资榜中文.json","w",encoding="utf8") as f:
    json.dump(jz_data3,f,indent=4,ensure_ascii=False)
# jz_json = json.load(open("./json_data_file/集资榜.json",'rb').decode())
# print(jz_json,type(jz_json))

def get_dict_from_response(response_json):
    """
    从http://www.jzb48.com/json/get.php?type=index&list=czy获取的json数据转化为dict
    :param response_json: bytes类型，例如response.content
    :return: 字典
    """
    # jz_data2 = re.sub('\\\\', response_json, '\\')
    # print(jz_data2,type(jz_data2))
    jz_data3 = json.loads(response_json, encoding="utf-8")
    # print(jz_data3, type(jz_data3))
    jz_data3["main_table_data"] = json.loads(jz_data3["main_table_data"])
    jz_data3["growth_data"] = json.loads(jz_data3["growth_data"])
    jz_data3["percentage_data"] = json.loads(jz_data3["percentage_data"])
    jz_data3["advertising_url"] = json.loads(jz_data3["advertising_url"])

    return jz_data3