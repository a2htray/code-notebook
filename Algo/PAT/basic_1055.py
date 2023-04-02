#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/2

"""
PAT 乙级 1055
"""
from functools import cmp_to_key


class Student:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __str__(self):
        return f'{self.name}:{self.height}'


def cmp(a: Student, b: Student):
    if a.height > b.height:
        return -1
    elif a.height < b.height:
        return 1
    else:
        if a.name > b.name:
            return 1
        else:
            return -1


if __name__ == '__main__':
    n, k = map(int, input().split(' '))
    students = []
    for i in range(n):
        tokens = input().split(' ')
        students.append(Student(name=tokens[0], height=int(tokens[1])))

    students.sort(key=cmp_to_key(cmp))

    for student in students:
        print(student)

