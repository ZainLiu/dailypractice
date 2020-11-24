import gevent
import time
from gevent import monkey

# 打补丁，让gevent框架识别耗时的操作，比如：time.sleep，网络延时请求等
monkey.patch_all()


def work1(num):
    for _ in range(num):
        print('---work1---')
        time.sleep(0.2)


def work2(num):
    for _ in range(num):
        print('---work2---')
        time.sleep(0.1)


if __name__ == '__main__':
    g1 = gevent.spawn(work1, 5)
    g2 = gevent.spawn(work2, 5)
    g1.join()
    g2.join()
