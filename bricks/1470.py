# -*- coding: utf-8 -*-
from typing import List


def shuffle(nums: List[int], n: int) -> List[int]:
    result = []
    for i in range(n):
        result.append(nums[i])
        result.append(nums[i + n])
    return result


def shuffle1(nums: List[int], n: int) -> List[int]:
    result = [0] * n * 2
    for i in range(n):
        result[2 * i] = nums[i]
        result[2 * i + 1] = nums[i + n]
    return result


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 4, 3, 2, 1]
    n = 4
    print(shuffle1(nums, n))
