class Car(object):
    def __init__(self,name,loss):
        self.name = name
        self.loss = loss

    def getName(self):
        return self.name

    def getPrice(self):
        return self.loss[0]

    def getLoss(self):
        return self.loss[1]*self.loss[2]
bmw = Car("宝马",[60,9,500])
print(getattr(bmw,"name"))
print(bmw.__dir__())