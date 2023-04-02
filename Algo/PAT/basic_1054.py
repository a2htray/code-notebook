#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/2

"""
PAT 乙级 1054
"""

if __name__ == '__main__':
    num = int(input())
    tokens = list(input().split(' '))

    total = 0
    count = 0
    for token in tokens:
        try:
            temp = float(token)

            if '.' in token:
                if len(token.split('.')[1]) > 2:
                    print(f'ERROR: {token} is not a legal number')
                    continue

            if -1000 <= temp <= 1000:
                count = count + 1
                total = total + round(temp, 2)
            else:
                print(f'ERROR: {token} is not a legal number')
        except:
            print(f'ERROR: {token} is not a legal number')

    if count == 0:
        print('The average of 0 numbers is Undefined')
    elif count == 1:
        print("The average of {} number is {:.2f}".format(count, total / count))
    else:
        print("The average of {} numbers is {:.2f}".format(count, total / count))
