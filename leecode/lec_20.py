# -*- coding: utf-8 -*-
# @Time : 2020/5/27 16:21
# @Author : Mamamooo
# @Site :
# @File : lec_20.py
# @Software: PyCharm
"""
判断一个只包含各种括号符号的字符串中括号的匹配情况。
注意点：
字符串中只会包含"(",")","[","]","{","}"这些字符
括号匹配要注意顺序， 字符串"([)]"是错误的匹配
例子：
输入: s="(){}" 输出: True
输入: s="(){}[" 输出: False
"""

class Solution(object):
    def isValid(self,s):
        if len(s) % 2 == 1:
            return False
        stack =[]
        left = ("(","[","{")
        right = (")","]","}")
        zip(left,right)
        for v in s:
            if v in left:
                stack.append(v)
            else:
                if not stack:
                    return False
                p = stack.pop()
                if left.index(p) != right.index(v):
                    return False
        return len(stack) == 0

if __name__ == "__main__":
    print(Solution().isValid("({}){}"))
    print(Solution().isValid("({)}"))
    print(Solution().isValid("}}}"))
    print(Solution().isValid("((("))
