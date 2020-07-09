#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Aalon time:20/7/8

# python 实现99乘法表
for i in range(1, 10):
    for j in range(1, i + 1):  # 注意这里不能写为range(1,i),导致空
        # 以下为输出的三种写法，还有一种left,righe的写法
        print(j, 'x', i, '=', i * j, '\t', end='')  # 数字自动有两个空格
        print('{} x {} = {}\t'.format(j, i, j * i), end='') #{}外加空格
        print('{0:1d} x {1:1d} = {2:2d}\t'.format(j, i, j * i), end='')
    print()  # 此外作换行用
