import threading
import time


class MyThread(threading.Thread):
    def __init__(self, info1, info2):
        super(MyThread, self).__init__()
        self.info1 = info1
        self.info2 = info2

    def test1(self):
        for _ in range(5):
            time.sleep(1)
            print(self.info1)

    def test2(self):
        for _ in range(5):
            time.sleep(1)
            print(self.info2)

    def run(self):
        self.test1()
        self.test2()


my_thread = MyThread('测试一', '测试二')
my_thread2=MyThread('测试3','测试4')

my_thread.start()
my_thread2.start()
