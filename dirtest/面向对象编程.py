class Hello(object):
    bb = None

    def __init__(aaa, b):
        aaa.bb = b

    def hello(aaa):
        print(aaa.bb)


a = Hello(2)
print(a.bb)