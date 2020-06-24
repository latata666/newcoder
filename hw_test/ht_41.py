# -*- coding: utf-8 -*-
# @Time : 2020/6/21 14:33
# @Author : Mamamooo
# @Site :
# @File : ht_40.py
# @Software: PyCharm
"""
题目描述
现有一组砝码，重量互不相等，分别为m1,m2,m3…mn；
每种砝码对应的数量为x1,x2,x3...xn。现在要用这些砝码去称物体的重量(放在同一侧)，问能称出多少种不同的重量。
注：
称重重量包括0

输入描述:
输入包含多组测试数据。
对于每组测试数据：
第一行：n --- 砝码数(范围[1,10])
第二行：m1 m2 m3 ... mn --- 每个砝码的重量(范围[1,2000])
第三行：x1 x2 x3 .... xn --- 每个砝码的数量(范围[1,6])
输出描述:
利用给定的砝码可以称出的不同的重量数
"""

while True:
    try:
        n = int(input())
        m = list(map(int,input().split()))
        x = list(map(int,input().split()))
        print(n,m,x,sep='\n')
        height = [0]
        for r in range(n):
            h_1 = [m[r] * i for i in range(x[r] + 1)]
            height = list(set([a+b for a in h_1 for b in height]))
            print(height)

        print(len(height))
    except:
        break

