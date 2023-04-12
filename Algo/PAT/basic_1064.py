#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/12

"""
PAT 乙级 1064
"""

if __name__ == '__main__':
    n = int(input())
    nums = input().split()

    fnums = [0] * n
    for i, num in enumerate(nums):
        fnum = 0
        for c in num:
            fnum += int(c)
        fnums[i] = fnum

    fnums.sort()
    stat = {}
    ret = []
    for fnum in fnums:
        if fnum not in stat:
            stat[fnum] = True
            ret.append(fnum)

    print(len(ret))
    print(' '.join(map(str, ret)))
