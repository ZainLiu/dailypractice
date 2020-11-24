class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return "name:%s age:%s"%(self.name,self.age)

class Male(People):
    pass

class Female(People):
    pass

class Factory(object):
    @staticmethod
    def getPeople(gender,name,age):
        if gender == 'M':
            return Male(name, age)
        else:
            return Female(name,age)
a = Factory.getPeople("M","liu",18)
b = Factory.getPeople("F","lucy",18)
d = [1,2,3]
c = (d,4)
print(c)
d[1]=89
print(a,b,c)