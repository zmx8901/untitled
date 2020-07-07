#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:20/2/16
L = map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(L)
print(list(L))  # 对'generator' 不能用list()函数这样操作，普通函数可以

print("-" * 20)


def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))
print(L)
print("改造上面的函数，用匿名函数来代替")
M = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(M)

N = filter(lambda n: n % 2 == 1, range(1, 20))
print(list(N))
