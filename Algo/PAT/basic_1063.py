#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/11

"""
PAT 乙级 1062
"""
import math

if __name__ == '__main__':
    n = int(input())
    ans = -1

    for _ in range(n):
        v = math.sqrt(sum(map(lambda s: int(s)**2, input().split())))
        if v > ans:
            ans = v

    print('%.2f' % ans)
