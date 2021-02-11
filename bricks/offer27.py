# -*- coding: utf-8 -*-
from treenode import TreeNode


# https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/

def mirrorTree(root: TreeNode) -> TreeNode:
    if not root:
        return
    temp = root.left
    root.left = mirrorTree(root.right)
    root.right = mirrorTree(temp)
    return root


def build_tree():
    root = TreeNode(4)
    left = TreeNode(2, TreeNode(1), TreeNode(3))
    right = TreeNode(7, TreeNode(6), TreeNode(9))
    root.left = left
    root.right = right
    return root


def ldr(node: TreeNode, r: list):
    if not node:
        return
    ldr(node.left, r)
    r.append(node.val)
    ldr(node.right, r)


def dlr(node: TreeNode) -> list:
    if not node:
        return
    r.append(node.val)
    ldr(node.left, r)
    ldr(node.right, r)


def lrd(node: TreeNode) -> list:
    if not node:
        return
    ldr(node.left, r)
    ldr(node.right, r)
    r.append(node.val)


def create(nums: list) -> TreeNode:
    if not nums:
        return
    node = TreeNode(nums[len(nums) // 2])
    node.left = create(nums[:len(nums) // 2])
    node.right = create(nums[len(nums) // 2 + 1:])
    return node


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6]
    root = create(nums)
    r = []
    ldr(root, r)
    print(r)

    r = []
    ldr(mirrorTree(root), r)
    print(r)
