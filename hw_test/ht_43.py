# -*- coding: utf-8 -*-
# @Time : 2020/6/28 9:36
# @Author : Mamamooo
# @Site :
# @File : ht_43.py
# @Software: PyCharm
"""
迷宫问题
输入描述:
输入两个整数，分别表示二位数组的行数，列数。再输入相应的数组，其中的1表示墙壁，0表示可以走的路。
数据保证有唯一解,不考虑有多解的情况，即迷宫只有一条通道。
输出描述:
左上角到右下角的最短路径，格式如样例所示。
"""

def print_path(path):
    for i in path:
        print('(%d,%d)' %(i[0],i[1]))

def migong(i,j,MG,I,J):
    lu = [[i,j]]
    print(lu)
    while i != I-1 or j != J-1:
        if i < I-1 and MG[i+1][j] == 0:
            i += 1
            lu.append([i,j])
            print(lu)
        elif j < J-1 and MG[i][j+1] == 0:
            j += 1
            lu.append([i,j])
            print(lu)

    return lu

while True:
    try:
        [a,b] = [int(i) for i in input().split()]
        m = []
        for i in range(a):
            m.append([int(i) for i in input().split()])

        print(m,a,b)
        path = migong(0,0,m,a,b)
        print(path)
        print_path(path)
    except:
        break