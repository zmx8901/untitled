#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:20/2/15

# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。


def normalize(name):
    if name != " ":
        name = name[0].upper() + name[1:].lower()
    return name


L1 = ['adam', 'LISA', 'barT', ' ']
L2 = list(map(normalize, L1))
print(L2)

# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
from functools import reduce


def prod(L):
    return reduce(lambda x, y: x * y, L)


'''
from functools import reduce

def prod(L):
    def multi(x, y):
        return x*y
    return reduce(multi, L)
'''

L = [3, 5, 7, 9]
print('3 * 5 * 7 * 9 =', prod(L))


##利用map和reduce编写一个str2float函数,把字符串'123.456'转换成浮点数
## map 传递一个参数，reduce 传递两个参数
def str2float(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        # 上一行定义一个集合Dict { key: value, }，可以简单地使用 d[key] 的形式来查找对应的 value
        # 二是使用dict本身提供的一个 get 方法，在Key不存在的时候，返回None：
        # print(digits['2'])  #测试语句，
        return digits[s]

    #    return digits.get(s)

    index = s.find('.')  # find()方法，返回索引值
    print(index)
    L1 = list(map(char2num, s[:index]))
    L2 = list(map(char2num, s[index + 1:]))
    return reduce(fn, L1) + reduce(fn, L2) / pow(10, len(L2))  # pow() 方法返回 xy（x的y次方） 的值


print('str2float(\'123.456\') =', str2float('123.456'))
print(str2float('3.1415926'))
