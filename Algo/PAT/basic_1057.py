#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/3

"""
PAT 乙级 1057
"""


def count_0(s):
    count = 0
    for c in s:
        if c == '0':
            count += 1
    return count


if __name__ == '__main__':
    a_ord = ord('a')
    z_ord = ord('z')
    A_ord = ord('A')
    Z_ord = ord('Z')

    line = input()

    total = 0
    for c in line:
        c_ord = ord(c)
        if a_ord <= c_ord <= z_ord:
            total += c_ord - a_ord + 1
        if A_ord <= c_ord <= Z_ord:
            total += c_ord - A_ord + 1

    if total == 0:
        print(0, 0)
    else:
        s = bin(total)[2:]
        print(count_0(s), len(s) - count_0(s))
