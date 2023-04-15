#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/15

"""
PAT 乙级 1084
"""


def compute_next(d: str):
    ret = ''
    pre = d[0]
    cnt = 1
    for c in d[1:]:
        if pre == c:
            cnt += 1
        else:
            ret += pre + str(cnt)
            pre = c
            cnt = 1

    ret += pre + str(cnt)
    return ret


if __name__ == '__main__':
    d, n = map(int, input().split())
    d = str(d)
    while n != 1:
        d = compute_next(d)
        n -= 1

    print(d)
