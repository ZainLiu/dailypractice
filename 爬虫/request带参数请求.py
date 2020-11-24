import requests
url = "https://www.sogou.com/web"
key = input("请录入你要搜索的内容：")
params = {"query":key}
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    }

response = requests.get(url,headers=headers,params=params)
content = response.content.decode()
print(content)
