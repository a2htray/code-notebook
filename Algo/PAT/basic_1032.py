#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/3/12

"""
PAT 乙级 1032
"""

if __name__ == '__main__':
    n = int(input())
    scores = [0] * n

    for _ in range(n):
        school_no, score = map(int, input().split())
        scores[school_no - 1] += score

    max_score = max(scores)
    max_score_index = scores.index(max_score)

    print(f'{max_score_index + 1} {max_score}')
