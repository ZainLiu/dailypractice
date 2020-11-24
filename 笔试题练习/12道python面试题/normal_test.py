def atoi(s):
    num = 0
    i = 0
    for v in s:
        for j in range(10):
            i+=1
            if v == str(j):
                num = num * 10 + j
                break
    print(i)
    return num


if __name__ == '__main__':
    a = atoi('123')
    print(a,type(a))