import time


class CountTime(object):
    def __init__(self,func):
        self.__func=func

    def __call__(self, *args, **kwargs):
        st=time.time()
        ret=self.__func()
        print(time.time()-st)
@CountTime
def add():
    sum=0
    for i in range(10000001):
        sum+=i
    print(sum)

add()