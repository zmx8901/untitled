#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:20/2/18

f = open('test.txt', 'r')
a = f.read()
print(a)
f.close()

try:
    f = open('test.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

with open('test.txt', 'r') as f:
    print(f.read())
