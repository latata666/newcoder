# -*- coding: utf-8 -*-
# @Time : 2020/6/16 16:51
# @Author : Mamamooo
# @Site :
# @File : ht_35.py
# @Software: PyCharm
"""
题目说明
蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。
样例输入
5
样例输出
1 3 6 10 15
2 5 9 14
4 8 13
7 12
11
"""

while True:
    try:
        n = int(input())
        c1 = [sum(range(i)) for i in range(1,n+2)]
        c2 = [i+1 for i in c1]
        print(c1,c2)

        for j in range(n):
            c2 = [i-1 for i in c2[1:]]
            print(' '.join(map(str,c2)))

    except:
        break

