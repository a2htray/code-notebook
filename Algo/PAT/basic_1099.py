#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/24

"""
PAT 乙级 1099
"""


def is_prime(n: int) -> bool:
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, n // 2 + 2):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    print(is_prime(11))