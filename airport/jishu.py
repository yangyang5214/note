# -*- coding: utf-8 -*-


if __name__ == '__main__':
    nums = [133, 22, 43, 6, 9, 10, 100]
    arr = [0] * 200
    m = 0
    for _ in nums:
        arr[_] += 1
        if m < arr[_]:
            m = _

    r = []
    for i in range(m):
        if arr[i] != 0:
            for j in range(arr[i]):
                r.append(i)
    print(r)