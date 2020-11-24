import copy
list1=[1,2,['a','b'],('c','d')]
list2=list1
list3=copy.copy(list1)
list4=copy.deepcopy(list1)
list1.append(3)
# print(list3)#[1, 2, ['a', 'b'], ('c', 'd')]
# print(list4)#[1, 2, ['a', 'b'], ('c', 'd')]
# print(list2)#[1, 2, ['a', 'b'], ('c', 'd'), 3]
tuple1=(10,10)
list1[2].append({100})
# print(list2)#[1, 2, ['a', 'b', {100}], ('c', 'd'), 3]
# print(list3)#[1, 2, ['a', 'b', {100}], ('c', 'd')]
# print(list4)#[1, 2, ['a', 'b'], ('c', 'd')]
list1[3]=list1[3]+tuple1
# print(list1)#[1, 2, ['a', 'b', {100}], ('c', 'd', 10, 10), 3]
# print(list2)#[1, 2, ['a', 'b', {100}], ('c', 'd', 10, 10), 3]
# print(list3)#[1, 2, ['a', 'b', {100}], ('c', 'd')]
# print(list4)#[1, 2, ['a', 'b'], ('c', 'd')]
dict1={}
dict1['1']=1111
list1[2].append(dict1)
print(list1)
print(list2)
print(list3)
print(list4)