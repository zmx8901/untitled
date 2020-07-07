#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:20/2/14

'''
杨辉三角定义如下：

          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
把每一行看做一个list，试写一个generator，不断输出下一行的list：
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
'''


# # 列表生成式较为便捷，采用yield函数，代码量较少,实现方式如下：
# def triangles():
#     L = [1]   # ([0]+L)两个list 相加，相当于里面的元素合成一个list
#     #     while True:
#         yield L
#         L = [sum(i) for i in zip([0] + L, L + [0])]  # 列表生成式,zip()函数将两个list合并为一个
#
#
# g = triangles()
# for i in range(1, 4):
#     print(next(g))

# 该方式用到了列表生成式，理解起来较困难，下面是另一种方式：
def triangles():
    ret = [1]
    while True:
        yield ret
        for i in range(1, len(ret)):
            ret[i] = pre[i] + pre[i - 1]
        ret.append(1)
        pre = ret[:]

g = triangles()
# print(g())    'generator' object is not callable
for i in range(1, 4):
    print(next(g))



# # 另一个不用生成器的版本,也采用了列表生成式
# def YangHui(num=10):
#     LL = [[1]]
#     for i in range(1, num):
#         LL.append(
#             [(0 if j == 0 else LL[i - 1][j - 1]) + (0 if j == len(LL[i - 1]) else LL[i - 1][j]) for j in range(i + 1)])
#     print("\n")
#     return LL
# print(YangHui(5))
