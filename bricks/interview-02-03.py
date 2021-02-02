# -*- coding: utf-8 -*-
from util import ListNode


def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next


def buildNode():
    l = ['a', 'b', 'c', 'd', 'e', 'f']
    n = ListNode(l[len(l) - 1])
    for i in reversed(range(len(l) - 1)):
        node = ListNode(l[i])
        node.next = n
        n = node
    return n


if __name__ == '__main__':
    deleteNode(buildNode())
