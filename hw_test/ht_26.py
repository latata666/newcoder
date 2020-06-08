# -*- coding: utf-8 -*-
# @Time : 2020/6/7 9:19
# @Author : Mamamooo
# @Site :
# @File : ht_26.py
# @Software: PyCharm
"""
编写一个程序，将输入字符串中的字符按如下规则排序。
规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。
如，输入： Type 输出： epTy
规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。
如，输入： BabA 输出： aABb
规则 3 ：非英文字母的其它字符保持原来的位置。
如，输入： By?e 输出： Be?y
"""

while True:
    try:
        str = input()
        # res是最终返回的字符串的列表形式，char是提取的英文字母。
        res,char = [False] * len(str),[]
        # 经过这个循环，把相应的非英文字母及其位置存储到了res中。并且把英文字母提取出来了
        for i,v in enumerate(str):
            if v.isalpha():
                char.append(v)
                print(char)
            else:
                res[i] = v
        # 使用lambda表达式排序，暴力有效。
        char.sort(key=lambda c:c.lower())
        print(char)

        # 将char中对应的字符填到res中。
        for i,v in enumerate(res):
            if not v:
                res[i] = char[0]
                char.pop(0)
                print(char,res)
        print("".join(res))
    except:
        break