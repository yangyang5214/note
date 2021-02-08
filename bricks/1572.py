# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/matrix-diagonal-sum/comments/

def diagonalSum(mat):
    w = len(mat)
    s = 0
    for i in range(w):
        s = s + mat[i][i] + mat[i][w - 1 - i]
    if w % 2 != 0:
        s = s - mat[w // 2][w // 2]
    return s


if __name__ == '__main__':
    # mat = [[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]]
    mat = [[1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1]]
    print(diagonalSum(mat))
