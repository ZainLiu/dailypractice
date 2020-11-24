import requests
import sys
import json

word = sys.argv[1]
print(word)
url = 'http://fy.iciba.com/ajax.php?a=fy'
data = {
    'f':'auto',
    't':'auto',
    'w':word
}
response = requests.post(url,data)
# print(response.content)
# with open('worning.html', "wb") as f:
#     f.write(response.content)
dic = json.loads(response.content.decode())
print(dic['content'])
rs = dic['content'].get('out',None)
if not rs:
    rs = dic['content']['word_mean'][0]

print(rs)


################################################################################
# 表单数据
# data = {
#     'name': 'lao wang'
# }
# # 发送POST请求
# response = requests.post("http://httpbin.org/post", data=data)
#
# print(response.content.decode())