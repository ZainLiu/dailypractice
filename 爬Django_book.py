import pdfkit
import time
def scrapy_django_book():
    url = 'http://djangobook.py3k.cn/2.0/chapter{:0>2d}/'
    confg = pdfkit.configuration(wkhtmltopdf='D:/编辑软件/html转pdf工具/wkhtmltopdf/bin/wkhtmltopdf.exe')
    file_name = 'D:/网站好文章保存pdf/Django教程/第{:0>2d}章.pdf'
    for i in range(1,21):
        des_url = url.format(i)
        des_file_name = file_name.format(i)
        print(des_url,des_file_name)
        pdfkit.from_url(des_url, des_file_name, configuration=confg)
        time.sleep(1)

def scrapy_jianshu():
    url = 'https://www.jianshu.com/p/dc252b5efca6'
    confg = pdfkit.configuration(wkhtmltopdf='D:/编辑软件/html转pdf工具/wkhtmltopdf/bin/wkhtmltopdf.exe')
    file_name = 'C:/Users/86186/Desktop/跳跃表.pdf'
    pdfkit.from_url(url, file_name, configuration=confg)
if __name__ == '__main__':
    scrapy_jianshu()