# coding=utf-8
# Author: Worthy
# Create Time: 2017/11/8 14:17

# 二叉树节点
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right


def lookup(root):
    """广度遍历二叉树"""
    stack = [root]
    while stack:
        current = stack.pop(0)
        print current.value
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)


def deep(root):
    """深度打印二叉树"""
    if root is None:
        return
    print root.value
    deep(root.left)
    deep(root.right)


def max_deep(root):
    """二叉树最大深度"""
    if root is None:
        return 0
    return max(max_deep(root.left), max_deep(root.right)) + 1


def equal_tree(root1, root2):
    """判断二叉树是否相等"""
    if root1 is None and root2 is None:
        return True
    elif root1 and root2:
        if root1.value == root2.value and equal_tree(root1.left, root2.left) and equal_tree(root1.right, root2.right):
            return True
    else:
        return False


def rebuild(pre, center):
    """
    前序中序还原树
    :param pre: 前序
    :param center: 中序
    :return:
    """
    if not pre:
        return
    cur = Node(pre[0])
    index = center.index(pre[0])
    cur.left = rebuild(pre[1:index + 1], center[:index])
    cur.right = rebuild(pre[index + 1:], center[index + 1:])
    return cur


def back_print(root):
    """打印二叉树后序序列"""
    if root is None:
        return
    back_print(root.left)
    back_print(root.right)
    print root.value


if __name__ == '__main__':
    tree = Node(1, Node(2, Node(4, Node(8)), Node(5, Node(9), Node(10))), Node(3, Node(6, Node(11)), Node(7)))
    tree1 = tree
    print equal_tree(tree, tree1)
    print "树深:{}".format(max_deep(tree))
    print "----深度遍历---"
    lookup(tree)
    print "----END----"
    print "----深度遍历---"
    deep(tree)
    print "----END----"
