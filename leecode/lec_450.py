# -*- coding: utf-8 -*-
# @Time : 2020/8/6 16:07
# @Author : Mamamooo
# @Site :
# @File : lec_450.py
# @Software: PyCharm
"""
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，
并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
一般来说，删除节点可分为两个步骤：
首先找到需要删除的节点；
如果找到了，删除它。
说明： 要求算法时间复杂度为 O(h)，h 为树的高度。
示例:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。

一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。

    5
   / \
  4   6
 /     \
2       7

另一个正确答案是 [5,2,6,null,4,null,7]。

    5
   / \
  2   6
   \   \
    4   7
"""

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMin(self,node):
        while node.left != None:
            node = node.left
        return node

    def deleteNode(self,root,key):
        if root == None:
            return None
        if root.val == key:
            if root.left == None:
                return root.right
            if root.right == None:
                return root.left
            minNode = self.getMin(root.right)
            root.val = minNode.val
            root.right = self.deleteNode(root.right,minNode.val)
        elif root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)

        return root


root = TreeNode(10,TreeNode(5),TreeNode(15,TreeNode(6),TreeNode(20)))
key = 15

s = Solution()
node1 = s.deleteNode(root,key)

print(node1.val,node1.left.val,node1.right.val)


