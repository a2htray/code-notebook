#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/15

"""
PAT 乙级 1094
"""
import math


def is_prime(n: int):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    l, k = map(int, input().split())
    line = input()

    for i in range(0, l - k + 1):
        n = int(line[i:i + k])
        if is_prime(n):
            print(line[i:i + k])
            exit(0)

    print(404)
