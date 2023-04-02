#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/1

"""
PAT 乙级 1047
"""

if __name__ == '__main__':
    n = int(input())
    scores = [0] * 1000
    for _ in range(n):
        tokens = input().split(' ')
        scores[int(tokens[0].split('-')[0]) - 1] += int(tokens[1])

    max_score = max(scores)
    print(scores.index(max_score) + 1, max_score)
