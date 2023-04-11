#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/11

"""
PAT 乙级 1062
"""
import math

if __name__ == '__main__':
    tokens = input().split()
    n1, m1 = map(int, tokens[0].split('/'))
    n2, m2 = map(int, tokens[1].split('/'))
    k = int(tokens[2])

    if 1.0 * n2 / m2 < 1.0 * n1 / m2:
        n1, m1, n2, m2 = n2, m2, n1, m1
    ts = []
    for i in range(1, k):
        if k * n1 < i * m1 and i * m2 < k * n2 and math.gcd(i, k) == 1:
            ts.append(i)

    print(' '.join(map(lambda t: f'{t}/{k}', ts)))
