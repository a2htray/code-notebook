#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/12

"""
PAT 乙级 1065
"""

if __name__ == '__main__':
    n = int(input())
    pairs = {}
    for _ in range(n):
        p1, p2 = input().split()
        pairs[p1] = p2
        pairs[p2] = p1

    m = int(input())
    ps = input().split()

    ps_map = []

    lost_ps = []
    for p in ps:
        if p not in pairs:
            lost_ps.append(p)

    lost_ps.sort()
    print(lost_ps)
