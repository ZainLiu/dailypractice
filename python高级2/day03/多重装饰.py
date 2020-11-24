def func1(func):
    def wrapper():
        print(111111111)
        ret=func()
        print(1111111111)
        return ret
    return wrapper

def func2(func):
    def wrapper():
        print(2222222)
        ret=func()
        print(222222)
        return ret
    return wrapper
@func1
@func2
def show():
    print('hello')
