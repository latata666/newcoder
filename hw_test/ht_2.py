# -*- coding: utf-8 -*-

"""
写出一个程序，接受一个由字母和数字组成的字符串，和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写。
"""

str = "ABCDEF12aa4235abckhsdkjfh"
target = "a"


def mycount(str,target):
    count = 0
    for i in range(len(str)):
        if (str[i] == target or str[i] == target.upper()):
            count = count + 1
    return count

print(mycount(str,target))

