import requests
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    }
url = "https://www.baidu.com"
response = requests.get(url,headers=headers)
print(type(response.cookies))

cookies = requests.utils.dict_from_cookiejar(response.cookies)
print(cookies)