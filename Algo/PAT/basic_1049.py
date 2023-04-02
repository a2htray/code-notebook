#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/1

"""
PAT 乙级 1049
"""

from decimal import Decimal

if __name__ == '__main__':
    n = int(input())
    nums = list(map(Decimal, input().split(' ')))

    answer = Decimal(0)
    for i in range(1, n + 1, 1):
        answer += nums[i - 1] * i * (n + 1 - i)

    print(answer.quantize(Decimal('0.00')))
