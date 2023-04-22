#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/22

"""
PAT 乙级 1025
"""
import sys

if __name__ == '__main__':
    tokens = sys.stdin.readline().strip().split()

    start = tokens[0]
    n = int(tokens[1])
    k = int(tokens[2])
    if k > n:
        k = n

    order_dict = {}  # addr: [value, next]
    for _ in range(n):
        tokens = sys.stdin.readline().strip().split()
        order_dict[tokens[0]] = [tokens[1], tokens[2]]

    nodes = []
    while start != '-1':
        nodes.append([start, order_dict[start][0]])
        start = order_dict[start][1]

    new_nodes = []

    for i in range(0, n // k):
        tmp = nodes[i*k:(i+1)*k]
        tmp.reverse()
        new_nodes = new_nodes + tmp

    nodes = new_nodes + nodes[-(n % k):]

    for i in range(n):
        if i == n - 1:
            print(nodes[i][0], nodes[i][1], '-1')
        else:
            print(
                nodes[i][0], nodes[i][1], nodes[i + 1][0])
