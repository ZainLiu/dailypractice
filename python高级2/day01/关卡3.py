import copy
list1 = [1,2,['a','b'],('c','d')]
list2 = list1
list3 = copy.copy(list1)
list4 = copy.deepcopy(list1)
list1.append(3)
tuple1 = (10,10)
list1[2].append({100})
list1[3] = list1[3] + tuple1
dict1 = {}
dict1['1'] = 1111
list1[2].append(dict1)
print(list1)
#(1)结果是：[1, 2, ['a', 'b', {100}, {'1': 1111}], ('c', 'd', 10, 10), 3]
print(list2)
#(2)结果是：[1, 2, ['a', 'b', {100}, {'1': 1111}], ('c', 'd', 10, 10), 3]
print(list3)
#(3)结果是：[1, 2, ['a', 'b', {100}, {'1': 1111}], ('c', 'd')]
print(list4)
#(4)结果是：[1, 2, ['a', 'b'], ('c', 'd')]
