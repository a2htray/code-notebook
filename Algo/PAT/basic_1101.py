#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/6

"""
PAT 乙级 1101
"""

if __name__ == '__main__':
    tokens = input().split(' ')

    num_str = tokens[0]
    d = int(tokens[1])

    new_num_str = num_str[-d:] + num_str[:-d]

    print('%.2f' % (1.0 * int(new_num_str) / int(num_str)))
