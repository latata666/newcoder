# -*- coding: utf-8 -*-
# @Time : 2020/5/13 17:06
# @Author : Mamamooo
# @Site :
# @File : ht_20_re.py
# @Software: PyCharm

"""
密码要求:
1.长度超过8位
2.包括大小写字母.数字.其它符号,以上四种至少三种
3.不能有相同长度超2的子串重复
说明:长度超过2的子串
输入描述:
一组或多组长度超过2的子符串。每组占一行
输出描述:
如果符合要求输出：OK，否则输出NG
"""

import re

while True:
    try:
        str = input()
        a = re.findall(r'(.{3,}).*\1',str)
        b1 = re.findall(r'\d',str)
        b2 = re.findall(r'[a-z]',str)
        b3 = re.findall(r'[A-Z]',str)
        b4 = re.findall(r'[^a-zA-Z0-9]',str)
        print(a)
        print(b1,b2,b3,b4)

        if([b1, b2, b3, b4].count([]) <= 1 and a == [] and len(str) > 8):
            print("OK")
        else:
            print("NG")

    except:
        break
