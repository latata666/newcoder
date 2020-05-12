# -*- coding: utf-8 -*-

"""
编写一个函数，计算字符串中含有的不同字符的个数。字符在ACSII码范围内(0~127)，换行表示结束符，
不算在字符里。不在范围内的不作统计。注意是不同的字符
"""

while True:
    try:
        n = input()
        s = ''
        for ch in n:
           if ord(ch) >=0 and ord(ch) <= 127 and ch not in s:
               s += ch
        print(len(s))
    except:
        break

