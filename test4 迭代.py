#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:20/2/14
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：

def findMinAndMax(L):
    if L!= []:
        (max, min) = (L[0], L[0])
        for x in L:
            if x > max:
                max = x
            if x < min:
                min = x
        return (max, min)
    else:
        return (None, None)

L=[1,23,4]
print(findMinAndMax(L))