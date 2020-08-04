# -*- coding: utf-8 -*-
# @Time : 2020/7/8 9:36
# @Author : Mamamooo
# @Site :
# @File : lec_509.py
# @Software: PyCharm
"""
斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，
后面的每一项数字都是前面两项数字的和。也就是：
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
给定 N，计算 F(N)。
示例 1：

输入：2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1.
"""

# class Solution:
#     def fib(self, N: int) -> int:
#         if N <= 1:
#             return N
#         return self.fib(N-1) + self.fib(N-2)
#
# solution = Solution()
#
# print(solution.fib(4))

# class Solution:
#     def fib(self, N: int) -> int:
#         if N <= 1:
#             return N
#         return self.memoize(N)
#
#     def memoize(self,N:int) -> {}:
#         cache = {0: 0,1: 1}
#         for i in range(2,N+1):
#             cache[i] = cache[i-1] + cache[i-2]
#
#         return cache[N]

class Solution:
    def fib(self, N: int) -> int:
        if (N == 1 | N ==2):
            return 1
        prev = 1
        cur = 1
        for i in range(3,N+1):
            sum = prev + cur
            prev = cur
            cur = sum

        return cur


solution = Solution()

print(solution.fib(5))


