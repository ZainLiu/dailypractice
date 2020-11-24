a = ['b','c','d','c','a','a']
l2 = list(set(a))
l2.sort(key=a.index)
print(l2, (a.index))
