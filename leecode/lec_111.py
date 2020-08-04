# -*- coding: utf-8 -*-
# @Time : 2020/7/10 20:09
# @Author : Mamamooo
# @Site :
# @File : lec_111.py
# @Software: PyCharm
"""
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明: 叶子节点是指没有子节点的节点。
示例:
给定二叉树 [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.
"""


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.parent = None

    def insert_left(self, value):
        self.left = TreeNode(value)
        self.left.parent = self
        return self.left

    def insert_right(self, value):
        self.right = TreeNode(value)
        self.right.parent = self
        return self.right

    def show(self):
        print(self.val)



#方法一
# class Solution:
#     def minDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         children = [root.left, root.right]
#         if not any(children):
#             return 1
#         min_depth = float('inf')
#         for c in children:
#             if c:
#                 min_depth = min(self.minDepth(c), min_depth)
#
#         return min_depth + 1


#node = TreeNode([3, 9, 20, None, None, 15, 7])

#方法二：深度优先搜索迭代

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            stack ,min_depth = [(1,root),],float('inf')

        while stack:
            depth,root = stack.pop()
            children = [root.left,root.right]
            if not any(children):
                min_depth = min(depth,min_depth)
            for c in children:
                if c:
                    stack.append((depth + 1,c))

        return min_depth











root = TreeNode(3)
a1 = root.insert_left(9)
a2 = root.insert_right(20)
b1 = a1.insert_left(15)
b2 = a1.insert_right(7)
b3 = a2.insert_left(31)
b4 = a2.insert_right(7)
c1 = b1.insert_left(15)
c2 = b1.insert_right(7)
c3 = b2.insert_left(31)
c4 = b2.insert_right(7)
c5 = b3.insert_left(15)
c6 = b3.insert_right(7)
c7 = b4.insert_left(31)
c8 = b4.insert_right(7)

d1 = c1.insert_right(23)
d2 = c2.insert_left(23)



s = Solution()
x = s.minDepth(root)
print(x)
