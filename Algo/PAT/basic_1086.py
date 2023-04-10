#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/10

"""
PAT 乙级 1086
"""

if __name__ == '__main__':
    a, b = map(int, input().split())
    num = a * b

    s = str(num)
    first = True
    for i in range(len(s) - 1, -1, -1):
        if first and s[i] == '0':
            continue
        else:
            first = False
            print(s[i], end='')
    print()
