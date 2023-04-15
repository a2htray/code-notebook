#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/12
# link: https://www.liuchuo.net/archives/6503

"""
PAT 乙级 1089
"""

if __name__ == '__main__':
    n = int(input())
    vs = [0] * n
    for i in range(n):
        vs[i] = int(input())

    for i in range(n):
        for j in range(i + 1, n):
            lie = []  # 保存说慌的人的编号
            # 假设第 i 和 j 为狼人
            a = [1] * n
            a[i] = -1
            a[j] = -1

            for z in range(n):
                if vs[z] * a[abs(vs[z]) - 1] < 0:
                    lie.append(z)

            if len(lie) == 2 and a[lie[0]] + a[lie[1]] == 0:
                # 第 1 个条件要满足有 2 个说谎
                # 第 2 个条件要满足 2 个狼人只有一个说谎
                print(i + 1, j + 1)
                exit(0)
    print('No Solution')
