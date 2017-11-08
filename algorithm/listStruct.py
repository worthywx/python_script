# coding=utf-8
# Author: Worthy
# Create Time: 2017/11/7 14:03

class Node(object):
    def __init__(self, val, next=None):
        self.value = val
        self.next = next


def createList(n):
    if n < 1:
        return None
    head = Node(1)
    if n == 1:
        return head
    tmp = head
    for i in range(2, n + 1):
        tmp.next = Node(i)
        tmp = tmp.next
    return head


def printList(head):
    if head == None:
        return
    tmp = head
    while tmp:
        print tmp.value
        tmp = tmp.next


def insertList(head, n, val):
    if n > listLeng(head) or n < 0:
        return False

    if n == 0:
        tmp = Node(val)
        tmp.next = head
        return tmp

    p = head
    while n > 1:
        p = p.next
        n -= 1
    tmp = Node(val)
    tmp.next = p.next
    p.next = tmp
    return head


def listLeng(head):
    p = head
    n = 0
    while p:
        n += 1
        p = p.next
    return n


def deleteList(head, n):
    if n <= 0 or n > listLeng(head):
        return False
    if n == 1:
        return head.next
    p = head
    while n > 2:
        p = p.next
        n -= 1
    p.next = p.next.next
    return p


def swapPairs(head):
    if head != None and head.next != None:
        next = head.next
        head.next = swapPairs(next.next)
        next.next = head
        return next
    return head


def merge_list(l1, l2):
    tmp = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] > l2[0]:
            tmp.append(l2[0])
            del l2[0]
        else:
            tmp.append(l1[0])
            del l1[0]
    tmp.extend(l1)
    tmp.extend(l2)
    return tmp


a = [1, 2, 5, 8, 10]
b = [3, 7, 9, 11, 12]
print merge_list(a, b)
