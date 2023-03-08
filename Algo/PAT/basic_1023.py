#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/3/8

"""
PAT 乙级 1023
"""

if __name__ == '__main__':
    digits = []
    for i, digit in enumerate(map(int, input().split(' '))):
        digits += [i] * digit

    digits.sort()

    if digits[0] != 0:
        print(''.join(map(str, digits)))
        exit(0)

    for i, v in enumerate(digits):
        if v != 0:
            digits[0], digits[i] = digits[i], digits[0]
            break
    print(''.join(map(str, digits)))
