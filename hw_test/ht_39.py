# -*- coding: utf-8 -*-
# @Time : 2020/6/19 9:50
# @Author : Mamamooo
# @Site :
# @File : ht_39.py
# @Software: PyCharm
"""
输入描述:
输入一行字符串，可以有空格

输出描述:
统计其中英文字符，空格字符，数字字符，其他字符的个数
"""


while True:
    try:
        string = input()
        a,n,s,o = 0,0,0,0

        for i in string:
            if 'A' <= i <= 'Z' or 'a' <= i <= 'z':
                a += 1
            elif '0' <= i <= '9':
                n += 1
            elif i == ' ':
                s += 1
            else:
                o += 1

        print(a,s,n,o,sep='\n')

    except:
        break