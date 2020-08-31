# -*- coding: utf-8 -*-
# @Time : 2020/7/17 17:25
# @Author : Mamamooo
# @Site :
# @File : lec_122.py
# @Software: PyCharm
"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
示例 1:
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
"""
class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = float('-inf')
        for i in range(n):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0,dp_i_1+prices[i])
            dp_i_1 = max(dp_i_1,tmp-prices[i])

        return dp_i_0


#prices = [7,1,5,3,6,4]
prices = [1,9,6,9,1,7,1,1,5,9,9,9]
s = Solution()
print(s.maxProfit(prices))