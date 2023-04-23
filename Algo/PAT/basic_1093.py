#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/15

"""
PAT 乙级 1093
"""

if __name__ == '__main__':
    line1 = input()
    line2 = input()

    tokens = []
    stat = {}
    for token in line1:
        if token not in stat:
            stat[token] = True
            tokens.append(token)

    for token in line2:
        if token not in stat:
            stat[token] = True
            tokens.append(token)

    print(''.join(tokens))
