#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/18

"""
PAT 乙级 1075
"""

import sys

Add, N, K = sys.stdin.readline().strip().split()

add_next, add_data = {}, {}  # 地址 to 下一个地址，地址 to 数据
for i in range(int(N)):
    address, data, nex = sys.stdin.readline().strip().split()
    add_next[address], add_data[address] = nex, int(data)

a = Add
res_add0, res_add1, res_add2 = [], [], []
while True:
    if a == '-1':
        break
    if add_data[a] < 0:
        res_add0.append(a)  # 负值元素
    elif 0 <= add_data[a] <= int(K):
        res_add1.append(a)  # [0,K]
    else:
        res_add2.append(a)  # 大于 K
    a = add_next[a]  # 按原链表顺序进行

res_add0.extend(res_add1)  # 合并成一个列表
res_add0.extend(res_add2)
res_add0.extend(['-1'])

for i in range(len(res_add0) - 1):
    print(res_add0[i], add_data[res_add0[i]], res_add0[i + 1])
