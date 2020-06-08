# -*- coding: utf-8 -*-

"""
将一个罗马数字转化为阿拉伯数字，范围在1-3999。下面是罗马数字的介绍及基本规则：
罗马数字采用七个罗马字母作数字、即Ⅰ（1）、X（10）、C（100）、M（1000）、V（5）、L（50）、D（500）
"""

class Solution(object):
    def RomaToInt(self,s):
        map = {"M":1000, "D":500,"C":100, "L":50, "X":10,"V":5,"I":1}

        result = 0
        for i in range(len(s)):
          if i > 0 and map[s[i]] > map[s[i-1]]:
              print (map[s[i]])
              result -= map[s[i-1]]
              result += map[s[i]] - map[s[i-1]]
          else:
              result += map[s[i]]
        return result

if __name__ == "__main__":
    #print (Solution().RomaToInt("XII"))
    # print(Solution().RomaToInt("XXI") )
    print( Solution().RomaToInt("XCI") )