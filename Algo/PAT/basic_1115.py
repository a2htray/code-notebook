#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/5/8

"""
PAT 乙级 1115
"""

if __name__ == '__main__':
    num1, num2 = map(int, input().split())
    nums = [num1, num2]
    available_values = {abs(num1 - num2): True}

    n, m = map(int, input().split())
    num_matrix = []

    for i in range(n):
        num_matrix.append(list(map(int, input().split())))

    in_pool = list(range(n))
    for t in range(m):
        round_str = f'Round #{t+1}:'
        for u in in_pool:
            user = u + 1
            if num_matrix[u][t] in available_values:
                for num in nums:
                    available_values[abs(num_matrix[u][t] - num)] = True
                nums.append(num_matrix[u][t])
            else:
                pri

