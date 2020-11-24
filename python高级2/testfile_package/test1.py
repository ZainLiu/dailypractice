class A(object):
    def __init__(self):
        print("enter A")
        print("leave A")
class B(object):
    def __init__(self):
        print("enter B")

        print("leave B")
class C(A):
    def __init__(self):
        print("enter C")
        super(C, self).__init__()
        print("leave C")
class D(A):
    def __init__(self):
        print("enter D")
        super(D, self).__init__()
        print("leave D")
class E(B, C):
    def __init__(self):
        print("enter E")
        B.__init__(self)
        C.__init__(self)
        print("leave E")
class F(E, D):
    def __init__(self):
        print("enter F")
        E.__init__(self)
        D.__init__(self)
        print("leave F")
print(F.__mro__)
f = F()
"""
(<class '__main__.F'>, <class '__main__.E'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.A'>, <class 'object'>)
enter F
enter E
enter B
leave B
enter C
enter D
enter A
leave A
leave D
leave C
leave E
enter D
enter A
leave A
leave D
leave F
"""
