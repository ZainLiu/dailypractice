def bubble_sort(alist):
    """冒泡排序"""
    for j in range(len(alist)-1, 0,-1):
        for i in range(j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]


def selection_sort(alist):
    """选择排序"""
    for i in range(len(alist)-1):
        min_index = i
        for j in range(i+1,len(alist)):
            if alist[j] < alist[min_index]:
                min_index = j

        if min_index != i:
            alist[i], alist[min_index] = alist[min_index], alist[i]


def insert_sort(alist):
    """插入排序"""
    for i in range(1, len(alist)):
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
                break


def quick_sort(alist, start, end):
    """快速排序"""
    if start >= end:
        mid = alist[start]
        low = start
        high = end
        while low < high:
            while low < high and alist[high] >=mid:
                high -= 1
            alist[low] = alist[high]
            while low < high and alist[low] < mid:
                low += 1
            alist[high] = alist[low]
        alist[low] = mid

        quick_sort(alist, start,low-1)
        quick_sort(alist,low+1,end)


def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            j = i
            # 插入排序，重第二行开始逐个遍历往纵列方向进行插入排序
            while j >= gap and alist[j-gap] > alist[j]:
                alist[j-gap],alist[j] = alist[j], alist[j-gap]
                j -= gap
        gap = gap // 2

def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    num = len(alist) // 2
    left = merge_sort(alist[alist[:num]])
    right = merge_sort(alist[num:])
    return merge_sort()

def merge(left,right):
    l, r = 0, 0
    result = []
    


