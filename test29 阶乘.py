#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Aalon time:20/7/8
from functools import reduce

num = int(input("请输入一个数字: "))
factorial = 1

# 查看数字是负数，0 或 正数
if num < 0:
    print("抱歉，负数没有阶乘")
elif num == 0:
    print("0 的阶乘为 1")
else:

    # for i in range(1, num + 1):
    #     factorial = factorial * i
    # print("%d 的阶乘为 %d" % (num, factorial))
    # 以上代码用匿名函数来表达
    # 匿名函数 reduce 需从 functools 中导入，reduce需两个参数
    print(reduce(lambda x, y: x * y, range(1, num + 1)))
