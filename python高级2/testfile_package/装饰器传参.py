# 定义一个可以传参的装饰器
def set_arg(string):
    print('set_arg_start')

    def zhuangshi(func):
        print('zhuangshi_start')

        def wapper():
            print('start')
            func(string)
            print('end')

        return wapper

    return zhuangshi


@set_arg('Lucy')
def hello(name):
    print('hello', name)


hello()
"""
set_arg_start
zhuangshi_start
start
hello Lucy
end
"""