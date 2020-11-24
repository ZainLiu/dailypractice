def decorate(string):
    def wrapper(func):
        str1 = string

        def inner(*args, **kwargs):
            print('这是' + str1)
            return func(*args, **kwargs)

        return inner

    return wrapper


@decorate('加法')
def add(a, b):
    return a + b


@decorate('减法')
def sub(a, b):
    return a - b


@decorate('乘法')
def mul(a, b):
    return a * b


@decorate('除法')
def div(a, b):
    return a / b


if __name__ == '__main__':
    print(add(10, 5))
    print(sub(10, 5))
    print(mul(10, 5))
    print(div(10, 5))
