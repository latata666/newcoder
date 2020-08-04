# -*- coding: utf-8 -*-
# @Time : 2020/7/17 15:55
# @Author : Mamamooo
# @Site :
# @File : lec_188.py
# @Software: PyCharm
"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
示例 1:
输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
"""


# class Solution:
#     def maxProfit(self, prices,k):
#         n = len(prices)
#         if k > n // 2:
#             return self.maxProfit(prices,1)
#
#         dp = [[[[0 for i in range(n)] for j in range(k)] for p in range(n)]]
#         print(n,dp)
#         for i in range(n):
#             for m in range(k,1,-1):
#                 #print(i)
#                 dp[i][m][0] = max(dp[i-1][m][0],dp[i-1][m][1] + prices[i])
#                 dp[i][m][1] = max(dp[i-1][m][1],dp[i-1][m-1][0]-prices[i])
#
#         return dp[n-1][m][0]

class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        dp_i10 = 0
        dp_i11 = float('-inf')
        dp_i20 = 0
        dp_i21 = float('-inf')

        for i in range(n):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0,dp_i_1+prices[i])
            dp_i_1 = max(dp_i_1,dp_pre_0-prices[i])
            dp_pre_0 = tmp

        return dp_i_0


prices = [3,3,5,0,0,3,1,4]

s = Solution()
print(s.maxProfit(prices))
