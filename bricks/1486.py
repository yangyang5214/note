# -*- coding: utf-8 -*-


def xorOperation(n: int, start: int) -> int:
    ans = 0
    for i in range(n):
        ans = ans ^ (start + i * 2)
    return ans


if __name__ == '__main__':
    n = 5
    start = 0
    print(xorOperation(n, start))
