# -*- coding: utf-8 -*-
# @Time : 2020/8/31 10:16
# @Author : Mamamooo
# @Site :
# @File : hw_0829.py
# @Software: PyCharm
"""
一组同学中每个人有一张卡片，卡片上有一个数字该数字不超过6位 ，输入每个卡片上的数字，求他们能组成的最大的数字串。
例如：
输入45,9,813
输出 981345
思路：
比较两个数字字符串大小，如果str1+str2 组合过后的串大于等于str2+str1，那么认为str1是大于str2的；然后进行列表的排序，越大的排在前面。
"""

import sys


def judge(str1, str2):
    if (str1 + str2) >= (str2 + str1):
        return True
    else:
        return False

def bigSum(list_str):
    for i in range(len(list_str)):
        for j in range(len(list_str)):
            if j > i:
                if judge(list_str[i],list_str[j]) == False:
                    list_str[i],list_str[j] = list_str[j],list_str[i]

    print(''.join(list_str))


str = sys.stdin.readline().strip()
list_str = str.split(',')
bigSum(list_str)
