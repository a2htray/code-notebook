#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/18

"""
PAT 乙级 1082
"""

from functools import cmp_to_key


def cmp(a, b):
    if a[1] > b[1]:
        return 1
    else:
        return -1


if __name__ == '__main__':
    n = int(input())

    players = []
    for _ in range(n):
        idstr, x, y = input().split()

        players.append([idstr, int(x) ** 2 + int(y) ** 2])

    players.sort(key=cmp_to_key(cmp))

    print(players[0][0], players[-1][0])
