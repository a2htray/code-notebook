#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/3/13

"""
PAT 乙级 1030
"""

if __name__ == '__main__':
    n, p = map(int, input().split(' '))
    if n == 0:
        exit(0)

    digits = [int(v) for v in input().split(' ')]
    digits.sort()

    # print(digits)

    cnt = 0
    for i, v1 in enumerate(digits):
        for j, v2 in enumerate(digits):
            if v2 <= p * v1:
                if j - i + 1 > cnt:
                    cnt = j - i + 1
    print(cnt)

