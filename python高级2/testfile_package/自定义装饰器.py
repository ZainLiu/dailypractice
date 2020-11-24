def setFunc(func):
    def wrapper(s):
        print('Start')
        func(s)
        print('End')

    return wrapper


@setFunc
def show(s):
    print('Hello %s' % s)


show('Tom')