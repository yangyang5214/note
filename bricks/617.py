# -*- coding: utf-8 -*-
from treenode import TreeNode


def mergeTrees(root1: TreeNode, root2: TreeNode) -> TreeNode:
    if not root1:
        return root2
    if not root2:
        return root1
    root1.val = root1.val + root2.val
    root1.left = mergeTrees(root1.left, root2.left)
    root1.right = mergeTrees(root1.right, root2.right)
    return root1


if __name__ == '__main__':
    pass
