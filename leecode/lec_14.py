# -*- coding: utf-8 -*-

"""
找出一组字符串中最长的公共前缀。
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        longest = strs[0]
        for i in range(len(strs[0])):
            print (i)
            for str in strs:
                print (str)
                print ("test",len(str),strs[0][i],str[i])
                if len(str) <= i or strs[0][i] != str[i]:
                    print (i, str)
                    return strs[0][:i]

        return strs[0]

if __name__ == "__main__":
  print (Solution().longestCommonPrefix(["heaallo", "heabc", "heacall"]))