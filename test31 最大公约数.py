#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Aalon time:20/7/9

# 最大公约数
from functools import reduce


def hcf(x, y):
    """该函数返回两个数的最大公约数"""

    for i in range(1, min(x, y) + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i

    return hcf


# 用户输入两个数字
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))
# print(num1, "和", num2, "的最大公约数为", hcf(num1, num2))

# 采用匿名函数和高阶函数来简化代码
# print(max(map(lambda i : i if (x % i == 0) and (y % i == 0), list(range(1,min(x,y)+1)))))
# print(max(map(lambda i : i, list(range(1,min(x,y)+1)))))
# 多行语句
# print(num1, '和', num2, '最大公约数为：',max(map(lambda i:i if ((num1  % i == 0) and (num1 % i == 0)) , range(1, min(num1, num2) + 1))))
print(num1, '和', num2, '最大公约数为：',max(map(lambda i: i, range(1, min(num1, num2) + 1))))
# 上式作了简化，但还没解决条件判别放入匿名函数内，后期多练习了再来看
