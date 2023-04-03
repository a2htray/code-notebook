#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/3

"""
PAT 乙级 1056
"""

if __name__ == '__main__':
    ns = list(map(int, input().split(' ')))[1:]

    print((sum(ns) * 10 + sum(ns)) * (len(ns) - 1))
