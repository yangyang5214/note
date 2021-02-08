# -*- coding: utf-8 -*-


def sumOddLengthSubarrays(arr):
    l = len(arr)
    r = 0
    for i in range(l):
        for j in range(i, l):
            if (j - i) % 2 == 0:
                r += sum(arr[i:j + 1])
    return r


if __name__ == '__main__':
    arr = [1, 4, 2, 5, 3]
    print(sumOddLengthSubarrays(arr))
