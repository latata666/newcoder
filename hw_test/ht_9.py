# -*- coding: utf-8 -*-

"""
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
"""

import sys
while True:
    try:
        n = input()
        s = ''
        print(n[::-1])
        for ch in n[::-1]:
           if ch not in s:
               s += ch
        print(s)
    except:
        break