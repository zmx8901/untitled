#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:20/2/17

class Student(object):  # 定义类
    def __init__(self, name, score, age):  # 注意是__init__,不是__int__
        self.name = name
        self.score = score
        self.age = age

    def print_score(self):  # 定义方法，和类放一起，称为类的方法
        print('%s: %s' % (self.name, self.score))

    # 不用self直接用std也能运行，有何不同
    # def print_score(std):
    #     print('%s: %s' % (std.name, std.score))
    def get_grade(self):  # 这里没测试通，在雪峰-面向对象编程-访问限制里
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.name


"""
既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，
可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了
"""

bart = Student("Bart Simpson", 595, 12)
print(bart.name)
bart.print_score()
print(bart.get_grade())  # 用到了类的方法调用，不从外部调用
print(bart.get_name())
