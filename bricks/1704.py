# -*- coding: utf-8 -*-

def halvesAreAlike(s):
    m = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    s1 = s[: len(s) // 2]
    s2 = s[len(s) // 2:]
    c = 0
    for _ in s1:
        if _ in m:
            c += 1
    for _ in s2:
        if _ in m:
            c -= 1
    return c == 0


if __name__ == '__main__':
    s = 'AbCdEfGh'
    print(halvesAreAlike(s))
