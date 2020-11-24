list1 = []


def print_sht(content):
    def func1(func):
        def warpper(*args, **kwargs):
            func(*args, **kwargs)

        print(content)
        list1.append(content)
        return warpper

    return func1


@print_sht('你好')  # 装饰器在程序运行时会自运行运行，封装成一个运行环境，等待传入函数
def add(a, b):
    print(a + b)

print(list1)
add(1, 2)
"""
你好
['你好']
3
"""
