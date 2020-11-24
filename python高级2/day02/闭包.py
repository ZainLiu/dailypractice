def func(num):
    def show():
        print(num)
    return show

f=func(1)
f()