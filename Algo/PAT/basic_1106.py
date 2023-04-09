#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/9

"""
PAT 乙级 1106
"""


def generate_tokens(tokens, n):
    if n == 4:
        return tokens
    return generate_tokens(tokens + [sum(tokens[-4:]) % 10], n - 1)


if __name__ == '__main__':
    n = int(input())

    tokens = [2, 0, 1, 9]

    if n <= 4:
        print(''.join(map(str, tokens[0:n])))
    else:
        print(''.join(map(str, generate_tokens(tokens, n))))
