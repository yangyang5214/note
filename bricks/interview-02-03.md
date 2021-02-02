## 面试题 02.03. 删除中间节点

https://leetcode-cn.com/problems/delete-middle-node-lcci/


好家伙，第一遍没仔细看题目，以为入参是两个，(node, val), 删除 node 中的 val 节点。

这题的意义在于，让人理解 链表的概念？ 

### code

```
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

```