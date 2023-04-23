#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/15

"""
PAT 乙级 1108
"""

if __name__ == '__main__':
    chars = ['S', 't', 'r', 'i', 'n', 'g']
    cnts = [0] * 6

    for c in input():
        if c == 'S':
            cnts[0] += 1
        elif c == 't':
            cnts[1] += 1
        elif c == 'r':
            cnts[2] += 1
        elif c == 'i':
            cnts[3] += 1
        elif c == 'n':
            cnts[4] += 1
        elif c == 'g':
            cnts[5] += 1

    counter = sum(cnts)

    while counter != 0:
        for i, v in enumerate(cnts):
            if v != 0:
                print(chars[i], end='')
                cnts[i] -= 1
                counter -= 1
    print()
