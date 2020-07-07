#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:20/2/16
'''
假设我们用一组tuple表示学生名字和成绩：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
请用sorted()对上述列表分别按名字排序：
'''
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


# # 测试语句，读取列表
# name=[x[0] for x in L]
# print(name)
print(L[0])
def re_name(t):
    return t[0].lower()


L1 = sorted(L, key=re_name)
print(L1)


def by_scort(t):
    return t[1] # 这个有点意思，直接返回元组中的后一个均元素


L2 = sorted(L, key=by_scort, reverse=True)
print(L2)
# def by_name(t):
#
#     return L
#
#
# L2 = sorted(L, key=by_name)
# print(L2)
