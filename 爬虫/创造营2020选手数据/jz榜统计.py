import requests
url = "https:\\www.toutiao.com\i6828748005709971979/?timestamp=1593152922&app=news_article&group_id=6828748005709971979&use_new_style=1&req_id=2020062614284201001402610926BC1243"
headers = {
'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Mobile Safari/537.36'
    }
cookies = {'tt_webid':'6842548179766904334'}
response = requests.get(url,headers=headers,cookies=cookies)
print(response.content)