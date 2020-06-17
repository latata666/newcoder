# -*- coding: utf-8 -*-
# @Time : 2020/6/16 9:50
# @Author : Mamamooo
# @Site :
# @File : ht_33.py
# @Software: PyCharm
"""
原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，
然后把这个二进制数转变成一个长整数。
输入
1 输入IP地址
2 输入10进制型的IP地址
输出
1 输出转换成10进制的IP地址
2 输出转换后的IP地址
"""

def ipTostr(ip):
    num = ''
    #print(len(ip))
    for i in range(len(ip)):
        #print(int(ip[i]))
        num += bin(int(ip[i]))[2:].rjust(8,'0')

    return int(num,2)

def strToip(num):
    ips = []
    n = bin(num).replace('0b','').rjust(32,'0')
    #print(n)
    for i in range(4):
        ips.append(str(int(n[8*i:8*i+8],2)))
    return ips


while True:
    try:
        ip = input().split('.')
        num = int(input())
        num1 = ipTostr(ip)
        print(num1)
        ip1 = strToip(num)
        tmp = ".".join(ip1)
        print(tmp)

    except:
        break


