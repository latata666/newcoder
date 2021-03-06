# -*- coding: utf-8 -*-
# @Time : 2020/5/26 9:31
# @Author : Mamamooo
# @Site :
# @File : lec_19.py
# @Software: PyCharm
"""
将一个链表中的倒数第n个元素从链表中去除。
输入: list = 1->2->3->4->5, n = 2.
输出: 1->2->3->5
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def myPrint(self):
            print(self.val)
            if self.next:
                self.next.myPrint()

class Solution(object):
    def removeNthFromEnd(self,head,n):
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        cur = dummy
        while prev and n >= 0:
            prev = prev.next
            n -= 1
        while prev:
            prev = prev.next
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next

if __name__ =="__main__":
    n5 = ListNode(5)
    n4 = ListNode(4)
    n3 = ListNode(3)
    n2 = ListNode(2)
    n1 = ListNode(1)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    result = Solution().removeNthFromEnd(n1,5)
    result.myPrint()





