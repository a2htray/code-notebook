#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/10

"""
PAT 乙级 1069
"""

if __name__ == '__main__':
    m, n, s = map(int, input().split())
    names = [''] * m
    for i in range(m):
        names[i] = input()

    if s > m:
        print('Keep going...')
        exit(0)

    names_match = {}

    while s <= m:
        if names[s - 1] not in names_match:
            print(names[s - 1])
            names_match[names[s - 1]] = True
            s += n
        else:
            s += 1
