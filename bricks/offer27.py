# -*- coding: utf-8 -*-
from treenode import TreeNode


# https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/

def mirrorTree(root: TreeNode) -> TreeNode:
    if root:
        root.val = root.val
        root.left = mirrorTree(root.right)
        root.right = mirrorTree(root.left)
    return root


if __name__ == '__main__':
    root = None
    print(mirrorTree(root))
