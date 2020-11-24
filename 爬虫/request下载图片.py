# https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589625794297&di=3f533034e5d8f2bfdac19679ae749686&imgtype=0&src=http%3A%2F%2Fdingyue.ws.126.net%2F2020%2F0423%2F7a59e71bj00q98v8l000yc000hs00gkm.jpg
import requests

response = requests.get("""https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589625794297&di=3f533034e5d8f2bfdac19679ae749686&imgtype=0&src=http%3A%2F%2Fdingyue.ws.126.net%2F2020%2F0423%2F7a59e71bj00q98v8l000yc000hs00gkm.jpg""")
content = response.content
print(content)
with open("nene.jpg","wb") as f:
    f.write(content)