import time


def get_time(func):
    def wrapper():
        start = time.time()
        func()
        print(time.time() - start)

    return wrapper


@get_time
def add():
    sum = 0
    for i in range(1000001):
        sum += i
    print(sum)

    pass
add()
