# -*- coding: utf-8 -*-

"""
找出一个列表中三个元素之和与目标值最接近的情况，并返回这个值。假设整个列表中只有一个最接近的值。
"""


class Solution(object):
    def threeSumClosest(self,nums,target):
        nums.sort()
        print (nums)
        i = 0
        result = 0
        distance = pow(2,32) - 1
        for i in range(len(nums)):
                print ("i",i)
                j = i + 1
                print ("j",j)
                k = len(nums) - 1
                while j < k:
                    l = [nums[i],nums[j],nums[k]]
                    print ("l",l)
                    if sum(l) == target:
                        return target
                    if abs(sum(l) - target) < distance:
                        result = sum(l)
                        distance = abs(sum(l) - target)
                        print ("result,distance",result,distance)
                    elif sum(l) > target:
                        k -= 1
                    else:
                        j += 1
        return result


if __name__ == "__main__":
    print (Solution().threeSumClosest([1, 2, 3, 4], 1))