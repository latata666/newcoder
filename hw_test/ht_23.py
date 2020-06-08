# -*- coding: utf-8 -*-
# @Time : 2020/5/18 13:53
# @Author : Mamamooo
# @Site :
# @File : ht_23.py
# @Software: PyCharm
"""
实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。
输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
注意每个输入文件有多组输入，即多个字符串用回车隔开
输入描述:
字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。

输出描述:
删除字符串中出现次数最少的字符后的字符串。
输入
abcdd

输出
dd
"""

while True:
    try:
        str = input()
        result = []
        num = []
        for s in str:
            num.append(str.count(s))
        min_num = min(num)

        for i,j in zip(str,num):
            if j != min_num:
                result.append(i)
        print(''.join(result))
    except:
        break