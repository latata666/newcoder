# -*- coding: utf-8 -*-
# @Time : 2020/6/15 10:56
# @Author : Mamamooo
# @Site :
# @File : lec_322_coinChange.py
# @Software: PyCharm
"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1
输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
"""

class Solution:
    def coinChange(self,coins: List[int],amount: int) ->int:

        return