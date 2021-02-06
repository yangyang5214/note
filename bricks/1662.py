# -*- coding: utf-8 -*-
from typing import List


def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    l = []
    for w in word1:
        for _ in w:
            l.append(_)

    index = 0
    length = len(l)
    for w in word2:
        for _ in w:
            if index == length or _ != l[index]:
                return False
            index = index + 1
    if index < length:
        return False
    return True


if __name__ == '__main__':
    word1 = ["a", "b"]
    word2 = ["ab", "c"]
    #
    # word1 = ["abc", "d", "defg"]
    # word2 = ["abcddef"]

    print(arrayStringsAreEqual(word1, word2))
