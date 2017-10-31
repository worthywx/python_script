# coding=utf-8
# Author: Worthy
# Create Time: 2017/10/30 10:16
import random
import cProfile
import time
import functools
import sys

sys.setrecursionlimit(1000000)

SORTSIZE = 1000


def runTimeWrapper(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        if len(args[0]) == SORTSIZE:
            print "%s run time is %f" % (func.__doc__, end - start)
        return res

    return wrapper


def getRandomDate(num):
    return [random.randint(0, 1000) for i in range(num)]


@runTimeWrapper
def bubbleSort(l):
    '''冒泡排序'''
    n = len(l)
    if len(l) <= 0:
        return None

    for i in range(n):
        for j in range(0, n - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


@runTimeWrapper
def quickSort(l):
    '''快速排序'''
    if len(l) <= 0:
        return []
    mdata = l[0]
    left = quickSort([i for i in l[1:] if i < mdata])
    right = quickSort([i for i in l[1:] if i >= mdata])
    return left + [mdata] + right


@runTimeWrapper
def insertSort(l):
    '''插入排序'''
    length = len(l)
    for i in range(1, length):
        j = i
        temp = l[i]
        while j > 0 and l[j - 1] > temp:
            l[j] = l[j - 1]
            j -= 1
        l[j] = temp
    return l


@runTimeWrapper
def shellSort(l):
    '''希尔排序'''
    dist = len(l) // 2
    while dist > 0:
        for i in range(dist, len(l)):
            temp = l[i]
            j = i
            while j > 0 and l[j - dist] > temp:
                l[j] = l[j - dist]
                j -= dist
            l[j] = temp
        dist = dist // 2
    return l


def merge(a, b):
    c = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i == len(a):
        c.extend(b[j:])
    if j == len(b):
        c.extend(a[i:])
    return c


@runTimeWrapper
def mergeSort(l):
    """归并排序"""
    if len(l) <= 1:
        return l
    mid = len(l) / 2
    left = mergeSort(l[:mid])
    right = mergeSort(l[mid:])
    return merge(left, right)


lvalue = getRandomDate(SORTSIZE)

shellSort(lvalue)
mergeSort(lvalue)
insertSort(lvalue)
bubbleSort(lvalue)
quickSort(lvalue)
