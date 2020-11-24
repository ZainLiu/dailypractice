import time
import threading


def login_io(callback):
    """将好事的操作交给另一个线程来处理"""

    def fun(cb):  # 回调函数作为参数
        print("开始执行IO操作")
        time.sleep(2)
        print("完成IO操作")
        cb("io result")
    threading.Thread(target=fun, args=(callback,)).start()


def on_finish(ret):
    """回调函数"""
    print("""开始执行回调函数on_finish""")
    print("ret: %s"%(ret,))
    print("完成执行回调函数on_finsh")


def req_a():
    print("开始请求处理req_a")
    login_io(on_finish)
    print("离开处理请求req_a")

def req_b():
    print("start req_b")
    time.sleep(5)
    print("finish req_b")

def main():
    req_a()
    req_b()
    while 1:
        pass

if __name__ == '__main__':
    main()
