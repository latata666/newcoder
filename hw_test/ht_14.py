# -*- coding: utf-8 -*-

"""
给定n个字符串，请对n个字符串按照字典序排列。
"""

import sys
while True:
    try:
        n = int(input())
        d = []
        for i in range(n):
            str = input()
            d.append(str)
        d.sort()
        for i in range(len(d)):
            print(d[i])
    except:
        break