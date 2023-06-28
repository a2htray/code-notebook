#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/6/6

"""
PAT 乙级 1112
"""

if __name__ == '__main__':
    n, t = map(int, input().split())
    nums = list(map(int, input().split()))

    idxes_pair = []
    max_num = -1

    # flag 为 0 时，表示需要找一个左端索引值
    # flag 为 1 时，表示需要找一个右端索引值
    flag = 0
    idxes = []
    for i in range(n):
        max_num = max(max_num, nums[i])

        if nums[i] > t and flag == 0:
            idxes.append(i)
            flag = 1
        elif nums[i] <= t and flag == 1:
            idxes.append(i - 1)
            flag = 0
            idxes_pair.append(idxes)
            idxes = []

        if flag == 1 and i == n - 1:
            idxes.append(i)
            idxes_pair.append(idxes)

    if len(idxes_pair) != 0:
        for v in idxes_pair:
            print('[%d, %d]' % (v[0], v[1]))
    else:
        print(max_num)
