#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/6

"""
PAT 乙级 1103
"""
import math

if __name__ == '__main__':
    m, n = map(int, input().split(' '))

    got = False
    for i in range(m, n + 1):
        a = i ** 3 - (i - 1) ** 3
        b = math.sqrt(a)

        if int(b) == b:  # 可以用于判断一个数是否是另一个数的平方
            for j in range(2, int(b)):
                if j ** 2 + (j - 1) ** 2 == b:
                    print(i, j)
                    got = True

    if not got:
        print('No Solution')
