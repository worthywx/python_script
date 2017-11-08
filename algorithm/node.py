# coding=utf-8
# Author: Worthy
# Create Time: 2017/11/8 10:57

class Node(object):
    def __init__(self, val, next=None):
        self.value = val
        self.next = next


def node(l1, l2):
    if l1 == None or l2 == Node:
        return None

    p1, p2 = l1, l2
    n1, n2 = 0, 0
    while p1.next:
        p1 = p1.next
        n1 += 1
    while p2.next:
        p2 = p2.next
        n2 += 1

    if n1 > n2:
        for _ in range(n1 - n2):
            l1 = l1.next
    else:
        for _ in range(n2 - n1):
            l2 = l2.next

    while l1 and l2:
        if l1.value == l2.value:
            return l1
        else:
            l1 = l1.next
            l2 = l2.next
    return None


lst1 = Node(1, Node(2, Node(3, Node(8, Node(9, Node(10))))))
lst2 = Node(8, Node(9, Node(10)))

print node(lst1, lst2).value
