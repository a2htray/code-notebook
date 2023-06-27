#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/6/5

"""
PAT 乙级 1114
"""
import math


def is_prime(n: int) -> bool:
    if n == 1:
        return False

    for i in range(3, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    date_str = input()

    all_prime = True
    for i in range(0, 8):
        s = date_str[i:]
        prime = is_prime(int(s))
        if not prime:
            all_prime = False
        print('%s %s' % (s, 'Yes' if prime else 'No'))

    if all_prime:
        print('All Prime!')
