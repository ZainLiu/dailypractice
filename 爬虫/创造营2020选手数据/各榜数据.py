# https://api.aiiuii.com/v3/variety/single/list?pid=produce&rid=46&table=fast  QQ音乐能量站
# https://api.aiiuii.com/v3/variety/single/list?pid=produce&rid=47&table=fast 微视能量周
# https://api.aiiuii.com/v3/variety/single/list?pid=produce&table=hour&fields=pp_fans腾讯视频撑腰粉丝
# https://api.aiiuii.com/v3/variety/single/list?pid=produce&table=boost&fields=sum,mention,interactive,addoil元气能量加油站
import json

import requests

chuang_top_number = {
    "QQ音乐能量站": 46,
    "微视能量/周": 47,
    "微视能量/总": 48,
    "微视能量/视频": 49,
    "曼妮芬自信补给": 53,
    "真热爱发光帮": 58,
    "荣耀30能量站": 50,
    "ABC能量站": 51,
    "高露洁能量站/总榜": 52,
    "dance赛道": 41,
    "vocal赛道": 42,
    "创作赛道": 43,
    "艺能赛道": 44,
}
nomal_url = "https://api.aiiuii.com/v3/variety/single/list?pid=produce&rid={}&table=fast"
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    }
response = requests.get(nomal_url.format(chuang_top_number["ABC能量站"]),headers=headers)
json_str = response.content.decode()
dict = json.loads(json_str)
with open("./chuang_data_json/各榜数据合集.json",'w',encoding='utf8') as f:
    json.dump(dict,f,ensure_ascii=False,indent=4)