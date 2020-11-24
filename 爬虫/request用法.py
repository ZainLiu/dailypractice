import requests

"""Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"""
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
header = {"User-Agent":user_agent}
response = requests.get("https://i0.taoba.club/h5/static/js/index.6e041cf5.js",headers=header)
print(response.content.decode())
