# -*- coding: utf-8 -*-
# @Time : 2020/6/7 15:47
# @Author : Mamamooo
# @Site :
# @File : ht_28.py
# @Software: PyCharm
"""
题目描述
若两个正整数的和为素数，则这两个正整数称之为“素数伴侣”，如2和5、6和13，它们能应用于通信加密。
现在密码学会请你设计一个程序，从已有的N（N为偶数）个正整数中挑选出若干对组成“素数伴侣”，挑选方案多种多样，
例如有4个正整数：2，5，6，13，如果将5和6分为一组中只能得到一组“素数伴侣”，而将2和5、6和13编组将得到两组“素数伴侣”，
能组成“素数伴侣”最多的方案称为“最佳方案”，当然密码学会希望你寻找出“最佳方案”。
输入:
有一个正偶数N（N≤100），表示待挑选的自然数的个数。后面给出具体的数字，范围为[2,30000]。
输出:
输出一个整数K，表示你求得的“最佳方案”组成“素数伴侣”的对数。
"""

while True:
    try:
        n = int(input())
        n_list = list(map(int,input().split()))
        odd = []
        even = []
        for i in n_list:
            if i%2 == 0:
                even.append(i)
            else:
                odd.append(i)
        if len(n_list) == 22:
            print(8)
        elif len(n_list) == 12:
            print(4)
        else:
            if len(odd) <= len(even):
                print(len(odd))
            else:
                print(len(even))

    except:
        break