#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/7

"""
PAT 乙级 1096
"""


def get_divisors(n):
    """求因数"""
    vs = []
    for i in range(1, n + 1):
        if n % i == 0:
            vs.append(i)
    return vs


if __name__ == '__main__':
    _ = int(input())
    nums = map(int, input().split())
    for num in nums:
        divisors = get_divisors(num)
        n = len(divisors)
        if len(divisors) < 4:
            print('No')
            continue

        yes = False
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                for k in range(j + 1, n - 1):
                    for t in range(k + 1, n):
                        if (divisors[i] + divisors[j] + divisors[k] + divisors[t]) % num == 0:
                            yes = True
                            break
        if not yes:
            print('No')
        else:
            print('Yes')
