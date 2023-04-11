#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/11

"""
PAT 乙级 1098
"""

if __name__ == '__main__':
    n = int(input())
    tops = list(map(int, input().split()))
    bottoms = list(map(int, input().split()))

    min_top = min(tops)
    max_bottom = max(bottoms)
    if min_top > max_bottom:
        print('Yes', min_top - max_bottom)
    else:
        print('No', max_bottom - min_top + 1)

