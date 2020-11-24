import sys
class Man(object):
    b = 22

    def __init__(self,age):
        self.age = age

    @classmethod
    def look(cls):
        print(cls)

    def a(self):
        print(self)

    @staticmethod
    def b():
        print('222')


if __name__ == '__main__':
    man = Man(22)
    print(hasattr(man, 'b'))
    man.c = 233
    print(man.c)
    print(sys.getrefcount(man))
