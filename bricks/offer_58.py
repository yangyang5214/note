# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/

def reverseLeftWords(s: str, n: int) -> str:
    return s[n:] + s[0:n]


if __name__ == '__main__':
    s = "lrloseumgh"
    n = 1000
    print(reverseLeftWords(s, n))
