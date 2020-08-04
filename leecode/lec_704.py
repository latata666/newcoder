# -*- coding: utf-8 -*-
# @Time : 2020/7/16 14:24
# @Author : Mamamooo
# @Site :
# @File : lec_704.py
# @Software: PyCharm
"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
示例 1:
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为4
"""
# class Solution:
#     def search(self, nums, target):
#         left,right = 0, len(nums) -1
#         while left <= right:
#             pivot = left + (right -left)//2
#             if nums[pivot] == target:
#                 return pivot
#             if target < nums[pivot]:
#                 right = pivot -1
#             else:
#                 left = pivot + 1
#
#         return -1

class Solution:
    def search(self, nums, target):
        left,right = 0,len(nums) -1
        while left <= right:
            mid = left + (right -left) // 2
            if (nums[mid] < target):
                left = mid + 1
            elif (nums[mid] > target):
                right = mid - 1
            elif (nums[mid] == target):
                left = mid + 1

        if (right < 0 | nums[right] != target):
            return -1
        return right


nums = [-1,0,3,5,7,2,9,12]
target = 9
s = Solution()

result = s.search(nums,target)
print(result)


