# -*- coding: utf-8 -*-
# @Time : 2020/6/28 14:03
# @Author : Mamamooo
# @Site :
# @File : ht_43_2.py
# @Software: PyCharm
"""
迷宫问题
输入描述:
输入两个整数，分别表示二位数组的行数，列数。再输入相应的数组，其中的1表示墙壁，0表示可以走的路。
数据保证有唯一解,不考虑有多解的情况，即迷宫只有一条通道。
输出描述:
左上角到右下角的最短路径，格式如样例所示。
"""


deals = [lambda x,y:[x + 1, y], #向下
         lambda x,y:[x ,y + 1], #向右
         lambda x,y:[x - 1, y], #向上
         lambda x,y:[x ,y - 1], #向左
]

def deal_maze(start,end,maze):
    path = []
    path.append(start)
    maze[0][0] =2
    while len(path) > 0:
        curnode = path[-1]
        if curnode[0] == end[0] and curnode[1] == end[1]:
            for i in path:
                print('(' + str(i[0]) + ',' + str(i[1]) + ')')

        for deal in deals:
            nextnode = deal(curnode[0],curnode[1])
            if 0 <= nextnode[0] <= end[0] and 0 <= nextnode[1] <= end[1]:
                if maze[nextnode[0]][nextnode[1]] == 0:
                    path.append(nextnode)
                    #print(path)
                    maze[nextnode[0]][nextnode[1]] =2
                    break
        else:
            path.pop()


while True:
    try:
        [a,b] = [int(i) for i in input().split()]
        m = []
        for i in range(a):
            m.append([int(i) for i in input().split()])

        print(m,a,b)
        path = deal_maze([0,0],(a-1,b-1),m)


    except:
        break