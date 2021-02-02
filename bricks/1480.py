# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/running-sum-of-1d-array/
from typing import List


def runningSum(nums: List[int]) -> List[int]:
    flag = nums[0]
    for i in range(1, len(nums)):
        nums[i] = nums[i] + flag
        flag = nums[i]
    return nums


if __name__ == '__main__':
    # nums = [1, 2, 3, 4]
    # nums = [1, 1, 1, 1, 1]
    nums = [3, 1, 2, 10, 1]
    print(runningSum(nums))
