#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/10

"""
PAT 乙级 1071
"""

if __name__ == '__main__':
    total, k = map(int, input().split())

    for _ in range(k):
        n1, b, t, n2 = list(map(int, input().split()))
        if t > total:
            print(f'Not enough tokens.  Total = {total}.')
            continue

        if (b == 0 and n2 < n1) or (b == 1 and n2 >= n1):
            total = total + t
            print(f'Win {t}!  Total = {total}.')
        else:
            total = total - t
            print(f'Lose {t}.  Total = {total}.')
            if total == 0:
                print(f'Game Over.')
                break
