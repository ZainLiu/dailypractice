import requests
url = "https://www.numpy.org.cn/"
response = requests.get(url,verify=False)
print(response.content)