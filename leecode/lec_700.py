# -*- coding: utf-8 -*-
# @Time : 2020/8/7 9:59
# @Author : Mamamooo
# @Site :
# @File : lec_700.py
# @Software: PyCharm
"""
给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。
返回以该节点为根的子树。 如果节点不存在，则返回 NULL。
例如，
给定二叉搜索树:
        4
       / \
      2   7
     / \
    1   3
和值: 2
你应该返回如下子树:
      2
     / \
    1   3
在上述示例中，如果要找的值是 5，但因为没有节点值为 5，我们应该返回 NULL。
"""
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Soultion:
    def searchBST(self,root,val):
        if root == None:
            return False
        if root.val == val:
            return True
        if root.val < val:
            return self.searchBST(root.right,val)
        if root.val > val:
            return self.searchBST(root.left,val)

        #return self.searchBST(root.left,val) or self.searchBST(root.right,val)





