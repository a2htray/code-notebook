#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/15

"""
PAT 乙级 1097
"""

if __name__ == '__main__':
    n, k, x = map(int, input().split())

    data = []
    cur_k = 1
    for i in range(1, n + 1):
        values = list(map(int, input().split()))
        if i % 2 != 0:
            values = [x] * cur_k + values[:-cur_k]
            cur_k += 1
            if cur_k > k:
                cur_k = 1

        data.append(values)

    col_sums = [0] * n

    for i in range(n):
        for j in range(n):
            col_sums[j] += data[i][j]

    print(' '.join(map(str, col_sums)))
