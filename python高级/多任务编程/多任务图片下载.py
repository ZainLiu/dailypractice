import urllib.request

import gevent
import time

from gevent import monkey

monkey.patch_all()


def download_img(img_url, img_name):
    try:
        print(img_name)
        response = urllib.request.urlopen(img_url)
        with open(img_name, 'wb') as img_file:
            while True:
                img_date = response.read(1024)
                if img_date:
                    img_file.write(img_date)
                else:
                    break
    except Exception as e:
        print('图片下载异常：', e)
    else:
        print(f'图片下载成功{img_name}')


if __name__ == '__main__':
    # 准备图片地址
    img_url1 = "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=551346117,2593226454&fm=27&gp=0.jpg"
    img_url2 = "https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=829730016,3409799239&fm=27&gp=0.jpg"
    img_url3 = "https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1815077192,817368579&fm=27&gp=0.jpg"
    g1 = gevent.spawn(download_img, img_url1, '1.jpg')
    g2 = gevent.spawn(download_img, img_url2, '2.jpg')
    g3 = gevent.spawn(download_img, img_url3, '3.jpg')
    g1.join()
    gevent.joinall([g2, g3])
