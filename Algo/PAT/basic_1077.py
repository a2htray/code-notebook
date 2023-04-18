#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/14

"""
PAT 乙级 1077
"""

if __name__ == '__main__':
    n, m = map(int, input().split())
    for _ in range(n):
        scores = list(map(int, input().split()))
        t_score = scores[0]
        g_scores = [score for score in scores[1:] if 0 <= score <= m]
        g_scores.sort()

        valid_scores = g_scores[1:-1]
        final_score = (t_score + 1.0 * sum(valid_scores) / len(valid_scores)) / 2 + 0.5
        print(int(final_score))
