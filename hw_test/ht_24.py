# -*- coding: utf-8 -*-
# @Time : 2020/5/18 16:18
# @Author : Mamamooo
# @Site :
# @File : ht_24.py
# @Software: PyCharm
"""
计算最少出列多少位同学，使得剩下的同学排成合唱队形
说明：

N位同学站成一排，音乐老师要请其中的(N-K)位同学出列，使得剩下的K位同学排成合唱队形。
合唱队形是指这样的一种队形：设K位同学从左到右依次编号为1，2…，K，他们的身高分别为T1，T2，…，TK，   则他们的身高满足存在i（1<=i<=K）使得T1<T2<......<Ti-1<Ti>Ti+1>......>TK。
你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。

请注意处理多组输入输出！

"""
import bisect

def deal(l,res):
    b = [9999]*len(l)
    # 每次向b中加一个list中的元素
    print(b)
    b[0] = l[0]
    print(b)
    res = res + [1]
    print(res)
    for i in range(1,len(l)):
        pos = bisect.bisect_left(b,l[i])
        print(pos)
        res += [pos + 1]
        b[pos] = l[i]
    return res




while True:
    try:
        n = int(input())
        s = list(map(int,input().split()))
        print(s)
        dp1 = []
        dp2 = []
        dp1 = deal(s,dp1)
        dp2 = deal(s[::-1],dp2)[::-1]
        a = max(dp1[i] + dp2[i] for i in range(n))
        print(n-a+1)

    except:
        break

