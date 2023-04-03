#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/3

"""
PAT 乙级 1058
"""
from typing import List


class Problem:
    def __init__(self, seq, score, cnt_op, cnt_correct_op, answers):
        self.seq = seq
        self.score = score
        self.cnt_op = cnt_op
        self.cnt_correct_op = cnt_correct_op
        self.answers = set(answers)
        self.cnt_incorrect = 0


def get_answers(line: str):
    return [answer.strip(' ')[1:].split(' ')[1:] for answer in line.split(')') if answer != '']


def all_right(problems: List[Problem]):
    right = True
    for p in problems:
        if p.cnt_incorrect != 0:
            right = False
    return right


if __name__ == '__main__':
    m, n = map(int, input().split(' '))

    problems = []
    for i in range(n):
        tokens = input().split(' ')
        problems.append(Problem(
            seq=i+1,
            score=int(tokens[0]),
            cnt_op=int(tokens[1]),
            cnt_correct_op=int(tokens[2]),
            answers=tokens[3:]
        ))

    # for p in problems:
    #     print(p.seq, p.score, p.cnt_op, p.cnt_correct_op, p.answers)

    for i in range(m):
        answers = get_answers(input())
        score = 0
        for j, answer in enumerate(answers):
            if set(answer) == problems[j].answers:
                score += problems[j].score
            else:
                problems[j].cnt_incorrect += 1
        print(score)

    if all_right(problems):
        print('Too simple')
    else:
        pass




