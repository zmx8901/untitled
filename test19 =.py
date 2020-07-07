#!/usr/bin/python3

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
# print(a,b)
while b < 10:
    print(b, end=' ')
    a, b = b, a + b  # 右边表达式的执行顺序是从左往右的。
import os
print(os.environ)
# print(os.environ)
