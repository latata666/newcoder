# -*- coding: utf-8 -*-

"""
将一个int型的数字转化为罗马数字，范围在1-3999。
罗马数字采用七个罗马字母作数字、即Ⅰ（1）、X（10）、C（100）、M（1000）、V（5）、L（50）、D（500）
"""

class Solution(object):
    def intToRoman(self,num):
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        strings = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        result = ''
        for i in range(len(nums)):
            while num >= nums[i]:
                num -= nums[i]
                result += strings[i]
        return result

if __name__ == "__main__":
    print (Solution().intToRoman(12))
    print(Solution().intToRoman(21) )
    print( Solution().intToRoman(31) )