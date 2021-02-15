# -*- coding: utf-8 -*-

def hammingDistance(x: int, y: int) -> int:
    z = x ^ y
    c = 0
    while z > 0:
        z = z & (z - 1)
        print('z: {}, z-1:{}'.format(z, z - 1))
        c = c + 1
    return c


if __name__ == '__main__':
    x = 1
    y = 4
    print(hammingDistance(x, y))
