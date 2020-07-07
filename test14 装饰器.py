#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:20/2/17

# 使用@log 前需要先定义装饰器函数吗，不然会提示log示定义
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2015-3-25')


print(now())
