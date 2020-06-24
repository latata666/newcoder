# -*- coding: utf-8 -*-
# @Time : 2020/6/17 15:48
# @Author : Mamamooo
# @Site :
# @File : ht_37.py
# @Software: PyCharm
"""
有一只兔子，从出生后第3个月起每个月都生一只兔子，小兔子长到第三个月后每个月又生一只兔子，
假如兔子都不死，问每个月的兔子总数为多少？
"""

while True:
    try:
        month = int(input())
        if month < 3:
            print(1)
        else:
            a, b = 1, 1
            for i in range(3, month + 1):
                a, b = b, a + b  # 依据a,b的初始值，先计算‘=’号右边的值，暂时不考虑左边的值。
            print(b)
    except:
        break
