import time
import threading


def gen_coroutine(f):
    def wrapper(*args, **kwargs):
        gen_f = f()
        r = next(gen_f)
        def fun(g):
            ret = next(g)
            try:
                gen_f.send(ret)
            except StopIteration:
                pass
        threading.Thread(target=fun,args=(r,)).start()
    return wrapper

def login_io():
    print("开始执行IO操作")
    time.sleep(5)
    print("完成IO操作，yield返回操作结果")
    yield "io result"


@gen_coroutine
def req_a():
    print("开始处理请求req_a")
    ret = yield login_io()
    print("ret:%s"%ret)
    print("完成处理请求req_a")


def req_b():
    print("开始处理请求req_b")
    time.sleep(2)
    print("完成处理请求req_b")

def main():
    req_a()
    req_b()
    while 1:
        pass

if __name__ == '__main__':
    main()
