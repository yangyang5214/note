# -*- coding: utf-8 -*-
from treenode import TreeNode


def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


def maxDepth1(root: TreeNode) -> int:
    if not root:
        return 0
    r = 0
    q = [root]
    while q:
        for i in range(len(q)):
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        r = r + 1
    return r


def create(nums: list) -> TreeNode:
    if not nums:
        return
    node = TreeNode(nums[len(nums) // 2])
    node.left = create(nums[:len(nums) // 2])
    node.right = create(nums[len(nums) // 2 + 1:])
    return node


if __name__ == '__main__':
    nums = [1, 2, 4, 5, 6, 8]
    node = create(nums)
    print(maxDepth1(create(nums)))
    print(maxDepth(create(nums)))
