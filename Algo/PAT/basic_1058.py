#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/3

"""
PAT 乙级 1058
"""

# 3 4
# 3 4 2 a c
# 2 5 1 b
# 5 3 2 b c
# 1 5 4 a b d e
# (2 a c) (2 b d) (2 a c) (3 a b e)
# (2 a c) (1 b) (2 a b) (4 a b d e)
# (2 b d) (1 e) (2 b c) (4 a b c d)

if __name__ == '__main__':
    n, m = map(int, input().split())
    problems = []

    for _ in range(m):
        tokens = input().split()
        problems.append([
            int(tokens[0]),
            int(tokens[1]),
            int(tokens[2]),
            set(tokens[3:])
        ])

    answers = []
    for _ in range(n):
        tokens = input().split(')')[:-1]
        answer = []
        for token in tokens:
            answer.append(set(token.strip(' ')[1:].split(' ')[1:]))

        answers.append(answer)

    counts = [0] * m
    for i in range(n):
        score = 0
        for j, item in enumerate(answers[i]):
            if item == problems[j][3]:
                score += problems[j][0]
            else:
                counts[j] += 1
        print(score)

    print(counts)

