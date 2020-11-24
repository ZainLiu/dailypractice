import os
# 方法一
def get_files(dir,suffix):
    res = []
    for root,dirs,files in os.walk(dir):
        for filename in files:
            name,suf = os.path.splitext(filename)
            if suf == suffix:
                res.append(os.path.join(root,filename))
    print(res)

# 方法二
def pick(obj):
    if obj.endswith(".py"):
        print(obj)
def scan_path(dir):
    file_list = os.listdir(dir)
    for obj in file_list:
        if os.path.isfile(obj):
            pick(obj)
        elif os.path.isdir(obj):
            scan_path(obj)
# 方法三
from glob import iglob
def func(fb, postfix):
    for i in iglob(f'{fb}/**/*{postfix}',recursive=True):
        print(i)
if __name__ == '__main__':
    # 方法一
    # get_files('./','.py')
    # 方法二
    # scan_path('./')
    # 方法三
    func('../','.py')
