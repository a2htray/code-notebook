#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/9

"""
PAT 乙级 1061
"""

if __name__ == '__main__':
    n, m = map(int, input().split())

    scores = list(map(int, input().split()))
    answer = list(map(int, input().split()))

    for _ in range(n):
        stu_answer = list(map(int, input().split()))
        score = 0
        for i in range(m):
            if answer[i] == stu_answer[i]:
                score += scores[i]
        print(score)
