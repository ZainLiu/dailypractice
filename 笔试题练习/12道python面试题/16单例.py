# 装饰器方法
def singleton(cls):
    instance = {}
    def wrapper(*args,**kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapper

@singleton
class Temple(object):
    def __init__(self,name):
        self.name = name

    def get_name(self):
        print(self.name)

class Singleton1(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self,name):
        self.name = name
    def get_name(self):
        print(self.name)
class Hello(Singleton1):
    pass
if __name__ == '__main__':

    a= Temple('liu')
    a.get_name()
    b = Temple("zhenyu")
    b.get_name()

    a = Hello('liu')
    a.get_name()
    b = Hello("zhenyu")
    b.get_name()
    print(a is b)