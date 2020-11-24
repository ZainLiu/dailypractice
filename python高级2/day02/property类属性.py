class Account(object):
    def __init__(self, name, money):
        self.__username = name
        self.__userbalance = money
        self.__createtime = 9

    @property
    def name(self):
        return self.__username

    @property
    def balance(self):
        return self.__userbalance

    @property
    def time(self):
        return self.__createtime

    @time.deleter
    def time(self):
        del self.__createtime

    # name=property(get_name)
    # money=property(get_balance)
    # time=property(get__createtime,del_createtime)


li = Account('li', 999)
print(li.name)
print(li.balance)
print(li.name)
print(li.time)
del li.time
print(li.time)
