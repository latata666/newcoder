# -*- coding: utf-8 -*-
# @Time : 2020/6/7 10:11
# @Author : Mamamooo
# @Site :
# @File : ht_27.py
# @Software: PyCharm
"""
输入描述:
先输入字典中单词的个数，再输入n个单词作为字典单词。
输入一个单词，查找其在字典中兄弟单词的个数
再输入数字n

输出描述:
根据输入，输出查找到的兄弟单词的个数
"""


import sys

def isBrother(s1,s2):
    if s1 == s2 or len(s1) != len(s2):
        return False
    l1 = list(s1)
    l1.sort()
    l2 = list(s2)
    l2.sort()

    if l1 != l2:
        return False
    return True

while True:

    try:
        line = sys.stdin.readline()
        if not line:
            break
        line = line.strip().split()
        num = int(line[0])
        line_dic = line[1:num+1]
        word = line[-2]
        index = int(line[-1])
        brother = []

        for i in line_dic:
            if isBrother(i,word):
                brother.append(i)
        brother.sort()
        print(str(len(brother)))
        if index <= len(brother):
            print(brother[index - 1])

    except:
        break