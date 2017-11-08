# coding=utf-8
# Author: Worthy
# Create Time: 2017/11/8 11:17

def midFind(l, val):
    """
    :param l:查找集合
    :param val: 查找值
    :return: False or 位置
    """
    low = 0
    high = len(l) - 1

    while high >= low:
        mid = (low + high) / 2
        if val > l[mid]:
            low = mid + 1
        elif val < l[mid]:
            high = mid - 1
        else:
            return mid
    return False


lst = [2, 4, 8, 9, 10, 333]
print midFind(lst, 2)
