# -*- coding: utf-8 -*-

"""
数据表记录包含表索引和数值（int范围的整数），请对表索引相同的记录进行合并，
即将相同索引的数值进行求和运算，输出按照key值升序进行输出。
"""

import sys
while True:
    try:
        n = int(input())
        d = {}
        for i in range(n):
            a,b = map(int,sys.stdin.readline().split())
            if a in d:
                d[a] += b
            else:
                d[a] = b
        for x in sorted(d.keys()):
            print(str(x) + ' '+str(d[x]))

    except:
        break