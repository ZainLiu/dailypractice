class Int_reverse(object):
    def __init__(self,intnum):
        self.intnum = intnum
    def reverseit(self):
        if -10 < self.intnum < 10:
            return self.intnum
        intnum = str(self.intnum)
        if intnum[0] == '-':
            intnum = -int(intnum[1:][::-1])
        else:
            intnum = intnum[::-1]
        return intnum

a = Int_reverse(-6)
b = a.reverseit()
print(b)