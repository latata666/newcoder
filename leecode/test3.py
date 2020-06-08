# -*- coding: utf-8 -*-

"""
计算字符串最后一个单词的长度，单词以空格隔开。
"""

def str_count(str):
    print(len(str))
    for i in range(len(str)):
        print(i)
        if str[len(str)-1-i]==' ':
            count=i
            break
        else:
            count=i+1
    print(count)

str_count("hello world")