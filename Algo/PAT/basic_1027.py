#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/3/10

"""
PAT 乙级 1027
"""


def get_n(h):
    if h == 1:
        return 1

    return sum([1] + [2*i for i in range(3, h+1, 2)])


if __name__ == '__main__':
    tokens = input().split(' ')
    n = int(tokens[0])
    symbol = tokens[1]

    h = 1
    for h in range(3, 200, 2):
        if get_n(h) > n:
            h = h - 2
            break

    space = 0
    for x in range(h, 0, -2):
        print(''.join([' '] * space + [symbol]*x + [' ']*space))
        space += 1
    space = space - 1
    for x in range(3, h+1, 2):
        # print(space)
        space -= 1
        print(''.join([' '] * space + [symbol]*x + [' ']*space))

    print(n - get_n(h))

