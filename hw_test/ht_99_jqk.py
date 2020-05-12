"""
计算24点是一种扑克牌益智游戏，随机抽出4张扑克牌，通过加(+)，减(-)，乘(*), 除(/)四种运算法则计算得到整数24，
本问题中，扑克牌通过如下字符或者字符串表示，其中，小写joker表示小王，大写JOKER表示大王：

                   3 4 5 6 7 8 9 10 J Q K A 2 joker JOKER

本程序要求实现：输入4张牌，输出一个算式，算式的结果为24点。
"""

import math
import itertools


def pre_joker(joker):
    joker = joker.split(" ")
    list = []
    if len(joker) != 4:
        print("ERROR")
        return False
    for i in range(len(joker)):
        if joker[i] == "joker" or joker[i] == "JOKER":
            print("ERROR")
            return "ERROR"
        else:
            list.append(joker[i])
    print(list)
    return list


if __name__ == "__main__":
    joker = input()
    pre_joker(joker)
    print(joker)
