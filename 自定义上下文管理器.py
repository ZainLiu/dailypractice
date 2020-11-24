class Hello(object):
    def __enter__(self):
        self.__handel = [1,2,3]
        return self.__handel
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__handel.append(5)

with Hello() as b:
    print(b,id(b))
print(b,id(b))