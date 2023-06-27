#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: a2htray
# create date: 2023/4/23

"""
递归版本的归并排序
"""
from typing import List


def r_merge(left: List[int], right: List[int]) -> List[int]:
    ret = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            ret.append(left[i])
            i += 1
        else:
            ret.append(right[j])
            j += 1

    if i < len(left):
        ret = ret + left[i:]
    if j < len(right):
        ret = ret + right[j:]

    return ret


def r_merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = r_merge_sort(arr[:mid])
    right = r_merge_sort(arr[mid:])

    return r_merge(left, right)


if __name__ == '__main__':
    arr1 = [9, 8, 6, 6, 5, 4, 3, 2, 1]
    print(r_merge_sort(arr1))

    arr2 = [3, 1, 4, 4, 6, 5, 8]
    print(r_merge_sort(arr2))
