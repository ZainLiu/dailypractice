def singleinstance(cls):
    instance = {}
    def generateinstance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return generateinstance


@singleinstance
class Hello(object):
    def __init__(self,a):
        self.a = a

hello = Hello(1)
print(hello.a)
hello2 = Hello(2)
print(hello2.a)

class Bye(object):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance