# -*- coding: utf-8 -*-
# @Time : 2020/5/11 14:21
# @Author : Mamamooo
# @Site :
# @File : ht_15.py
# @Software: PyCharm
"""
输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。
"""

# while True:
# #     try:
# #         n = int(input())
# #         r = 0
# #         while n:
# #             if n & 1:
# #                 r += 1
# #             n = n // 2
# #         print(r)
# #
# #     except:
# #         break

num = int(input())
print(bin(num).count('1'))