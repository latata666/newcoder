

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for index,value in enumerate(nums):
            print(index,value)
            hash_map[value] = index
            print(hash_map)
        for index1 , value in enumerate(nums):
            if target - value in hash_map:
                index2 = hash_map[target - value]
                if index1 != index2:
                    return [index1+1,index2+1]




numbers=[2, 7, 11, 15]
target = 9
s = Solution()
t = s.twoSum(numbers,target)
print(t)