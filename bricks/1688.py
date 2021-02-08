# -*- coding: utf-8 -*-


def numberOfMatches(n):
    r = 0
    while n != 1:
        r = r + n // 2
        if n % 2 == 0:
            n = n // 2
        else:
            n = n // 2 + 1
    return r


if __name__ == '__main__':
    n = 14
    print(numberOfMatches(n))
