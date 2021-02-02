# -*- coding: utf-8 -*-
from typing import List


def numIdenticalPairs(nums: List[int]) -> int:
    m = {}
    for n in nums:
        if n in m:
            m[n] = m[n] + 1
        else:
            m[n] = 1

    sum = 0
    for v in m.values():
        sum = sum + v * (v - 1) / 2
    return int(sum)


if __name__ == '__main__':
    nums = [1, 2, 3, 1, 1, 3]
    nums = [1, 1, 1, 1]
    print(numIdenticalPairs(nums))
