# -*- coding: utf-8 -*-
# @Time : 2020/7/17 17:33
# @Author : Mamamooo
# @Site :
# @File : lec_123.py
# @Software: PyCharm
"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
"""

class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        dp_i_0 = 0
        dp_i_1 = float('-inf')
        dp_pre_0 = 0
        for i in range(n):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0,dp_i_1+prices[i])
            dp_i_1 = max(dp_i_1,dp_pre_0-prices[i])
            dp_pre_0 = tmp

        return dp_i_0


prices = [3,3,5,0,0,3,1,4]

s = Solution()
print(s.maxProfit(prices))