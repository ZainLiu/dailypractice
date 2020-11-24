import re
a = re.match('\w:/\w*/','D:/课件/就业班课件/1_DRF_v1.1')
if a:
    print(a.group())
else:
    print(a)