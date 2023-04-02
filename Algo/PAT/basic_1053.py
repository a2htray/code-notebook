#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/2

"""
PAT 乙级 1053
"""


def count(e, es):
    c = 0
    for v in es:
        if v < e:
            c += 1
    return c


if __name__ == '__main__':
    tokens = input().split(' ')
    n = int(tokens[0])
    e = float(tokens[1])
    d = int(tokens[2])

    a = 0
    b = 0

    for i in range(n):
        tokens = input().split(' ')
        k = int(tokens[0])
        es = list(map(float, tokens[1:]))
        c = count(e, es)

        if c > k // 2:
            a += 1
            if k > d:
                a -= 1
                b += 1

    print('%.1f%% %.1f%%' % (1.0 * a / n * 100, 1.0 * b / n * 100))
