#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Aalon time:20/7/8

year = int(input('please input a number:'))
if year % 100 == 0:
    if year % 400 == 0 or year % 4 == 0:  # 整百年且能被400整除为闰年
        print('{}是闰年'.format(year))
    else:
        print('{}不是闰年'.format(year))
elif year % 4 == 0:  #非整百年且能被4整除的为闰年
    print('{}是闰年'.format(year))
else:
    print('{}不是闰年'.format(year))
