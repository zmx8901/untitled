#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:20/2/16

'''
高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
求和函数如果不需要立刻求和，可以不返回求和的结果，而是返回求和的函数：

内层函数引用了外层函数的变量（参数也算变量），然后返回内层函数的情况，称为闭包（Closure）。
返回的函数并没有立刻执行，而是直到调用了f()才执行
调用外层函数时，返回的并不是求和结果，而是求和函数：
同一外闭包调用两次，调用结果相互不影响。调用结果相互不影响。
'''


# 返回的是（求和）函数，
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1)  # 返回是函数
print(f1())  # 调用函数返回的才是结果
print(f2())  # 调用函数返回的才是结果
print(f1() == f2())
print(f1 == f2)


def count():
    fs = []
    for i in range(1, 4):
        def f():
            j = i * i
            return j

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
# 上述两个结果全部都是9，返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
