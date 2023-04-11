#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/11

"""
PAT 乙级 1034
"""

import math
import copy


class RationalNumber:
    def __init__(self, sign, numerator, denominator):
        self.sign = sign
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def parse(s: str):
        sign = '-' if s.startswith('-') else '+'
        if sign == '-':
            s = s[1:]
        numerator, denominator = map(int, s.split('/'))
        return RationalNumber(sign, numerator, denominator)

    def __str__(self):
        k = self.numerator // self.denominator
        a = self.numerator % self.denominator
        fmt = '(-%s)' if self.sign == '-' else '%s'

        denominator = self.denominator
        t = math.gcd(a, denominator)
        if t != 0:
            a = a // t
            denominator = denominator // t

        if a == 0:
            return fmt % k
        else:
            if k == 0:
                return fmt % (str(a) + '/' + str(denominator))
            else:
                return fmt % (str(k) + ' ' + str(a) + '/' + str(denominator))


def add(ab1: RationalNumber, ab2: RationalNumber):
    a1 = -ab1.numerator if ab1.sign == '-' else ab1.numerator
    a2 = -ab2.numerator if ab2.sign == '-' else ab2.numerator

    numerator = a1 * ab2.denominator + a2 * ab1.denominator
    denominator = ab1.denominator * ab2.denominator

    if numerator < 0:
        sign = '-'
        numerator = -numerator
    else:
        sign = '+'
    return RationalNumber(sign, numerator, denominator)


def sub(ab1: RationalNumber, ab2: RationalNumber):
    ab1 = copy.deepcopy(ab1)
    ab2 = copy.deepcopy(ab2)
    if ab2.sign == '-':
        ab2.sign = '+'
    else:
        ab2.sign = '-'
    return add(ab1, ab2)


def mul(ab1: RationalNumber, ab2: RationalNumber):
    if (ab1.sign == '-' and ab2.sign == '+') or (ab1.sign == '+' and ab2.sign == '-'):
        sign = '-'
    else:
        sign = '+'

    numerator = ab1.numerator * ab2.numerator
    denominator = ab1.denominator * ab2.denominator
    return RationalNumber(sign, numerator, denominator)


def div(ab1: RationalNumber, ab2: RationalNumber):
    if ab2.numerator == 0:
        return 'Inf'

    ab1 = copy.deepcopy(ab1)
    ab2 = copy.deepcopy(ab2)
    ab2.numerator, ab2.denominator = ab2.denominator, ab2.numerator

    return mul(ab1, ab2)


if __name__ == '__main__':
    tokens = input().split()
    num1 = RationalNumber.parse(tokens[0])
    num2 = RationalNumber.parse(tokens[1])

    print(num1, '+', num2, '=', add(num1, num2))
    print(num1, '-', num2, '=', sub(num1, num2))
    print(num1, '*', num2, '=', mul(num1, num2))
    print(num1, '/', num2, '=', div(num1, num2))
