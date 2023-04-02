#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/1

"""
PAT 乙级 1052
"""
import sys


def pick_elements(s):
    s = str(s)
    elements = []
    element = ''
    for c in s:
        if c == '[':
            element = ''
        elif c == ']':
            elements.append(element)
        else:
            element += c
    return elements


if __name__ == '__main__':
    hand_elements = pick_elements(sys.stdin.buffer.readline())
    n_hand_elements = len(hand_elements)
    eye_elements = pick_elements(sys.stdin.buffer.readline())
    n_eye_elements = len(eye_elements)
    mouth_elements = pick_elements(sys.stdin.buffer.readline())
    n_mouth_elements = len(mouth_elements)

    n = int(input())
    emojis = [''] * n

    for i in range(n):
        print(str(sys.stdin.buffer.readline()).split(' '))
        left_hand, left_eye, mouth, right_eye, right_hand = map(int, str(sys.stdin.buffer.readline()).split(' '))
        if left_hand > n_hand_elements or left_eye > n_eye_elements or mouth > n_mouth_elements or right_eye > n_eye_elements or right_hand > n_hand_elements:
            continue
        emojis[i] = hand_elements[left_hand-1] + '(' + eye_elements[left_eye-1] + mouth_elements[mouth-1] + eye_elements[right_eye-1] + ')' + hand_elements[right_hand-1]

    for emoji in emojis:
        if emoji == '':
            print('Are you kidding me? @\\/@')
        else:
            print(emoji)

