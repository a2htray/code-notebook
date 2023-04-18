#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/14

"""
PAT 乙级 1079
"""


def is_palindromic(num: int):
    num_str = str(num)
    if len(num_str) == 1:
        return True

    i = 0
    j = len(num_str) - 1

    while j - i != 0 and j - i != 1:
        if num_str[i] != num_str[j]:
            return False
        i += 1
        j -= 1
    return True


def reverse_num(num: int):
    num_str = str(num)
    return int(num_str[::-1]), num_str[::-1]


if __name__ == '__main__':
    num = int(input())
    if is_palindromic(num):
        print(f'{num} is a palindromic number.')
        exit(0)

    cnt = 0
    while cnt < 10:
        num_reverse, num_reverse_str = reverse_num(num)
        print(f'{num} + {num_reverse_str} = {num + num_reverse}')
        num = num + num_reverse
        if is_palindromic(num):
            print(f'{num} is a palindromic number.')
            exit(0)
        cnt += 1

    if cnt == 10:
        print('Not found in 10 iterations.')
