# -*- coding: utf-8 -*-

"""
找出一个列表中四个元素之和为目标值的情况，打印出所有的情况。
输入: nums=[1, 0, -1, 0, -2, 2]
输出: [[-1, 0, 0, 1], [-2, 0, 0, 2], [-2, -1, 1, 2]]
"""

class Solution(object):
    def fourSum(self,nums,target):
        if len(nums) < 4:
            return []
        result = set()
        sumIndexes = {}
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if nums[i] + nums[j] in sumIndexes:
                    sumIndexes[nums[i] + nums[j]].append(i,j)
                else:
                    sumIndexes[nums[i] + nums[j]] == [(i,j)]

            for i in range(len(nums)):
                for j in range(i + 1,len(nums)):
                    sumNeeded = target - (nums[i] + nums[j])
                    if sumNeeded in sumIndexes:
                        for index in sumIndexes[sumNeeded]:
                            if index[0] > j:
                                result.add(tuple(sorted(nums[i],nums[j],nums[index[0],nums[index[1]]])))
                                result = [list(l) for l in result]
                                return result

if __name__ =="__main_":
   print(Solution().fourSum([1,0,-1,0,-2,2],0))
