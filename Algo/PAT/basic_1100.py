#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/5/8

"""
PAT 乙级 1100
"""

if __name__ == '__main__':
    n = int(input())

    pool = {}
    for _ in range(n):
        id_str = input()
        pool[id_str] = [id_str, int(id_str[6:14]), False]

    m = int(input())

    count = 0
    max_age_id_str = ''
    birthday = 20190101
    for _ in range(m):
        id_str = input()
        if int(id_str[6:14]) < birthday:
            birthday = int(id_str[6:14])
            max_age_id_str = id_str

        if id_str in pool:
            count = count + 1
            pool[id_str][2] = True

    if count != 0:
        print(count)
        max_age_id_str = ''
        birthday = 20190101
        for id_str, info in pool.items():
            if info[2]:
                if info[1] < birthday:
                    birthday = info[1]
                    max_age_id_str = id_str
        print(max_age_id_str)
    else:
        print(0)
        print(max_age_id_str)
