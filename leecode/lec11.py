# -*- coding: utf-8 -*-

"""
给定一组长短不一的隔板，挑其中的两块板，使得板子之间能装最多的水。
注意点：

两块板之间能装多少水是由短的那块板决定的
选定两块板之后，它们之间的板就不存在了
"""


class Solution(object):
    def maxArea(self, height):
        if not height :
            return 0
        left = 0
        right = len(height) - 1
        result = 0
        while left < right:
            if height[left] < height[right]:
                area = height[left] * (right - left)
                result = max(result, area)
                left += 1
            else:
                area = height[right] * (right - left)
                result = max(result, area)
                right -= 1
        return result

if __name__ == "__main__":
   print (Solution().maxArea([1,1]) )