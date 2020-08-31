# -*- coding: utf-8 -*-
# @Time : 2020/8/18 17:20
# @Author : Mamamooo
# @Site :
# @File : LC9.py
# @Software: PyCharm
"""
题目描述
对于一个给定的链表，返回环的入口节点，如果没有环，返回null
拓展：
你能给出不利用额外空间的解法么？
"""


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param head ListNode类
# @return ListNode类
#
class Solution:
    def detectCycle(self, head):
        # write code here
        slow = head
        fast = head
        while slow and fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return None
            if slow == fast:
                res = head
                while res != slow:
                    res = res.next
                    slow = slow.next
                return res

        return None