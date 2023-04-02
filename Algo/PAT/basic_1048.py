#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/1

"""
PAT 乙级 1048
"""

if __name__ == '__main__':
    str1, str2 = input().split(' ')
    n_str1 = len(str1)
    n_str2 = len(str2)
    max_n = max(n_str1, n_str2)

    if max_n > n_str1:
        str1 = ''.join(['0'] * (max_n - n_str1)) + str1
    if max_n > n_str2:
        str2 = ''.join(['0'] * (max_n - n_str2)) + str2

    cs = [''] * max_n
    for i in range(-1, -max_n - 1, -1):
        if i % 2 == 1:
            c = (int(str1[i]) + int(str2[i])) % 13
            if c == 10:
                c = 'J'
            elif c == 11:
                c = 'Q'
            elif c == 12:
                c = 'K'
            else:
                c = str(c)
        else:
            c = int(str2[i]) - int(str1[i])
            if c < 0:
                c = c + 10
            c = str(c)
        cs[i] = c

    print(''.join(cs))
