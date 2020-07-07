#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:20/2/14

'''
不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值
'''
L = [x * x for x in range(10)]
g = (x * x for x in range(10))  # 将list的[]改为（）即可
print(L)
print(g)

for i in range(1, 3):
    print(next(g))
print("上面已输出前两个，下面从剩下的开始")
for j in g:
    print(j)


## print([next(g) for i in range(6, 10)])  # 不能再从第3个开始输出，不然会出错

'''
第二种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
'''

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
#
# print([i for i in fib(6)])  # print语句内部要采用[]方括号
# for i in fib(6):
#     print(i)
