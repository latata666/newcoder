# -*- coding: utf-8 -*-
# @Time : 2020/6/11 13:51
# @Author : Mamamooo
# @Site :
# @File : ht_32.py
# @Software: PyCharm
"""
题目描述
Catcher是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，比如像这些ABBA，ABA，A，123321，
但是他们有时会在开始或结束时加入一些无关的字符以防止别国破解。比如进行下列变化 ABBA->12ABBA,ABA->ABAKK,123321->51233214　。
因为截获的串太长了，而且存在多种可能的情况（abaaab可看作是aba,或baaab的加密形式），Cathcer的工作量实在是太大了，
他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？
输入描述:
输入一个字符串
输出描述:
返回有效密码串的最大长度
示例1
输入
ABBA
输出
4
"""

def check(alist):
    res = 0
    n = len(alist)
    print("check",alist,n)
    for i in range(n-1):
        if alist[i] == alist[i+1]:
            first = i
            last = i+1
            while (first >= 0 and last < (n) and alist[first] == alist[last]):
                first -= 1
                last += 1
            print("double",first,last,res)
            res = max(res,last-first-1)
        if alist[i-1] == alist[i+1]:
            first = i-1
            last = i+1
            while (first >= 0 and last < (n) and alist[first] == alist[last]):
                first -= 1
                last += 1
            print("single", first, last, res)
            res = max(res,last-first-1)
    return res

while True:
    try:
        alist = input().strip()
        res = check(alist)
        print(res)
    except:
        break
