#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/11

"""
PAT 乙级 1059
"""
import math


def is_prime(n):
    if n == 2:
        return True
    flag = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            flag = False
            break
    return flag


if __name__ == '__main__':
    n = int(input())
    ids = [''] * n
    id_order = {}
    for i in range(n):
        ids[i] = input()
        id_order[ids[i]] = i

    had_checked = {}
    k = int(input())
    for _ in range(k):
        id_str = input()
        if id_str not in id_order:
            print(f'{id_str}: Are you kidding?')
        else:
            if id_str in had_checked:
                print(f'{id_str}: Checked')
                continue

            had_checked[id_str] = True
            if id_order[id_str] == 0:
                print(f'{id_str}: Mystery Award')
            elif is_prime(id_order[id_str] + 1):
                print(f'{id_str}: Minion')
            else:
                print(f'{id_str}: Chocolate')
