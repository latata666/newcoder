# -*- coding: utf-8 -*-
# @Time : 2020/7/6 16:10
# @Author : Mamamooo
# @Site :
# @File : ht_44.py
# @Software: PyCharm
"""
题目描述
问题描述：数独（Sudoku）是一款大众喜爱的数字逻辑游戏。玩家需要根据9X9盘面上的已知数字，推算出所有剩余空格的数字，
并且满足每一行、每一列、每一个粗线宫内的数字均含1-9，并且不重复。
输入：
包含已知数字的9X9盘面数组[空缺位以数字0表示]
输出：
完整的9X9盘面数组

输入描述:
包含已知数字的9X9盘面数组[空缺位以数字0表示]

输出描述:
完整的9X9盘面数组

示例1
输入
0 9 2 4 8 1 7 6 3
4 1 3 7 6 2 9 8 5
8 6 7 3 5 9 4 1 2
6 2 4 1 9 5 3 7 8
7 5 9 8 4 3 1 2 6
1 3 8 6 2 7 5 9 4
2 7 1 5 3 8 6 4 9
3 8 6 9 1 4 2 5 7
0 4 5 2 7 6 8 3 1
输出
5 9 2 4 8 1 7 6 3
4 1 3 7 6 2 9 8 5
8 6 7 3 5 9 4 1 2
6 2 4 1 9 5 3 7 8
7 5 9 8 4 3 1 2 6
1 3 8 6 2 7 5 9 4
2 7 1 5 3 8 6 4 9
3 8 6 9 1 4 2 5 7
9 4 5 2 7 6 8 3 1
"""


def check(lst, row, col, value):
    """
      检测在(row,col)放value是否合适
      1.每行含1-9,不含重复值value
      2.每列含1-9,不含重复值value
      3.3*3区块含1-9,不含重复值value
      """
    # 检测每行
    for i in range(9):
        if lst[i][col] == value:
            return False
    # 检测每列
    for j in range(9):
        if lst[row][j] == value:
            return False
    # 检测元素所在3*3区域
    area_row = (row // 3) * 3
    area_col = (col // 3) * 3
    for i in range(area_row, area_row + 3):
        for j in range(area_col, area_col + 3):
            if lst[i][j] == value:
                return False
    return True


def solve(lst, count):
    # 遍历每一个未填的元素，遍历1-9替换为合适的数字
    # 递归出口
    if count == 81:
        for i in range(9):
            print(' '.join(map(str, lst[i])))
    row = count // 9    # 行标
    col = count % 9     # 列标
    #print(row,col)
    if lst[row][col] == 0:  # 未填充
        for i in range(1, 10):
            #print(i)
            if check(lst, row, col, i):     # 找到可能的填充数
                lst[row][col] = i
                solve(lst, count + 1)        # 是否可完成
            # 不可完成
            lst[row][col] = 0   # 回溯
    else:   # 已填充
        solve(lst, count + 1)


while True:
    try:
        lst = []
        for i in range(9):
            lst.append(list(map(int, input().split(' '))))

        # print(lst)

        solve(lst, 0)

    except:
        break
