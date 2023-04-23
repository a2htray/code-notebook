#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/15

"""
PAT 乙级 1087
"""

if __name__ == '__main__':
    n = int(input())

    values = [0] * n
    for i in range(1, n + 1):
        value = int(1.0 * i / 2) + int(1.0 * i / 3) + int(1.0 * i / 5)
        values[i - 1] = value

    stat = {}
    cnt = 0
    for value in values:
        if value not in stat:
            cnt += 1
            stat[value] = True

    print(cnt)
