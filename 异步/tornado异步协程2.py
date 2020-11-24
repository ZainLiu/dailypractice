import time
import threading

gen = None

def gen_coroutine(f):
    def wrapper(*args, **kwargs):
        global gen
        gen = f()
        next(gen)
    return wrapper


def login_io():
    def fun():
        print("开始执行IO操作")
        global gen
        time.sleep(5)
        try:
            print("完成IO操作，并send结果唤醒挂起的程序并继续执行")
            gen.send("io result")
        except StopIteration:
            pass
    threading.Thread(target=fun)
@gen_coroutine
def req_a():
    print("开始处理请求req_a")
    ret = yield login_io()
    print("ret: %s"%(ret,))
    print("完成处理请求req_a")

def req_b():
    print("开始处理请求req_b")
    time.sleep(2)
    print("完成处理请求req_b")


def main():
    req_a()
    req_b()



