class Hello(object):
    a = 2333
    b = 4333
    def get_1(self):
        return self.a + self.b

    @classmethod
    def get_2(cls):
        return cls.a+cls.b

    @classmethod
    def get_3(cls):
        return cls.get_2()

    @staticmethod
    def get_4():
        return "hello"


print(Hello.get_4())