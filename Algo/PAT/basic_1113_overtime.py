#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/23

"""
PAT 乙级 1113
"""

if __name__ == '__main__':
    m1 = {
         '0': 0,
         '1': 1,
         '2': 2,
         '3': 3,
         '4': 4,
         '5': 5,
         '6': 6,
         '7': 7,
         '8': 8,
         '9': 9,
         'a': 10,
         'b': 11,
         'c': 12,
         'd': 13,
         'e': 14,
         'f': 15,
         'g': 16,
         'h': 17,
         'i': 18,
         'j': 19,
         'k': 20,
         'l': 21,
         'm': 22,
         'n': 23,
         'o': 24,
         'p': 25,
         'q': 26,
         'r': 27,
         's': 28,
         't': 29,
     }

    m2 = {}

    for k, v in m1.items():
        m2[v] = k

    n1, n2 = input().split()

    l1, l2 = len(n1), len(n2)

    if l1 == l2:
        n1 = '0' + n1
        n2 = '0' + n2
    elif l1 > l2:
        n2 = ''.join(['0'] * (l1 - l2)) + n2
    else:
        n1 = ''.join(['0'] * (l2 - l1)) + n1

    ans = ''
    carry = 0
    for i in range(len(n1) - 1, -1, -1):
        c1 = (m1[n1[i]] + m1[n2[i]] + carry) % 30
        carry = (m1[n1[i]] + m1[n2[i]] + carry) // 30
        ans = m2[c1] + ans

    if carry != 0:
        ans = m2[carry] + ans

    ans = ans.lstrip('0')

    if ans == '':
        print(0)
    else:
        print(ans)
