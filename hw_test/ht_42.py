# -*- coding: utf-8 -*-
# @Time : 2020/6/22 10:18
# @Author : Mamamooo
# @Site :
# @File : ht_42.py
# @Software: PyCharm
"""
Jessi初学英语，为了快速读出一串数字，编写程序将数字转换成英文：
如22：twenty two，123：one hundred and twenty three。
说明：
数字为正整数，长度不超过九位，不考虑小数，转化结果为英文小写；
输出格式为twenty two；
非法数据请返回“error”；
关键字提示：and，billion，million，thousand，hundred。
方法原型：public static String parse(long num)
输入描述:
输入一个long型整数
输出描述:
输出相应的英文写法
"""

def dps(n):
    m1 = 'one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen'.split(',')
    m2 = 'twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety'.split(',')

    if n < 20:
        return m1[n-1:n]
    if n < 100:
        return [m2[n//10 -2 ]] + dps(n%10)
    if n < 1000:
        return [m1[n//100 -1]] + ['hundred'] + ['and'] + dps(n%100)
    else:
        for w,p in enumerate(('thousand','million','billion'),1):
            if (n < 1000 **(w+1)):
                return dps(n//(1000**w)) + [p] + dps(n%1000 ** w)
while True:
    try:
        n = int(input())
        print(' '.join(dps(n)) or 'zero')
    except:
        break
