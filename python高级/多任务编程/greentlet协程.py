import greenlet
import time


def work1():
    for _ in range(5):
        print('---work1---')
        time.sleep(0.5)
        g2.switch()


def work2():
    for _ in range(5):
        print('---work2---')
        time.sleep(0.5)
        g1.switch()


if __name__ == '__main__':
    g1 = greenlet.greenlet(work1)
    g2 = greenlet.greenlet(work2)
    g1.switch()
