#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/3/10

"""
PAT 乙级 1028
"""
from functools import cmp_to_key


class Person:
    def __init__(self, name, year, month, day):
        self.name = name
        self.year = year
        self.month = month
        self.day = day


def cmp(v1: Person, v2: Person):
    if v1.year > v2.year:
        return 1
    elif v1.year < v2.year:
        return -1
    else:
        if v1.month < v2.month:
            return 1
        elif v1.month > v2.month:
            return -1
        else:
            return 1 if v1.day < v2.day else -1


if __name__ == '__main__':
    n = int(input())

    person_list = []

    for _ in range(n):
        tokens = input().split(' ')
        year, month, day = map(int, tokens[1].split('/'))
        if year > 2014:
            continue
        if year == 2014 and month > 9:
            continue
        if year == 2014 and month == 9 and day > 6:
            continue

        if year < 1814:
            continue
        if year == 1814 and month < 9:
            continue
        if year == 1814 and month == 9 and day < 6:
            continue

        person_list.append(Person(tokens[0], year, month, day))

    person_list.sort(key=cmp_to_key(cmp))
    if len(person_list) == 0:
        print(0)
    else:
        print(len(person_list), person_list[0].name, person_list[-1].name)

