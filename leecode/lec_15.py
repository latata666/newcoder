# -*- coding: utf-8 -*-

"""
找出一个列表中所有和为零的三元组。要求求出的三元组中没有重复。
"""

class Solution(object):
    def threeSum(self, nums):
        print (nums)
        nums.sort()
        print (nums)
        result = []
        i = 0
        print (len(nums))
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                l = [nums[i], nums[j], nums[k]]
                if sum(l) == 0:
                    result.append(l)
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif sum(l) > 0:
                    k -= 1
                else:
                    j += 1
            i += 1

            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result



if __name__ == "__main__":
    print (Solution().threeSum([-1, 0, 1, 2, -1, -4]) )