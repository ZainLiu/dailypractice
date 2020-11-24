# 方法一
def func1(l):
    if isinstance(l,str):
        l = [int(i) for i in l]
        l.sort(reverse=True)
        for i in range(len(l)):
            if l[i] %2 >0:
                l.insert(0,l.pop(i))
        print(''.join(str(e) for e in l))

# 方法二
def func2(l):
    print(''.join(sorted(l, key=lambda x:int(x)%2==0 and 20 - int(x) or int(x))))

if __name__ == '__main__':
    a = "1982376455"
    func1(a)
    func2(a)