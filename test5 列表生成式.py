#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:20/2/14

L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)
L = [m + n for m in 'ABC' for n in 'XYZ']
print(L)
import os

print([d for d in os.listdir('.')])  # 需要用方括号括起来,不然就只是一个地址

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])  # 标准模式，函数在前
# print(s.lower() for s in L)

# if语句放在函数位置需要有else,放在后面不能有else
print([x if x % 2 == 0 else -x for x in range(1, 11) if x % 2 == 0])

# 如果list中既包含字符串，又包含整数，将其中的字符串小写
L = ['HelLo', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L if isinstance(s, str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')