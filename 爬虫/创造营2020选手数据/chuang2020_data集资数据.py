import json
import re
import requests


def get_dict_from_response(response_json):
    """
    从http://www.jzb48.com/json/get.php?type=index&list=czy获取的json数据转化为dict
    :param response_json: bytes类型，例如response.content
    :return: 字典
    """
    jz_data = json.loads(response_json, encoding="utf-8")
    jz_data["main_table_data"] = json.loads(jz_data["main_table_data"])
    jz_data["growth_data"] = json.loads(jz_data["growth_data"])
    jz_data["percentage_data"] = json.loads(jz_data["percentage_data"])
    jz_data["advertising_url"] = json.loads(jz_data["advertising_url"])

    return jz_data

jz_url = "http://www.jzb48.com/json/get.php?type=index&list=czy"
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    }
response = requests.get(jz_url,headers=headers)
response_json = response.content
dict = get_dict_from_response(response_json)
with open("./chuang_data_json/集资榜中文.json","w",encoding="utf8") as f:
    json.dump(dict,f,indent=4,ensure_ascii=False)

