#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/6

"""
PAT 乙级 1102
"""

if __name__ == '__main__':
    n = int(input())

    a = ''
    a_num = 0  # 销售量
    b = ''
    b_num = 0  # 销售额

    for _ in range(n):
        tokens = input().split(' ')
        if a == '' or b == '':
            a = tokens[0]
            a_num = int(tokens[2])
            b = tokens[0]
            b_num = int(tokens[1]) * int(tokens[2])
            continue

        if int(tokens[2]) > a_num:
            a = tokens[0]
            a_num = int(tokens[2])

        if int(tokens[1]) * int(tokens[2]) > b_num:
            b = tokens[0]
            b_num = int(tokens[1]) * int(tokens[2])

    print(a, a_num)
    print(b, b_num)
