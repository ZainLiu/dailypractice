list1 = [1,2,3,1,3,6,9]
list2 = [3,4,5,3,5,6,7,8,9]

# 相同
same = set()
for i in list1:
    if i in list2:
        same.add(i)
# 不同
diff1 = set()
for i in list1:
    if i not in same:
        diff1.add(i)
diff2 = set()
for i in list2:
    if i not in same:
        diff2.add(i)
list1_set = set(list1)
list2_set = set(list2)
same1 = list1_set & list2_set
diff1_1 = list1_set ^ list2_set
diff2_2 = list2_set ^ list1_set
diff11 = list1_set ^same1
diff22 = list2_set ^ same1
print(same,same1,'\n',diff1,diff11,'\n',diff2,diff22)
