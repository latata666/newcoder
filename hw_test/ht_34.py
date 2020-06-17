# -*- coding: utf-8 -*-
# @Time : 2020/6/16 14:04
# @Author : Mamamooo
# @Site :
# @File : ht_34.py
# @Software: PyCharm
"""
输入描述:
Lily使用的图片包括"A"到"Z"、"a"到"z"、"0"到"9"。输入字母或数字个数不超过1024。
输出描述:
Lily的所有图片按照从小到大的顺序输出
输入
Ihave1nose2hands10fingers
输出
0112Iaadeeefghhinnnorsssv
"""

while True:
    try:
        lily = input()
        if len(lily) >1024 :
            break
        tmp = ''.join(sorted(lily))
        print(tmp)
    except:
        break

