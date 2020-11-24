import requests

session = requests.session()
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
}
login_url = "http://www.renren.com/PLogin.do"
data = {
    "email":"15565280933",
    "password":"a123456"
}
response = session.post(login_url,data=data,headers=headers)
print(response.status_code)
print(response.content.decode())
profile_url = "http://www.renren.com/965194180/profile"
response = session.get(profile_url)
with open("./down_temp/个人主页.html","wb") as f:
    f.write(response.content)


# # * 使用requests模块中的session对象,记录登录后的cookie信息
# # 步骤:
# # 1. 获取session对象
# session = requests.session()
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
# }
#
# # 2. 使用session对象,进行登录,登录后seesion对象会记录用户相关的cookie信息
# # 发送URL是什么? 需要传入的数据是什么?
# login_url = "http://www.renren.com/PLogin.do"
# data = {
#     "email": "15565280933",
#     "password": "a123456"
# }
#
# response = session.post(login_url, data=data, headers=headers)
# print(response.status_code)
# print(response.content.decode())
# # 3. 再使用记录cookie信息对象session访问个人主页
# profile_url = "http://www.renren.com/965194180/profile"
# response = session.get(profile_url)
# with open("个人主页.html", "wb") as f:
#     f.write(response.content)