#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/10

"""
PAT 乙级 1067
"""

if __name__ == '__main__':
    tokens = input().split()
    password = tokens[0]
    n = int(tokens[1])

    user_password = input()
    while user_password != '#':
        if user_password == password:
            print('Welcome in')
            break
        else:
            print(f'Wrong password: {user_password}')
            n -= 1
            if n == 0:
                print('Account locked')
                break
        user_password = input()
