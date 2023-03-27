#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/3/25

"""
PAT 乙级 1041
"""

if __name__ == '__main__':
    n = int(input())

    student_dict = {}
    for _ in range(n):
        tokens = input().split(' ')
        student_dict[tokens[1]] = [tokens[0], tokens[2]]

    _ = input()
    nums = input().split(' ')
    for num in nums:
        print(' '.join(student_dict[num]))
