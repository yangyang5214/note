# -*- coding: utf-8 -*-
from typing import List


def restoreString(s: str, indices: List[int]) -> str:
    index = 0
    r = [0] * len(s)
    for i in indices:
        r[i] = s[index]
        index = index + 1
    return ''.join(r)


if __name__ == '__main__':
    s = 'codeleet'
    indices = [4, 5, 6, 7, 0, 2, 1, 3]
    # s = "aiohn"
    # indices = [3, 1, 4, 2, 0]

    # s = "aaiougrt"
    # indices = [4, 0, 2, 6, 7, 3, 1, 5]
    print(restoreString(s, indices))
