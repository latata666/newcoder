# -*- coding: utf-8 -*-

"""
讲一个字符串转化成int类型。题目非常简单，但要额外考虑的因素非常多，
如下面的一些字符串的处理："+123", " -23 ", "231ji2", null, " "等等。
"""

class Solution(object):
    def myAtoi(self,str):
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        # Check None situation
        if not str:
            return 0
        str = str.strip()
        if not str :
            return 0

        flag = 1
        if str[0] in ['+','-']:
            if str[0] == '-':
                flag  = -1
            str = str[1:]
        if not str or not str[0].isdigit():
            return 0
        for i,v in enumerate(str):
            if not v.isdigit():
                str = str[:i]
                break
        result = 0
        for v in str[:]:
            result += ord(v) - ord('0')
            result *= 10
        result /= 10
        result *= flag
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN

        return result

if __name__ == "__main__":
    print( Solution().myAtoi(" -1123"))
    print( Solution().myAtoi("222222222222222"))
