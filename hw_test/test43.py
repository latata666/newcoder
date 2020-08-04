deals = [lambda x, y: [x + 1, y],  # 向下
         lambda x, y: [x, y + 1],  # 向右
         lambda x, y: [x - 1, y],  # 向上
         lambda x, y: [x, y - 1],  # 向左
         ]


def deal_maze(start, end, maze):
    path = []  # 走过的路径
    path.append(start)
    maze[0][0] = 2  # 走过的路径记为2m
    while len(path) > 0:
        curnode = path[-1]
        if curnode[0] == end[0] and curnode[1] == end[1]:
            for i in path:
                print('(' + str(i[0]) + ',' + str(i[1]) + ')')

        for deal in deals:
            nextnode = deal(curnode[0], curnode[1])
            if 0 <= nextnode[0] <= end[0] and 0 <= nextnode[1] <= end[1]:
                # 判断没有出迷宫
                if maze[nextnode[0]][nextnode[1]] == 0:
                    path.append(nextnode)
                    # print(path)
                    maze[nextnode[0]][nextnode[1]] = 2
                    break
        else:
            path.pop()


while True:
    try:
        [a, b] = list(map(int, input().split()))  # a为行,b为列
        maze = []  # 迷宫本身
        for i in range(a):
            maze.append([int(j) for j in input().split()])
        deal_maze([0, 0], (a - 1, b - 1), maze)
    except:
        break