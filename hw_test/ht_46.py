# -*- coding: utf-8 -*-
# @Time : 2020/7/8 9:34
# @Author : Mamamooo
# @Site :
# @File : ht_46.py
# @Software: PyCharm
"""
编写一个截取字符串的函数，输入为一个字符串和字节数，输出为按字节截取的字符串。但是要保证汉字不被截半个，
如"我ABC"4，应该截为"我AB"，输入"我ABC汉DEF"6，应该输出为"我ABC"而不是"我ABC+汉的半个"。
输入
我ABC汉DEF
6
输出
我ABC
"""

while True:
    try:
        s,n = input().strip().split()
        n = int(n)
        if s[n - 1].isalpha():
            res = s[:n]
        else:
            res = s[:n - 1]
        print(res)
    except:
        break
