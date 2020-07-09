#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Aalon time:20/7/8

# python 判断是否为质数
num1 = int(input('输入一个整数： '))


def is_primenumber(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(num, '不是质数')
                print(i, '乘于', num//i, '等于', num)
                break
        # 注意这个else对应的是上面的for 语句
        else:
                print(num, '是一个质数')
    else:
        print('请输入一个大于 1 的整数！')


is_primenumber(num1)
