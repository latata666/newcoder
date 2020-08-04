# -*- coding: utf-8 -*-
# @Time : 2020/7/7 15:23
# @Author : Mamamooo
# @Site :
# @File : ht_45.py
# @Software: PyCharm
"""
题目描述
给出一个名字，该名字有26个字符串组成，定义这个字符串的“漂亮度”是其所有字母“漂亮度”的总和。
每个字母都有一个“漂亮度”，范围在1到26之间。没有任何两个字母拥有相同的“漂亮度”。字母忽略大小写。
给出多个名字，计算每个名字最大可能的“漂亮度”。
输入描述:
整数N，后续N个名字

输出描述:
每个名称可能的最大漂亮程度

示例1
输入
2
zhangsan
lisi

输出
192
101
"""

# 计算每个名字最大可能的“漂亮度”
# 意味着每个字母的漂亮度没确定
# 那就是如果哪个字母出现最多次，就把26给它，依次往后

while True:
    try:
        num = int(input())

        for i in range(num):
            name = input().strip()
            dic = {}
            for i in name:
                if i in dic:
                    dic[i] += 1
                else:
                    dic[i] = 1

            # d是待排序的字典
            # 得到的是一个列表
            lst_order = sorted(dic.items(),key=lambda i:i[1],reverse=True)
            print(lst_order)

            # 遍历列表内容，按顺序把从高到低的漂亮度给他并加和
            score = 0
            for i in range(len(lst_order)):
                score += lst_order[i][1] * (26-i)


            print(score)

    except:
        break



