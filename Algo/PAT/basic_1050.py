#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/22

"""
PAT 乙级 1049
"""
import math


def get_m_n(N: int):
    diff = math.inf
    m, n = 0, 0
    for i in range(1, N + 1):
        if N % i == 0:
            tmp_n = N // i
            if 0 <= i - tmp_n < diff:
                diff = i - tmp_n
                m = i
                n = tmp_n
    return m, n


if __name__ == '__main__':
    N = int(input())
    m, n = get_m_n(N)

    vs = list(map(int, input().split()))

    vs.sort(reverse=True)

    arr = []
    filled = []
    for _ in range(m):
        arr.append([0] * n)
        filled.append([False] * n)

    i, j = 0, 0
    direct = 'right'
    for v in vs:
        arr[i][j] = v
        filled[i][j] = True
        if direct == 'right':
            if j + 1 == n or filled[i][j + 1]:
                i += 1
                direct = 'down'
                continue
            else:
                j += 1

        if direct == 'down':
            if i + 1 == m or filled[i + 1][j]:
                j -= 1
                direct = 'left'
                continue
            else:
                i += 1

        if direct == 'left':
            if j - 1 < 0 or filled[i][j - 1]:
                i -= 1
                direct = 'up'
                continue
            else:
                j -= 1

        if direct == 'up':
            if i - 1 < 0 or filled[i - 1][j]:
                j += 1
                direct = 'right'
                continue
            else:
                i -= 1

    for i in range(m):
        print(' '.join(map(str, arr[i])))
