class Single(object):
    def __init__(self,name):
        self.name = name

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Single, "_instance"):
            Single._instance = Single(*args, **kwargs)
        return Single._instance
    def __str__(self):
        return self.name

class Single2(object):
    _instance = None
    _is_first_init = False
    def __init__(self, name):
        # if not self._is_first_init:
        self.name = name
            # self._is_first_init = True
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance
    def __str__(self):
        return self.name

s3 = Single2("s3")
s4 = Single2("s4")

s1 = Single.instance("s1")
s2 = Single.instance("s2")
print(s1,s2,s3,s4)
