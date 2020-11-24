class Account(object):
    def __init__(self, name, money):
        self.__name = name
        self.__balance = money

    @property
    def name(self):
        return self.__name

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, money):
        if isinstance(money, int):
            if money >= 0:
                self.__balance = money
            else:
                raise ValueError('输入金额不正确')
        else:
            raise ValueError('输入金额不是数字')


ac = Account('Tom', 100)
print(ac.name)
print(ac.balance)
ac.balance = 1000
print(ac.balance)
