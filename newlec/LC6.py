# -*- coding: utf-8 -*-
# @Time : 2020/8/27 9:58
# @Author : Mamamooo
# @Site :
# @File : LC6.py
# @Software: PyCharm
"""
求给定的二叉树的后序遍历。
例如：
给定的二叉树为{1,#,2,3},
   1
     \
     2
    /
   3

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
#
# @param root TreeNode类
# @return int整型一维数组
#
class Solution:
    def postorderTraversal(self, root):
        # write code here
        if root == None:
            return []
        stack = [root]
        res = []
        s = stack.pop()
        res.append(s.val)
        if s.left:
            stack.append(s.left)
        if s.right:
            stack.append(s.right)

        return res[::-1]

