# -*- coding: utf-8 -*-

"""
计算字符串最后一个单词的长度，单词以空格隔开。
"""

# def str_count(str):
#     print(len(str))
#     for i in range(len(str)):
#         print(i)
#         if str[len(str)-1-i]==' ':
#             count=i
#             break
#         else:
#             count=i+1
#     print(count)
#
# str_count("hello world")


class Solution:
    def evalRPN(self, tokens):
        # write code here
        list2 = ['+', '-', '*', '/']
        list3 = []
        for i in tokens:
            if i not in list2:
                list3.append(int(i))
            else:
                a = list3.pop()
                print(a)
                b = list3.pop()
                print('b',b)
                if i == '+':
                    c = a + b
                elif i == '-':
                    c = b - a
                elif i == '*':
                    c = b * a
                elif i == '/':
                    c = int(b / a)
                list3.append(c)
        return list3[0]


tokens = ["2", "1", "+", "3", "*"]
a1 = Solution()
a1.evalRPN(tokens)