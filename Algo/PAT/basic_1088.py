#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/22

"""
PAT 乙级 1088
"""


def compare(m, v):
    if m < v:
        return 'Cong'
    if m == v:
        return 'Ping'
    return 'Gai'


if __name__ == '__main__':
    m, x, y = map(int, input().split())

    got = False

    for jia in range(99, 9, -1):
        yi = jia % 10 * 10 + jia // 10
        bing = abs(jia - yi) * 1.0 / x
        if bing * y == yi:
            got = True
            break

    if got:
        print(jia, compare(m, jia), compare(m, yi), compare(m, bing))
    else:
        print('No Solution')
