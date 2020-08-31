# -*- coding: utf-8 -*-
# @Time : 2020/8/7 10:35
# @Author : Mamamooo
# @Site :
# @File : lec_701.py
# @Software: PyCharm
"""
给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。
保证原始二叉搜索树中不存在新值。
注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回任意有效的结果。
例如, 
给定二叉搜索树:

        4
       / \
      2   7
     / \
    1   3

和 插入的值: 5
你可以返回这个二叉搜索树:

         4
       /   \
      2     7
     / \   /
    1   3 5
或者这个树也是有效的:

         5
       /   \
      2     7
     / \
    1   3
         \
          4
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return TreeNode(val)
        if root.val < val:
            root.right =  self.insertIntoBST(root.right,val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left,val)
        return root

root = TreeNode(4,TreeNode(2),TreeNode(7))
val = 5
s = Solution()
node = s.insertIntoBST(root,val)
print(node.val,node.left.val)





