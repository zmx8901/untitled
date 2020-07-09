#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Aalon time:20/7/8
def is_number(s):
    try:
        float(s)  # 如果能运行float(s)语句，返回True（字符串s是浮点数）
        return True
    except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"
        pass  # 如果引发了ValueError这种异常，不做任何事情（pass：不做任何事情，一般用做占位语句）
    try:
        import unicodedata
        unicodedata.numeric(s)  # 把一个表示数字的字符串转换为浮点数返回的函数
        return True
    except(TypeError, ValueError):
        pass
    return False

print(is_number('四五'))  # True
# 版权号
