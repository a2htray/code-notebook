#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/14

"""
PAT 乙级 1078
"""


def print_compress(line):
    cnt = 1
    n = len(line)
    if n != 0:
        pre = line[0]
        for i in range(1, n):
            if line[i] == pre:
                cnt += 1
            else:
                if cnt >= 2:
                    print(cnt, end='')
                print(pre, end='')
                cnt = 1
                pre = line[i]
        if cnt >= 2:
            print(cnt, end='')
        print(pre)


def print_decompress(line):
    num = ''
    cnt = 1
    for i in range(len(line)):
        if '0' <= line[i] <= '9':
            num += line[i]
        else:
            if len(num) > 0:
                cnt = int(num)
            while cnt > 0:
                print(line[i], end='')
                cnt -= 1
            cnt = 1
            num = ''
    print('')


if __name__ == '__main__':
    cd = input()

    line = input()
    if cd == 'C':
        print_compress(line)
    else:
        print_decompress(line)
