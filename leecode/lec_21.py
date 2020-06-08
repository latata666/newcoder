# -*- coding: utf-8 -*-
# @Time : 2020/5/28 15:48
# @Author : Mamamooo
# @Site :
# @File : lec_21.py
# @Software: PyCharm
"""
将两个有序的链表拼接成一个有序的链表。
注意点：
不需要额外申请节点， 主要把原链表中的节点串联起来
原链表中的一个已经全部在新链表中后， 另一个链表剩余的部分可以直接拼接
例子：
输入: l1 = 1->2->4, l2 = 3 输出: 1->2->3->4
"""

class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self,l1,l2):
        temp = ListNode(-1)
        head = temp
        while l1 and l2:
            if l1.val > l2.val:
                temp.next = l2
                print("if",temp.val,temp.next.val)
                l2 = l2.next
            else:
                temp.next = l1
                l1 = l1.next
                print("else",temp.val, temp.next.val)
            temp = temp.next
        if l1:
                temp.next = l1
        else:
                temp.next = l2
        return head.next

if __name__ == "__main__":
            s = Solution().mergeTwoLists(ListNode(3),ListNode(2)).val
            print(s)