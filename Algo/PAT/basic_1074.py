#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/10

"""
PAT 乙级 1074
"""

if __name__ == '__main__':
    line = input()
    bases = [0] * len(line)
    for i, c in enumerate(line):
        if c == '0':
            bases[i] = 10
        else:
            bases[i] = int(c)

    num_str1 = str(int(input()))
    num_str2 = str(int(input()))

    n_str1 = len(num_str1)
    n_str2 = len(num_str2)

    while len(num_str1) < n_str2:
        num_str1 = '0' + num_str1

    while len(num_str2) < n_str1:
        num_str2 = '0' + num_str2

    num_str1 = '0' + num_str1
    num_str2 = '0' + num_str2

    ans = []
    carry = 0

    for i in range(-1, -len(num_str1), -1):
        tmp = int(num_str1[i]) + int(num_str2[i]) + carry
        if i < -20:
            base = 10
        else:
            base = bases[i]

        carry = tmp // base
        ans = [tmp % base] + ans

    ans = [carry] + ans

    print(int(''.join(map(str, ans))))
