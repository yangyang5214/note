# -*- coding: utf-8 -*-
from typing import List


def totalFruit(tree: List[int]) -> int:
    length = len(tree)
    r = 0
    for i in range(length):
        for j in range(i, length):
            sub_tree = tree[i:j + 1]
            arr = set(sub_tree)
            if len(arr) <= 2:
                if len(sub_tree) > r:
                    r = len(sub_tree)
    return r


def totalFruit1(tree: List[int]) -> int:
    index = 0
    m = {}
    r = 0
    for i in range(len(tree)):
        if tree[i] not in m:
            m[tree[i]] = 1
        else:
            m[tree[i]] += 1
        while len(m) > 2:
            m[tree[index]] -= 1
            if m[tree[index]] == 0:
                m.pop(tree[index])
            index = index + 1
        r = max(i - index + 1, r)
    return r


if __name__ == '__main__':
    nums = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
    # nums = [1, 2, 3, 2, 2]
    # print(totalFruit(nums))
    print(totalFruit1(nums))
