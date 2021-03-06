# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies/submissions/
from typing import List


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    m = max(candies)
    return [i + extraCandies >= m for i in candies]


if __name__ == '__main__':
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    print(kidsWithCandies(candies, extraCandies))
