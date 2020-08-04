# -*- coding: utf-8 -*-
# @Time : 2020/7/14 16:53
# @Author : Mamamooo
# @Site :
# @File : lec_725.py
# @Software: PyCharm
"""
你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。
每个拨轮可以自由旋转：例如把 '9' 变为  '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。
示例 1:
输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
输出：6
解释：
可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
因为当拨动到 "0102" 时这个锁就会被锁定。
"""
import collections

class Solution:
    def openLock(self, deadends, target):
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1,1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i+1:]

        dead = set(deadends)
        queue = collections.deque([('0000',0)])
        seen = {'0000'}
        while queue:
            node,depth = queue.popleft()
            if node == target:
                return depth
            if node in dead:
                continue
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei,depth + 1))
        return -1

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
s = Solution()
reslut = s.openLock(deadends,target)

print(reslut)








