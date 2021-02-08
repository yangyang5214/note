# -*- coding: utf-8 -*-

def sortString(s):
    bucket = [0] * 26
    for _ in s:
        bucket[ord(_) - 97] += 1
    r = []
    l = len(s)
    print(bucket)
    while len(r) != l:
        for i in range(26):
            if bucket[i] != 0:
                r.append(chr(i + 97))
                bucket[i] -= 1
        for i in range(25, -1, -1):
            if bucket[i] != 0:
                r.append(chr(i + 97))
                bucket[i] -= 1
    return ''.join(r)


if __name__ == '__main__':
    s = "leetcode"
    print(sortString(s))
