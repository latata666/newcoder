# -*- coding: utf-8 -*-
# @Time : 2020/7/17 14:41
# @Author : Mamamooo
# @Site :
# @File : lec_567.py
# @Software: PyCharm
"""
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
换句话说，第一个字符串的排列之一是第二个字符串的子串。
示例1:
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
"""


class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        hashmap = {}
        for i in s1:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        m, n, count = len(s1), len(s2), len(s1)
        for i in range(m):
            if s2[i] not in hashmap:
                continue
            elif hashmap[s2[i]] > 0:
                count -= 1
            hashmap[s2[i]] -= 1
        if count == 0:
            return True
        for i in range(n - m):
            if s2[i] in hashmap:
                if hashmap[s2[i]] >= 0:
                    count += 1
                hashmap[s2[i]] += 1
            if s2[i + m] in hashmap:
                if hashmap[s2[i + m]] > 0:
                    count -= 1
                hashmap[s2[i + m]] -= 1
            if count == 0:
                return True
        return False


s1 = "ab"
s2 = "eidbooao"

s = Solution()

print(s.checkInclusion(s1, s2))
