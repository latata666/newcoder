# -*- coding: utf-8 -*-
# @Time : 2020/5/12 17:21
# @Author : Mamamooo
# @Site :
# @File : ht_20.py
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


def pre_str(str):
    if len(str) <= 8:
        return False
    else:
        return True

def count_str(str):
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    for c in str:
        if 'a' <= c <= 'z':
            num1 = 1
        elif 'A' <= c <= 'Z':
            num2 = 1
        elif '1' <= c <= '9':
            num3 = 1
        else:
            num4 = 1
    if (num1 + num2 + num3 + num4) >= 3:
        return True
    else:
        return False

def judge(str):
    for i in range(len(str) - 3):
        if str[i:i+3] in str[i+1:]:
            return False
            break
    return True

while True:
    try:
        str = input()
        if pre_str(str) and count_str(str) and judge(str):
            print("OK")
        else:
            print("NG")
    except:
        break