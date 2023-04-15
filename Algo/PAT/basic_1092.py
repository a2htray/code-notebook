#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/15

"""
PAT 乙级 1092
"""

if __name__ == '__main__':
    n, m = map(int, input().split())
    sales = [0] * n

    for _ in range(m):
        for i, v in enumerate(map(int, input().split())):
            sales[i] += v

    max_sale = max(sales)

    print(max_sale)

    print(' '.join([str(i + 1) for i, v in enumerate(sales) if v == max_sale]))
