str1 = "k:1|k1:2|k2:3|k3:4"
def strtodict(str1):
    dict = {}
    for items in str1.split('|'):
        key, value = items.split(':')
        dict[key] = value
    return dict

dict1 = strtodict(str1)

print(dict1,type(dict1))