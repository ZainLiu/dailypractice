class Test1(object):
    def __call__(self, *args, **kwargs):
        print('call run')

t=Test1()
t()