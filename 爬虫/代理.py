import random
import requests

# 1. 准备代理列表
"""
# "http":"http://14.118.252.64:6666"
          # "https":"https://114.99.30.126:18118"
          "http": "http://121.228.8.93:8118"
"""
proxies = [
    {'http': '121.8.98.198:80'},
    {'http': '39.108.234.144:80'},
    {'http': '125.120.201.68:808'},
    {'http': '120.24.216.39:60443'},
    {'http': '121.8.98.198:80'},
    {'http': '121.8.98.198:80'}
]

# 2. 随机选出一个代理
for i in proxies:
    # proxy = random.choice(proxies)
    print(i)
    try:
        response = requests.get("http://www.baidu.com", proxies=i, timeout=3)
        print(response.status_code)
    except Exception as ex:
        print("代理有问题: %s" % i)