class Test(object):
    def __init__(self,func):
        self.__func=func

    def __call__(self, *args, **kwargs):
        print('wrapper context')
        self.__func(*args,*kwargs)
@Test
def show(name):
    print('hello',name)

show('Lucy')