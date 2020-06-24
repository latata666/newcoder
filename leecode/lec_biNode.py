# -*- coding: utf-8 -*-
# @Time : 2020/6/23 10:47
# @Author : Mamamooo
# @Site :
# @File : lec.py
# @Software: PyCharm
"""
二叉树数据结构TreeNode可用来表示单向链表（其中left置空，right为下一个链表节点）。实现一个方法，
把二叉搜索树转换为单向链表，要求值的顺序保持不变，转换操作应是原址的，也就是在原始的二叉搜索树上直接修改。
返回转换后的单向链表的头节点。
输入： [4,2,5,1,3,null,6,0]
输出： [0,null,1,null,2,null,3,null,4,null,5,null,6]"
"""

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBinNode(self,root: TreeNode) -> TreeNode:
        def convert(root):
            begin = end = root
            if root:
                if root.left:
                    begin,end = convert(root.left)
                    end.right = root
                    end = root
                    root.left = None
                if root.right:
                    root.right,end = convert(root.right)

            return begin,end
        return convert(root)[0]
