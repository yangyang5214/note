# -*- coding: utf-8 -*-
from typing import List


def sumOfUnique(nums: List[int]) -> int:
    arr = [0] * 101
    for _ in nums:
        arr[_] += 1
    sum = 0
    for i in range(101):
        if arr[i] == 1:
            sum = sum + i
    return sum


if __name__ == '__main__':
    nums = [14, 83, 63, 42, 15, 87, 61, 37, 30, 95, 99, 100, 45, 30, 5, 2, 29, 65, 15, 71, 12, 17, 61, 81]
    print(sumOfUnique(nums))
