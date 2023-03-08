#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/3/8

"""
PAT 乙级 1022
"""


if __name__ == '__main__':
    num1, num2, base = map(int, input().split(' '))

    total = num1 + num2
    if total == 0:
        print(0)
        exit(1)

    res = []
    while total >= 1:
        res = [total % base] + res
        total = total // base

    if res[0] == 0:
        res = res[1:]

    print(''.join(map(str, res)))



