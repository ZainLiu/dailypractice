class Student(object):
    def __init__(self):
        self.__students = dict()

    def __getitem__(self, item):
        if item not in self.__students:
            return None
        return self.__students[item]

    def __setitem__(self, key, value):
        self.__students[key] = value

    def __delitem__(self, key):
        if key in self.__students:
            del self.__students[key]

    def __len__(self):
        return len(self.__students)


sm = Student()
sm[1] = 'tom'
print(sm[1])
