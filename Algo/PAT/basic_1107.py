#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/15

"""
PAT 乙级 1107
"""

if __name__ == '__main__':
    n, m = map(int, input().split())

    vs = [0] * n
    for i in range(n):
        v = max(map(int, input().split()))
        vs[i] = v

    print(' '.join(map(str, vs)))
    print(max(vs))

