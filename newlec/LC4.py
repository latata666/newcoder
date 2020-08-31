# -*- coding: utf-8 -*-
# @Time : 2020/8/18 10:47
# @Author : Mamamooo
# @Site :
# @File : LC4.py
# @Software: PyCharm
"""

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @param head ListNode类
# @return ListNode类

class Solution:
    def sortList(self, head):
        # write code here
        a = []
        p = head
        while p != None:
            a = a.append(p.val)
            p = p.next

        a = sorted(a)
        newhead = ListNode(0)
        q = newhead
        for tmp in a:
            q.next = tmp
            q = q.next

        return newhead.next

head = ListNode(3)
s = Solution()
s.sortList(head)


