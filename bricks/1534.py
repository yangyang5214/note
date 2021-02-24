# -*- coding: utf-8 -*-
from typing import List


def countGoodTriplets(arr: List[int], a: int, b: int, c: int) -> int:
    count = 0
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                    count += 1
    return count


if __name__ == '__main__':
    arr = [7, 3, 7, 3, 12, 1, 12, 2, 3]
    a = 5
    b = 8
    c = 1
    print(countGoodTriplets(arr, a, b, c))
