# -*- coding: utf-8 -*-
# @Time : 2020/7/13 15:20
# @Author : Mamamooo
# @Site :
# @File : btree_test.py
# @Software: PyCharm
"""

"""
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.parent = None

    def insertleft(self, value):
        self.left = TreeNode(value)
        self.left.parent = self
        return self.left

    def insertright(self, value):
        self.right = TreeNode(value)
        self.right.parent = self
        return self.right

    def show(self):
        print(self.val)

# 手动创建一个二叉树:root是根节点，a、b分别为root的左右子节点，c、d分别为a的左右子节点，e是b的左子节点
root = TreeNode('R')
a = root.insertleft('A')
b = root.insertright('B')
c = a.insertleft('C')
d = a.insertright('D')
e = b.insertleft('E')




