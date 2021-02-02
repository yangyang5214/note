# -*- coding: utf-8 -*-


def numJewelsInStones(jewels: str, stones: str) -> int:
    return sum([stones.count(j) for j in jewels])


if __name__ == '__main__':
    jewels = "aA"
    stones = "aAAbbbb"
    print(numJewelsInStones(jewels, stones))
