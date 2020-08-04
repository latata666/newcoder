# -*- coding: utf-8 -*-
# @Time : 2020/7/16 14:37
# @Author : Mamamooo
# @Site :
# @File : lec_34.py
# @Software: PyCharm
"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。
示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
"""

class Solution:
    def searchRange(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break
        else:
            return [-1,-1]
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] == target:
                right_idx = j
                break

        return [left_idx,right_idx]


nums = [5,7,7,8,8,10]
target = 8
s = Solution()
result = s.searchRange(nums,target)
print(result)






