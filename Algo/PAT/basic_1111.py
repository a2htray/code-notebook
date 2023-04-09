#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/9

"""
PAT 乙级 1111
"""

month_dict = {
    'Jan': '01',
    'Feb': '02',
    'Mar': '03',
    'Apr': '04',
    'May': '05',
    'Jun': '06',
    'Jul': '07',
    'Aug': '08',
    'Sep': '09',
    'Oct': '10',
    'Nov': '11',
    'Dec': '12',
}

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        md, year = map(lambda s: s.strip(), input().split(','))
        month, day = md.split(' ')

        while len(year) != 4:
            year = '0' + year
        while len(day) != 2:
            day = '0' + day

        value = year + month_dict[month] + day

        i = 0
        j = 7
        yes = True
        while i <= 3 and j >= 4:
            if value[i] != value[j]:
                yes = False
                break
            i += 1
            j -= 1

        if yes:
            print('Y', value)
        else:
            print('N', value)
