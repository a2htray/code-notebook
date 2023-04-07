#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/7

"""
PAT 乙级 1091
"""

if __name__ == '__main__':
    _ = input()
    nums = map(int, input().split())

    for num in nums:
        yes = False
        n = 1
        for i in range(1, 10):
            if str(i * num ** 2).endswith(str(num)):
                yes = True
                n = i
                break
        if yes:
            print(n, n * num ** 2)
        else:
            print('No')
