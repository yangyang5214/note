# -*- coding: utf-8 -*-
from bricks.base.treenode import TreeNode


class Solution(object):
    def sortedArrayToBST(self, nums):
        if nums:
            node = TreeNode(nums[len(nums) // 2])
            node.left = self.sortedArrayToBST(nums[:len(nums) // 2])
            node.right = self.sortedArrayToBST(nums[len(nums) // 2 + 1:])
            return node


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    s = Solution()
    node = s.sortedArrayToBST(nums)
    print(node)
