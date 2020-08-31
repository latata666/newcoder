# -*- coding: utf-8 -*-
# @Time : 2020/8/18 16:40
# @Author : Mamamooo
# @Site :
# @File : LC10.py
# @Software: PyCharm
"""
题目描述
判断给定的链表中是否有环
扩展：
你能给出空间复杂度的解法么？
"""


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param head ListNode类
# @return bool布尔型
#
class Solution:
    def hasCycle(self, head):
        # write code here
        p = head
        while p:
            p_next = p.next
            if p_next == head:
                return True
            p.next = head
            p = p_next

        return False


# class Solution:
#     def hasCycle(self, head):
#         # write code here
#         if not head:
#             return False
#         fast = head
#         slow = head
#         while fast and slow:
#             slow = slow.next
#             if fast.next:
#                 fast = fast.next.next
#             else:
#                 return False
#             if slow == fast:
#                 return True
#
#         return False