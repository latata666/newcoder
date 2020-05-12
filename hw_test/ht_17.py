# -*- coding: utf-8 -*-
# @Time : 2020/5/11 14:44
# @Author : Mamamooo
# @Site :
# @File : ht_17.py
# @Software: PyCharm
"""
开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。
从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。
"""

import  sys
while True:
    try:
        #pos = input().split(";")
        pos = sys.stdin.readline().split(';')
        initx = 0
        inity = 0
        for i in pos:
            if i[0] == 'A':
                initx -= int(i[1:])
            if i[0] == 'D':
                initx += int(i[1:])
            if i[0] == 'W':
                inity += int(i[1:])
            if i[0] == 'S':
                inity -= int(i[1:])
            else:
                continue
        print(str(initx) + ',' + str(inity))
    except:
        break

