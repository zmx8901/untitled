#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:20/2/17
import functools
int2 = functools.partial(int, base=2)  #partial 局部的
print(int2("100"))
int8=functools.partial(int,base=8)
print(int8("100"))
print(int8("100",base=10))

'''
当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
'''