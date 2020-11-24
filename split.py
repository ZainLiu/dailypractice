import time
def programspeed(func):
    def wrapper():
        # def inner(*args,**kwargs):
            # print(content)
        start = time.time()
        func()
        end = time.time()
        programtime = end-start
        print(programtime)
            # return inner
    return wrapper

@programspeed
def helloworld():
    a = 1
    for i in range(1,100000):
        a*=i
    print(a)

if __name__ == '__main__':
    helloworld()


