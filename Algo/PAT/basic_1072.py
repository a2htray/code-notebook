#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/10

"""
PAT 乙级 1072
"""

if __name__ == '__main__':
    n, m = map(int, input().split())
    item_dict = {}
    for item in input().split():
        item_dict[item] = True

    cnt_stu, cnt_item = 0, 0
    for _ in range(n):
        tokens = input().split()
        name = tokens[0]
        items = tokens[2:]

        stu_items = []
        for item in items:
            if item in item_dict:
                cnt_item += 1
                stu_items.append(item)

        if len(stu_items) != 0:
            print(name + ':', ' '.join(stu_items))
            cnt_stu += 1

    print(cnt_stu, cnt_item)



