from mmap import mmap
def process(e):
    print(e)

def get_lines():
    with open('./hello.log','rb') as f:
        return f.readlines()

def get_lines_1():
    with open('./hello.log','rb') as f:
        for i in f:
            yield i
def get_lines_2():
    with open('./hello.log','rb') as f:
        for i in f:
            yield i

def get_lines_3():
    l = []
    with open('./hello.log', 'rb') as f:
        data = f.readlines(100)
    l.append(data)
    # print(data)
    yield l

def get_lines_4(fb):
    with open(fb,'r+') as f:
        m = mmap(f.fileno(),0)
        tmp = 0
        for i, char in enumerate(m):
            if char == b'\n':
                yield m[tmp:i+1].decode()
                tmp = i+1
if __name__ == '__main__':
    # for e in get_lines_3():
    #     process(e)
    #     print('+++++++++')

    # mmap用法:
    for i in get_lines_4("./hello.log"):
        print(i)
    # while get_lines_3():
    #     pr
    # with open('./hello.log', 'rb') as f:
    #     while True:
    #         data = f.readlines()
    #         if not data:
    #             break
    #         print(data)
    #         print('______________')