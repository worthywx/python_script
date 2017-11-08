#-*- coding: utf-8 -*-

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


alist = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))


def list_reverse(head):
    """单链表逆置"""
    prev = head
    cur = head.next
    prev.next = None

    while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp
    return prev


root = list_reverse(alist)
while root:
    print root.data
    root = root.next
