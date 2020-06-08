# -*- coding: utf-8 -*-
# @Time : 2020/5/22 16:37
# @Author : Mamamooo
# @Site :
# @File : lec_189rotatearray.py
# @Software: PyCharm
"""
将一个数组中的数字右旋k位， 即所有的数字向后移k位， 末尾的数字移到开头。
注意点：
使用尽可能多的方法来解决提供一种只需要O(1)空间的解法
例子:
输入: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
输出: [5, 6, 7, 1, 2, 3, 4]
"""

class Solution(object):
    def rotate(self,nums,k):
        def reverse(nums,start,end):
            while start < end:
                nums[start],nums[end] = nums[end],nums[start]
                start += 1
                end -= 1
        n = len(nums)
        k %= n
        reverse(nums,0,n-k-1)
        reverse(nums,n-k,n-1)
        reverse(nums,0,n-1)

if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    Solution().rotate(nums,10)
    print(nums)