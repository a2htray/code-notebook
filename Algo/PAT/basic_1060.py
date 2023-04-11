#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/11

"""
PAT 乙级 1060
"""

if __name__ == '__main__':
    n = int(input())
    es = list(map(int, input().split()))
    es.sort()

    range_map = {}
    for i, e in enumerate(es):
        if e not in range_map:
            range_map[e] = []

        range_map[e].append(i)

    ans_e = 0

    for i in range(1, n + 1, 1):
        if es[-i] > i:
            ans_e = i

    print(ans_e)
