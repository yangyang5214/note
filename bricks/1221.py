# -*- coding: utf-8 -*-

def balancedStringSplit(s):
    f = 0
    r = 0
    for _ in s:
        if _ == 'R':
            f += 1
        elif _ == 'L':
            f -= 1
        if f == 0:
            r += 1
    return r


if __name__ == '__main__':
    s = 'LLLLRRRR'
    print(balancedStringSplit(s))
