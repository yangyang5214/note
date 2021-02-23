# -*- coding: utf-8 -*-
from typing import List


def countGoodRectangles(rectangles: List[List[int]]) -> int:
    m = {}
    max_flag = 0
    for _ in rectangles:
        side = min(_[0], _[1])
        max_flag = max(max_flag, side)
        if side in m:
            m[side] = m[side] + 1
        else:
            m[side] = 1
    return m[max_flag]


if __name__ == '__main__':
    rectangles = [[5, 8], [3, 9], [5, 12], [16, 5]]
    rectangles = [[2,3],[3,7],[4,3],[3,7]]
    print(countGoodRectangles(rectangles))
