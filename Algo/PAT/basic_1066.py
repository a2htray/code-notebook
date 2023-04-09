#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/9

"""
PAT 乙级 1066
"""

if __name__ == '__main__':
    m, n, a, b, r = map(int, input().split())

    graph = []
    for _ in range(m):
        graph.append(list(map(int, input().split())))

    for i in range(m):
        for j in range(n):
            if a <= graph[i][j] <= b:
                graph[i][j] = r

    for i in range(m):
        for j in range(n):
            v = str(graph[i][j])
            while len(v) < 3:
                v = '0' + v
            graph[i][j] = v

        print(' '.join(graph[i]))
