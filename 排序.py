class Sort(object):
    def __init__(self, sort_type, list):
        self.sort_type = sort_type
        self.list = list
    def sort(self):
        if self.sort_type == "mp":
            return self.mp_sort()
        elif self.sort_type == "xz":
            return self.xz_sort()

    def mp_sort(self):
        for j in range(len(self.list)-1,0,-1):
            for i in range(j):
                if self.list[i] > self.list[i+1]:
                    self.list[i], self.list[i+1] = self.list[i+1], self.list[i]
        print(self.list)
        return self.list
    def xz_sort(self):
        for i in range(len(self.list)-1):
            min_index = i
            for j in range(i+1, len(self.list)):
                if self.list[j] < self.list[min_index]:
                    min_index =j
            if min_index != i:
                self.list[i], self.list[min_index] = self.list[min_index], self.list[i]
        return self.list



a=Sort("xz", [2, 1, 3])
print(a.sort())