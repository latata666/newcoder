# -*- coding: utf-8 -*-
# @Time : 2020/6/18 16:03
# @Author : Mamamooo
# @Site :
# @File : ht_38.py
# @Software: PyCharm
"""
假设一个球从任意高度自由落下，每次落地后反跳回原高度的一半; 再落下, 求它在第5次落地时，共经历多少米?第5次反弹多高？
最后的误差判断是小数点6位
"""

while True:
    try:
        high = int(input())
        sum = high
        for i in range(1,5):
            sum += 2*high*(1/2)**i
        bound = float(high*(1/2)**5)

        print('%g'%sum)
        print('%g'%bound)
    except:
        break
