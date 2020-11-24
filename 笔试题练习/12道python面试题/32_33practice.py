# 方法一
def num_list(ls):
    """
    该函数的输入是一个仅包含数字的list,输出一个新的list，其中每一个元素要满足以下条件：
    1、该元素是偶数
    2、该元素在原list中是在偶数的位置(index是偶数)
    """
    return [x for x in ls if x%2==0 and ls.index(x)%2==0]

# 方法二
def num_list_1(ls):
    return [x for x in ls[::2] if x%2==0]

if __name__ == '__main__':
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 9]
    a = num_list(num)
    b = num_list_1(num)
    print(a)
    print(b)