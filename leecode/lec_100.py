# -*- coding: utf-8 -*-
# @Time : 2020/8/5 16:58
# @Author : Mamamooo
# @Site :
# @File : lec_100.py
# @Software: PyCharm
"""
给定两个二叉树，编写一个函数来检验它们是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


p = TreeNode(1,TreeNode(2))
print(p.val)
q = TreeNode(1,TreeNode(1))
print(q.val)

s = Solution()
print(s.isSameTree(p, q))
