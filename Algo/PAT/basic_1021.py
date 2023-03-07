#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/3/7

"""
PAT 乙级 1021
"""


if __name__ == '__main__':
    counts = [0] * 10
    for s in input():
        counts[int(s)] += 1

    for i, count in enumerate(counts):
        if count != 0:
            print('%d:%d' % (i, count))
